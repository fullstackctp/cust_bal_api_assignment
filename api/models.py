from sqlalchemy import Integer, String, Boolean, DateTime, text, Enum,Date,Text,ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from api import db
from sqlalchemy import CheckConstraint
from datetime import datetime

class User(db.Model):
    uid = db.Column(Integer, primary_key=True)
    name = db.Column(String(100), nullable=False)
    email_id = db.Column(String(120), unique=True, nullable=False)
    gender = db.Column(String(10), nullable=False, server_default='Male')
    registration_date = db.Column(Date)
    age = db.Column(Integer)
    location = db.Column(String(50))
    birthday = db.Column(Date)
    phone_no = db.Column(String(15))
    primary_address = db.Column(Text)
    role = db.Column(db.String(50),ForeignKey("role.uid"), default='user')
    ts_cust = db.relationship("TSCustomer", backref="ts_customer", lazy=True)
    _table_args_ = (
        CheckConstraint(gender.in_(['Male', 'Female', "Others"]), name='check_gender'),
        CheckConstraint(role.in_(['user', 'manager']), name='check_role'),
    )
    def _repr_(self):
        return f'<User {self.name}>'

class TSCustomer(db.Model):
    uid = db.Column(Integer, ForeignKey("user.uid"), nullable=False, primary_key=True)
    cart_id = db.Column(Integer)
    dnt = db.Column(Date)
    def __init__(self,uid, cart_id):
        self.cart_id = cart_id
        self.uid = uid
        self.dnt = datetime.now()
    def _repr_(self):
        return f'<User {self.uid}>'

class Role(db.Model):
    uid = db.Column(Integer, primary_key=True)
    role = db.relationship("User", backref="user", lazy=True)
    user = db.Column(String(50), unique=True, nullable=False)
    def _repr_(self):
        return f'<Role {self.user} - {self.role}>'