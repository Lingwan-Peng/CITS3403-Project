from typing import Optional
import sqlalchemy as sa
from sqlalchemy import ForeignKey
import sqlalchemy.orm as so
from sqlalchemy.orm import relationship
from app import db

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(120), nullable=False)
    user_password = db.Column(db.String(20), nullable=False)
    user_email = db.Column(db.String(120), nullable=False, unique=True)
    posts = db.relationship('Post', back_populates='post_author')

class Station(db.Model):
    station_id = db.Column(db.Integer, primary_key=True)
    station_name = db.Column(db.String(120), nullable=False)
    station_postcode = db.Column(db.Integer)
    station_phone_number = db.Column(db.String(20))
    station_address = db.Column(db.String(255))
    def __repr__(self):
        return f"<GasStation {self.station_name}, address {self.station_address}>\n"

class Post(db.Model):
    post_id = db.Column(db.Integer, primary_key=True)
    superior_post_id = db.Column(db.String(120), nullable=False)
    post_title = db.Column(db.String(255), nullable=False)
    post_content = db.Column(db.Text, nullable=False)
    post_author_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    post_author = relationship('User', back_populates ='posts')