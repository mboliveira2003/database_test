from flask import Flask, jsonify, request
import os
import psycopg2
from psycopg2 import connect, Error
from psycopg2.extras import NamedTupleCursor
from datetime import datetime, timedelta


# Database URL
DB = os.environ.get('DATABASE_URL', "postgres://username:password@localhost:5432/database")

# Flask application instance
app = Flask(__name__)

@app.route("/", methods=("GET",))
def get_all_clinicas():
    """#### Returns all the clinics in the database."""
    
    with connect(DB) as conn:
        with conn.cursor(cursor_factory=NamedTupleCursor) as cur:

            try:
                # Fetch the name and address of all the clinics in the database
                cur.execute("SELECT nome, morada FROM clinica", {})
                clinicas = cur.fetchall()
                return jsonify(clinicas), 200
            
            except Error as e:
                return jsonify({"status": "error", "message": "Não foi possível executar o pedido: " + e.pgerror}), 400

@app.route("/c/<clinica>/", methods=("GET",))
def get_specialties_by_clinic(clinica):
    """ #### Returns all the specialties offered by a given clinic.
        Args:
            - clinic (str): The name of the clinic.
    """

    with connect(DB) as conn:
        with conn.cursor(cursor_factory=NamedTupleCursor) as cur:

            try:
                # Verify if the clinic exists in the database
                cur.execute("SELECT 1 FROM clinica WHERE nome = %s", (clinica,))
                if not cur.fetchone():
                    return jsonify({"status": "error", "message": f"A {clinica} nao existe."}), 404
                
                # Join doctor and work tables by doctor's nif.
                # Then return the specialties of the doctors that work in the provided clinic.
                cur.execute("SELECT DISTINCT especialidade FROM medico JOIN trabalha ON medico.nif = trabalha.nif WHERE trabalha.nome = %s", (clinica,))
                specialties = cur.fetchall()
                return jsonify(specialties), 200

            except Error as e:
                return jsonify({"status": "error", "message": "Não foi possível executar o pedido: " + e.pgerror}), 400

@app.route("/c/<clinica>/<especialidade>/", methods=("GET",))
def get_doctors_by_clinic_and_specialty(clinica, especialidade):
    """ #### Returns all the doctors that work in a given clinic and have a given specialty, and their first 3 available dates and time for an appointment.
        Args:
            - clinica (str): The name of the clinic.
            - especialidade (str): The specialty of the doctor.
    """
    with connect(DB) as conn:
        with conn.cursor(cursor_factory=NamedTupleCursor) as cur:
            try:
                
                # Verify if the clinic exists in the database
                cur.execute("SELECT 1 FROM clinica WHERE nome = %s", (clinica,))
                if not cur.fetchone():
                    return jsonify({"status": "error", "message": f"A {clinica} nao existe."}), 404

                # Join tables doctor and work by doctor's nif.
                # Then return the name and nif of the doctors that work in the provided clinic and have the provided specialty.
                cur.execute("SELECT medico.nome, medico.nif FROM medico JOIN trabalha ON medico.nif = trabalha.nif WHERE trabalha.nome = %s AND medico.especialidade = %s", (clinica, especialidade))
                doctors = cur.fetchall()

                # If there are no doctors with the provided specialty in the clinic, return an error message
                if not doctors:
                    return jsonify({"status": "error", "message": f"Nao existem medicos com a especialidade {especialidade} na {clinica}."}), 404

                # List to store the response
                response = []
            
                # For each computed doctor, find the first 3 available dates and times for an appointment
                for doctor in doctors:
                    # List to store the available appointments
                    available_appointments = []
                    
                    # Start from the current date and time.
                    current_time = datetime.now()

                    # For the current day, compute the first valid consultation time.
                    first_possible_time = datetime(current_time.year, current_time.month, current_time.day, current_time.hour + 2 if current_time.hour <= 21 else current_time.hour, 0)

                    while len(available_appointments) < 3:
                        # Check if the time is between 8:00 and 13:00 or between 14:00 and 19:00
                        if  8 <= first_possible_time.hour < 13 or 14 <= first_possible_time.hour < 19:

                            # Check if the doctor is already booked for the current time
                            cur.execute("""
                                SELECT 1 
                                FROM consulta 
                                WHERE nif = %s AND data = %s AND hora = %s
                            """, (doctor.nif, first_possible_time.date().strftime('%Y-%m-%d'), first_possible_time.time().strftime('%H:%M:00')))

                            # If the doctor is not booked, check if he works in the clinic at the date of the appointment
                            if not cur.fetchone():

                                # Add 1 to the day of the week to match the format of the database
                                day_of_week = first_possible_time.weekday() + 1 if first_possible_time.weekday() < 6 else 0

                                # If the doctor works in the clinic at the date of the appointment, add the appointment to the list
                                cur.execute("""
                                    SELECT 1
                                    FROM trabalha
                                    WHERE nif = %s AND nome = %s AND dia_da_semana = %s
                                """, (doctor.nif, clinica, day_of_week))
                                if cur.fetchone():
                                    available_appointments.append((first_possible_time.date().strftime('%Y-%m-%d'), first_possible_time.time().strftime('%H:%M:00')))

                        # Increment the time by 30 minutes
                        first_possible_time += timedelta(minutes=30)
                    
                    # Append the doctor's name and the available appointments to the response list
                    doctor_info = {
                        "nome": doctor.nome,
                        "availableAppointments": [{"data": appt[0], "hora": appt[1]} for appt in available_appointments]
                    }
                    response.append(doctor_info)
             
                return jsonify(response), 200
            
            except Error as e:
                return jsonify({"status": "error", "message": "Não foi possível executar o pedido: " + e.pgerror}), 400
                    
@app.route('/a/<clinica>/registar/', methods=['POST'])
def register_appointment(clinica):
    """ #### Registers a new appointment in the database.
        Args:
            - clinica (str): The name of the clinic.

        Request parameters:
            - paciente (str): The name of the patient.
            - medico (str): The name of the doctor.
            - data (str): The date of the appointment (YYYY-MM-DD).
            - hora (str): The time of the appointment (HH:MM:00).
    """

    # Get the parameters from the request
    patient_ssn = request.args.get("paciente")
    doctor_nif = request.args.get("medico")
    appointment_date = request.args.get("data")
    appointment_time = request.args.get("hora")

    # Verify if all the parameters are present
    if not all([patient_ssn, doctor_nif, appointment_date, appointment_time]):
        # Fetch the parameters that are missing
        missing_params = [param for param in ["paciente", "medico", "data", "hora"] if not request.args.get(param)]
        # Return an error message with the missing parameters
        return jsonify({"status": "error", "message": f"Faltam os parâmetros {', '.join(missing_params)} no pedido."}), 400
    
    # Validate the format of the time
    try:
        datetime.strptime(appointment_time, "%H:%M:00")
    except ValueError:
        return jsonify({"status": "error", "message": "Formato de hora inválido. Por favor use HH:MM:00."}), 400
    
    # Split the time string by ':' and check if the hour is between 8 and 13 or between 14 and 19, and in 30-minute intervals
    split_time_string = appointment_time.split(":")
    if not (8 <= int(split_time_string[0]) < 13 or 14 <= int(split_time_string[0]) < 19) or int(split_time_string[1]) % 30 != 0:
        return jsonify({"status": "error", "message": "A hora da consulta tem de ser entre as 8:00 e as 13:00 ou entre as 14:00 e as 19:00 e em intervalos de 30 minutos (Ex: 08:00:00; 08:30:00)"}), 400
    
    # Validate the format of the date
    try:
        datetime.strptime(appointment_date, "%Y-%m-%d")
    except ValueError:
        return jsonify({"status": "error", "message": "Formato de data inválido. Por favor use YYYY-MM-DD."}), 400

    # Verify if the inserted date-time is in the future
    if datetime.strptime(appointment_date + " " + appointment_time, "%Y-%m-%d %H:%M:00") < datetime.now():
        return jsonify({"status": "error", "message": "A data e hora da consulta têm de ser futuras."}), 400

    with connect(DB) as conn:
        with conn.cursor(cursor_factory=NamedTupleCursor) as cur:
            try:
                # Verify if the clinic exists in the database
                cur.execute("SELECT 1 FROM clinica WHERE nome = %s", (clinica,))
                if not cur.fetchone():
                    return jsonify({"status": "error", "message": f"A {clinica} nao existe."}), 404
                
                # Verify if the patient exists in the database
                cur.execute("SELECT 1 FROM paciente WHERE ssn = %s", (patient_ssn,))
                if not cur.fetchone():
                    return jsonify({"status": "error", "message": f"O paciente (ssn: {patient_ssn}) nao existe."}), 404
                
                # Verify if the doctor exists in the database
                cur.execute("SELECT 1 FROM medico WHERE nif = %s", (doctor_nif,))
                if not cur.fetchone():
                    return jsonify({"status": "error", "message": f"O medico (nif: {doctor_nif}) nao existe."}), 404
                
                # Verify if the doctor is available at the date and time of the appointment
                cur.execute("""
                    SELECT 1
                    FROM consulta
                    WHERE nif = %s AND data = %s AND hora = %s
                """, (doctor_nif, appointment_date, appointment_time))
                if cur.fetchone():
                    return jsonify({"status": "error", "message": f"O medico (nif: {doctor_nif}) ja tem uma consulta marcada para dia {appointment_date} às {appointment_time}."}), 400
                
                # Verify if the patient already has an appointment at the date and time of the appointment
                cur.execute("""
                    SELECT 1
                    FROM consulta
                    WHERE ssn = %s AND data = %s AND hora = %s
                """, (patient_ssn, appointment_date, appointment_time))
                if cur.fetchone():
                    return jsonify({"status": "error", "message": f"O paciente (ssn: {patient_ssn}) ja tem uma consulta marcada para dia {appointment_date} às {appointment_time}."}), 400
                
                # Verify if the doctor works in the given clinic at the date of the appointment
                day_of_week_python = datetime.strptime(appointment_date, "%Y-%m-%d").weekday()
                # Add 1 to the day of the week to match the format of the database
                day_of_week_sql = day_of_week_python + 1 if day_of_week_python < 6 else 0

                cur.execute("""
                    SELECT 1
                    FROM trabalha
                    WHERE nif = %s AND nome = %s AND dia_da_semana = %s
                """, (doctor_nif, clinica, day_of_week_sql))
                if not cur.fetchone():
                    return jsonify({"status": "error", "message": f"O medico (nif: {doctor_nif}) nao trabalha na {clinica} na data {appointment_date}."}), 400
                
                # Make sure the id sequence is updated
                cur.execute("""
                    SELECT setval('consulta_id_seq', COALESCE((SELECT MAX(id) FROM consulta) + 1, 1), false);
                """)

                # Insert the appointment in the database 
                cur.execute("""
                    INSERT INTO consulta (ssn, nif, nome, data, hora) 
                    VALUES (%s, %s, %s, %s,%s)
                """, (patient_ssn, doctor_nif, clinica, appointment_date, appointment_time))    

                conn.commit()
                return jsonify({"status": "Consulta marcada com sucesso!"}), 201
            
            except psycopg2.Error as e:
                conn.rollback()
                return jsonify({"status": "error", "message": f"Não foi possível realizar a marcação da consulta: " + e.pgerror}), 400
            
@app.route('/a/<clinica>/cancelar/', methods=['DELETE'])
def cancel_appointment(clinica):
        """#### Cancels an appointment, by removing it from the database.
        Args:
            - clinica (str): The name of the clinic.
        
        Request parameters:
            - paciente (str): The name of the patient.
            - medico (str): The name of the doctor.
            - data (str): The date of the appointment (YYYY-MM-DD).
            - hora (str): The time of the appointment (HH:MM:00).
        """
    
        # Get the parameters from the request
        patient_ssn = request.args.get("paciente")
        doctor_nif = request.args.get("medico")
        appointment_date = request.args.get("data")
        appointment_time = request.args.get("hora")

        # Verify if all the parameters are present
        if not all([patient_ssn, doctor_nif, appointment_date, appointment_time]):
            # Fetch the parameters that are missing
            missing_params = [param for param in ["paciente", "medico", "data", "hora"] if not request.args.get(param)]
            # Return an error message with the missing parameters
            return jsonify({"status": "error", "message": f"Faltam os parâmetros {', '.join(missing_params)} no pedido."}), 400
        
        # Validate the format of the date
        try:
            datetime.strptime(appointment_date, "%Y-%m-%d")
        except ValueError:
            return jsonify({"status": "error", "message": "Formato de data inválido. Por favor use YYYY-MM-DD."}), 400
        
        # Validate the format of the time
        try:
            datetime.strptime(appointment_time, "%H:%M:00")
        except ValueError:
            return jsonify({"status": "error", "message": "Formato de hora inválido. Por favor use HH:MM:00."}), 400
        
        # Split the time string by ':' and check if the hour is between 8 and 13 or between 14 and 19, and in 30-minute intervals
        split_time_string = appointment_time.split(":")
        if not (8 <= int(split_time_string[0]) < 13 or 14 <= int(split_time_string[0]) < 19) or int(split_time_string[1]) % 30 != 0:
            return jsonify({"status": "error", "message": "A hora da consulta tem de ser entre as 8:00 e as 13:00 ou entre as 14:00 e as 19:00 e em intervalos de 30 minutos (Ex: 08:00:00; 08:30:00)"}), 400

        # Verify if the inserted date-time is in the future
        if datetime.strptime(appointment_date + " " + appointment_time, "%Y-%m-%d %H:%M:00") < datetime.now():
            return jsonify({"status": "error", "message": "A data e hora da consulta têm de ser futuras."}), 400
    
        with connect(DB) as conn:
            with conn.cursor(cursor_factory=NamedTupleCursor) as cur:
                try:
                    # Verify if the clinic exists in the database
                    cur.execute("SELECT 1 FROM clinica WHERE nome = %s", (clinica,))
                    if not cur.fetchone():
                        return jsonify({"status": "error", "message": f"A {clinica} nao existe."}), 404
                    
                    # Verify if the patient exists in the database
                    cur.execute("SELECT 1 FROM paciente WHERE ssn = %s", (patient_ssn,))
                    if not cur.fetchone():
                        return jsonify({"status": "error", "message": f"O paciente (ssn: {patient_ssn}) nao existe."}), 404
                    
                    # Verify if the doctor exists in the database
                    cur.execute("SELECT 1 FROM medico WHERE nif = %s", (doctor_nif,))
                    if not cur.fetchone():
                        return jsonify({"status": "error", "message": f"O medico (nif: {doctor_nif}) nao existe."}), 404
                    
                    # Verify if the doctor works in the clinic at the date of the appointment
                    day_of_week_python = datetime.strptime(appointment_date, "%Y-%m-%d").weekday()
                    # Add 1 to the day of the week to match the format of the database
                    day_of_week_sql = day_of_week_python + 1 if day_of_week_python < 6 else 0

                    cur.execute("""
                        SELECT 1
                        FROM trabalha
                        WHERE nif = %s AND nome = %s AND dia_da_semana = %s
                    """, (doctor_nif, clinica, day_of_week_sql))
                    if not cur.fetchone():
                        return jsonify({"status": "error", "message": f"O medico (nif: {doctor_nif}) nao trabalha na {clinica} na data {appointment_date}."}), 400
                    
                    # Delete all rows that match the provided parameters and return the number of rows affected
                    cur.execute("""
                        DELETE FROM consulta 
                        WHERE ssn = %s AND nif = %s AND nome = %s AND data = %s AND hora = %s
                    """, (patient_ssn, doctor_nif, clinica, appointment_date, appointment_time))

                    # If there is no row affected, the appointment does not exist
                    if cur.rowcount == 0:
                        conn.rollback()
                        return jsonify({"status": "error", "message": f"A consulta fornecida nao existe."}), 404
                    
                    conn.commit()
                    return jsonify({"status": "Consulta cancelada com sucesso!"}), 200
                except psycopg2.Error as e:
                    conn.rollback()
                    return jsonify({"status": "error", "message": e.pgerror}), 400


if __name__ == "__main__":
    print(app.url_map)
    app.run(host="0.0.0.0", port=5000)
