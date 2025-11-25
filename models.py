
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    # connection esta. between department and user table
    #department_id = db.Column(db.Integer, db.ForeignKey('departments.id'), nullable=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(50), nullable=False)      # e.g. 'doctor', patients,'admin'
    Created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    
# patient model
class Patient(db.Model):
    __tablename__ = 'patients'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(10))
    contact = db.Column(db.String(15))
    address = db.Column(db.Text)

# Doctor model
class Doctor(db.Model):
    __tablename__ = 'doctors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    specialization = db.Column(db.String(100))
    contact = db.Column(db.String(15))
    department_id = db.Column(db.Integer, db.ForeignKey('departments.id'), nullable=True)
    



class Department(db.Model):
    __tablename__ = 'departments'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    # Relationship one department can have many doctors 
    doctors = db.relationship("Doctor", backref="department", lazy=True)

    @property
    def doctors_registered(self):
        return len(self.doctors)
    


#Appointment model
class Appointment(db.Model):
    __tablename__ = 'appointments'
    id = db.Column(db.Integer, primary_key=True)
    #Foreignkey
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'), nullable=False)
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'), nullable=False)
    date = db.Column(db.Date)
    time = db.Column(db.Time)
    status = db.Column(db.String(60), nullable=False, default="Booked") # booked, complted, cancle    
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    #Relationship
    patient = db.relationship('Patient', backref='appointments')
    doctor = db.relationship('Doctor', backref='appointments')
    



class Treatment(db.Model):
    __tablename__='treatments'
    id = db.Column(db.Integer, primary_key=True)
    appointment_id = db.Column(db.Integer, db.ForeignKey('appointments.id'), nullable=False)
    diagnosis = db.Column(db.Text, nullable=False)
    prescription = db.Column(db.Text)
    notes = db.Column(db.Text)
    appointment = db.relationship("Appointment", backref="treatments")
    

