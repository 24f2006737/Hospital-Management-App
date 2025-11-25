from datetime import datetime
from hospital_management import db

class user(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    secialzation_id = db.Column(db.Integer, db.Forigenkey('departments.db'), nullable=True)
    username = db.column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    role = db.Column(db.String(20), nullable=False) # e.g. 'doctor', patients,'admin', 'nurse'
    Created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

class Department(db.Model):
    __tablename__ = 'departments'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(255), nullable=True)
    