from os import path
import csv
from app import flaskApp, models, db
from .models import User, Station, Post
from flask import render_template, redirect, request, flash, jsonify
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(flaskApp)

@flaskApp.route('/')
@flaskApp.route('/home')
def home_func():
    return render_template('map-display.html')

@flaskApp.route('/login')
def login_func():
    return render_template('userLogin.html', is_submission_page=True)

@flaskApp.route('/check_login', methods=['POST'])
def check_login():
    data = request.get_json()
    username = data['username']
    password = data['password']

    user = User.query.filter_by(user_name=username).first()
    print(user)
    if user and bcrypt.check_password_hash(user.user_password_hash, password):
        return jsonify({'success': True})
    else:
        return jsonify({'success': False}), 401
    
@flaskApp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data['username']
    password = data['password']
    email = data['email']
    phone = data['phone']

    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')

    new_user = User(user_name=username, user_password_hash=hashed_password, user_email=email, user_phone=phone)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'})

@flaskApp.route('/submission')
def submission_func():
    return render_template('user_submission.html', is_submission_page=True)

@flaskApp.route('/leaderboard')
def leaderboard_func():
    return render_template('leaderboard.html')


@flaskApp.route('/profile')
def profile_func():
    return render_template('userProfile.html')

@flaskApp.route('/trial', methods = ["POST"])
def trial_func():
    input_data = request.form
    street = input_data.get('place')
    print(street)
    all_stations = Station.query.all()
    returned_row = []
    count = 0
    for s in all_stations:
        name = str(s.station_name.lower())
        if street.lower() in name:
            inner_row = [s.station_name, s.station_address, s.station_phone_number, s.station_postcode]
            returned_row.append(inner_row)
            count += 1
    print(returned_row)
    return jsonify({"text": returned_row})

@flaskApp.route('/map-submit', methods = ["POST"])
def map_input_func():
    data = request.form
    name = data.get('station_name')
    address = data.get('address')
    postcode = data.get('postcode')
    phone = data.get('phone_num')
    new_station = Station(station_name = name, station_postcode = postcode, station_phone_number = phone, station_address = address)
    db.session.add(new_station)
    print(new_station)
    db.session.commit()
    print("Received data:", data)
    return jsonify({"message": "Data received successfully"})


'''
: WHEN USER AND SUBMISSION PAGES ARE CONNECTED TO DATABASES
@flaskApp.route('/submit', methods=["POST"])
def submit():
    return render_template('listGroup.html')
'''



