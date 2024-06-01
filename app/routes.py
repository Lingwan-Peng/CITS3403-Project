from os import path
import csv
from app import flaskApp, models, db
from .models import User, Station, Post
from flask import render_template, redirect, request, flash, jsonify, url_for
import sqlalchemy as sa
import requests
import json

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
    if user and user.check_password(password):
        return jsonify({'success': True})
    else:
        return jsonify({'success': False}), 401
    
@flaskApp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirmed_password = request.form['confirm_password']
        
        existing_user = User.query.filter_by(user_name=username).first()
        existing_email = User.query.filter_by(user_email=email).first()
        if existing_user or existing_email:
            return jsonify({'success': False, 'new_user': False})

        if password != confirmed_password:
            return jsonify({'success': False, 'new_user': False, 'password_match': False})
        
        hashed_password = hash(password)
        new_user = User(
            user_name=username,
            user_password=hashed_password,
            user_email=email,
        )
        
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'success': True})
    return render_template('register.html')



@flaskApp.route('/submission')
def submission_func():
    return render_template('user_submission.html', is_submission_page=True)

@flaskApp.route('/leaderboard')
def leaderboard_func():
    return render_template('leaderboard.html')



@flaskApp.route('/userProfile', methods=['GET', 'POST'])
# @login_required
def profile_func():
    if request.method == 'POST':
        # Logic to handle the POST request and update the user profile
        data = request.form
        print(data)
        oldName = data.get('oldName')
        name = data.get('newName')
        email = data.get('newEmail')
        phone = data.get('newPhone')
        dob = data.get('newDOB')
        bio = data.get('newBio')
        # update db
        user = User.query.filter_by(user_name=oldName).first()
        if user:
            user.user_name = name
            user.user_email = email
            user.user_phone = phone
            user.user_dob = dob
            user.user_bio = bio

            # Commit changes to the database
            db.session.commit()
            print('user profile updated')
        return jsonify({'message': 'Profile updated successfully'}), 200
    else:
        return render_template('userProfile.html')

@flaskApp.route('/trial', methods=["POST"])
def trial_func():
    input_data = request.form
    user_query = input_data.get('place')
    filter = input_data.get('filter')
    print(filter, "is the filter")
    print(user_query)
    all_stations = Station.query.all()
    returned_row = []
    count = 0
    postcode_str = ''
    for s in all_stations:
        if filter == 'station_name':
            output = str(s.station_name.lower())
        elif filter == 'address':
            output = str(s.station_address.lower())
        elif filter == 'postcode':
            output = str(s.station_postcode)
        elif filter == 'nearby':
            lat_long = user_query.split(":")
            url = f"https://api.geoapify.com/v1/geocode/reverse?lat={lat_long[0]}&lon={lat_long[1]}&format=json&apiKey="
            response = requests.get(url)
            data_dict = response.json()
            postcode_dict = data_dict['results']
            for item in postcode_dict:
                inner = dict(item)
                postcode_str = inner['postcode']
            output = str(s.station_postcode)
        if postcode_str != '':
            print(postcode_str, "is the postcode")
            if postcode_str in output:
                print(postcode_str, "is in the thingy")
                inner_row = [s.station_name, s.station_address, s.station_phone_number, s.station_postcode]
                returned_row.append(inner_row)
                count += 1
        elif user_query.lower() in output:
            print(user_query)
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
    checked = data.get('checked')
    checked_dict = json.loads(checked)

    fuel_types_lst = []
    
    for key, value in checked_dict.items():
        input = f"{key}:{value}"
        fuel_types_lst.append(input)
    
    fuel_types_str = str(fuel_types_lst)
    
    new_station = Station(station_name = name, station_postcode = postcode, station_phone_number = phone, station_address = address, station_fuel_prices = fuel_types_str)
    db.session.add(new_station)
    print(new_station)
    db.session.commit()
    print("Received data:", data)
    return jsonify({"message": "Station added successfully"}), 200


# New route to fetch user's rank
@flaskApp.route('/leaderboard/user', methods=['GET'])
def get_user_rank():
    # Placeholder logic to fetch user's rank from the database
    user_rank = {'rank': 5}  # Placeholder for actual user rank
    return jsonify(user_rank)

@flaskApp.route('/test-redirect')
def test_redirect():
    return redirect('/home')





'''
: WHEN USER AND SUBMISSION PAGES ARE CONNECTED TO DATABASES
@flaskApp.route('/submit', methods=["POST"])
def submit():
  return render_template('listGroup.html')
'''

