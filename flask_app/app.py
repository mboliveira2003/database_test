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
                cur.execute("SELECT * FROM clinica", {})
                clinicas = cur.fetchall()
                return jsonify(clinicas), 200
            except Error as e:
                return jsonify({"status": "error", "message": e.pgerror}), 400

@app.route("/c/<clinica>/", methods=("GET",))
def get_specialties_by_clinic(clinic):
    """ #### Returns all the specialties offered by a given clinic.
        Args:
            - clinic (str): The name of the clinic.
    """

    with connect(DB) as conn:
        with conn.cursor(cursor_factory=NamedTupleCursor) as cur:
            try:
                # Join doctor and work tables by doctor's nif.
                # Then return the specialties of the doctors that work in the provided clinic.
                cur.execute("SELECT DISTINCT especialidade FROM medico JOIN trabalha ON medico.nif = trabalha.nif WHERE nome = %s", (clinic,))
                specialties = cur.fetchall()
                return jsonify(specialties), 200
            except Error as e:
                return jsonify({"status": "error", "message": e.pgerror}), 400

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
                # Join tables doctor and work by doctor's nif.
                # Then return the name and nif of the doctors that work in the provided clinic and have the provided specialty.
                cur.execute("SELECT medico.nome, medico.nif FROM medico JOIN trabalha ON medico.nif = trabalha.nif WHERE trabalha.nome = %s AND medico.especialidade = %s", (clinica, especialidade))
                doctors = cur.fetchall()

                # List to store the response
                response = []

                # For each computed doctor, find the first 3 available dates and times for an appointment
                for doctor in doctors:
                    # List to store the available appointments
                    available_appointments = []

                    # Start from the current date and time.
                    current_time = datetime.now()

                    # For the current day, compute the first valid consultation time.
                    first_possible_time = datetime(current_time.year, current_time.month, current_time.day, 8, 0)

                    while available_appointments.length < 3:
                        # Check if the time is between 8:00 and 13:00 or between 14:00 and 19:00
                        if  8 <= first_possible_time.hour < 13 or 14 <= first_possible_time.hour < 19:
                            # Check if the doctor is already booked for the current time
                            cur.execute("""
                                SELECT 1 
                                FROM consulta 
                                WHERE nif = %s AND data = %s AND hora = %s
                            """, (doctor.nif, first_possible_time.date().strftime('%Y-%m-%d'), first_possible_time.time().strftime('%H:%M:00')))
                            if not cur.fetchone():
                                available_appointments.append((first_possible_time.date(), first_possible_time.time()))
                        first_possible_time += timedelta(minutes=30)
                    
                    doctor_info = {
                        "nome": doctor.nome,
                        "appointments": [{"data": appt[0], "hora": appt[1]} for appt in available_appointments]
                    }
                    response.append(doctor_info)
                return jsonify(response), 200
            except Error as e:
                return jsonify({"status": "error", "message": e.pgerror}), 400
                    

@app.route('/a/<clinica>/registar/', methods=['POST'])
def register_appointment(clinica):

    # Get the parameters from the request
    patient_ssn = request.args.get("paciente")
    doctor_nif = request.args.get("medico")
    appointment_date = request.args.get("data")
    appointment_time = request.args.get("hora")

    # Verify if the inserted date-time is in the future
    if datetime.strptime(appointment_date + " " + appointment_time, "%Y-%m-%d %H:%M:00") < datetime.now():
        return jsonify({"status": "error", "message": "A data e hora da consulta têm de ser futuras."}), 400

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

    with connect(DB) as conn:
        with conn.cursor(cursor_factory=NamedTupleCursor) as cur:
            try:
                cur.execute("""
                    INSERT INTO consulta (ssn, nif, nome, data, hora) 
                    VALUES (%s, %s, %s, %s,%s)
                """, (patient_ssn, doctor_nif, clinica, appointment_date, appointment_time))
                conn.commit()
                return jsonify({"status": "Consulta marcada com sucesso!"}), 201
            except psycopg2.Error as e:
                conn.rollback()
                return jsonify({"status": "error", "message": e.pgerror}), 400
            
@app.route('/a/<clinica>/cancelar/', methods=['POST'])
def cancel_appointment(clinica):
    
        # Get the parameters from the request
        patient_ssn = request.args.get("paciente")
        doctor_nif = request.args.get("medico")
        appointment_date = request.args.get("data")
        appointment_time = request.args.get("hora")

        # Verify if the inserted date-time is in the future
        if datetime.strptime(appointment_date + " " + appointment_time, "%Y-%m-%d %H:%M:00") < datetime.now():
            return jsonify({"status": "error", "message": "A data e hora da consulta têm de ser futuras."}), 400
    
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
    
        with connect(DB) as conn:
            with conn.cursor(cursor_factory=NamedTupleCursor) as cur:
                try:
                    cur.execute("""
                        DELETE FROM consulta 
                        WHERE ssn = %s AND nif = %s AND nome = %s AND data = %s AND hora = %s
                    """, (patient_ssn, doctor_nif, clinica, appointment_date, appointment_time))
                    conn.commit()
                    return jsonify({"status": "Consulta cancelada com sucesso!"}), 200
                except psycopg2.Error as e:
                    conn.rollback()
                    return jsonify({"status": "error", "message": e.pgerror}), 400
            

