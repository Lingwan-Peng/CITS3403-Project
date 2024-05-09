from os import path
import csv
from app import flaskApp, models, db
from .models import User, Station, Post
from flask import render_template, redirect, request, flash, jsonify, url_for

@flaskApp.route('/')
@flaskApp.route('/home')
def home_func():
    return render_template('map-display.html')

@flaskApp.route('/login')
def login_func():
    return render_template('userLogin.html', is_submission_page=True)

@flaskApp.route('/submission')
def submission_func():
    return render_template('user_submission.html', is_submission_page=True)

@flaskApp.route('/leaderboard')
def leaderboard_func():
    # Fetch data for rank and user from your database
    # Example:
    # rank_data = [(user.rank, user.username) for user in User.query.order_by(User.rank).all()]
    # user_data = [(user.username, user.rank) for user in User.query.order_by(User.username).all()]

    # For demonstration purposes, I'm using static data
    rank_data = [("Rank 1", "User 1"), ("Rank 2", "User 2"), ("Rank 3", "User 3")]
    user_data = [("User 1", "Rank 1"), ("User 2", "Rank 2"), ("User 3", "Rank 3")]

    return render_template('leaderboard.html', rank_data=rank_data, user_data=user_data)

@flaskApp.route('/profile')
def profile_func():
    return render_template('userProfile.html')

@flaskApp.route('/trial', methods=["POST"])
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

@flaskApp.route('/map-submit', methods=["POST"])
def map_input_func():
    data = request.form
    name = data.get('station_name')
    address = data.get('address')
    postcode = data.get('postcode')
    phone = data.get('phone_num')
    new_station = Station(station_name=name, station_postcode=postcode, station_phone_number=phone, station_address=address)
    db.session.add(new_station)
    print(new_station)
    db.session.commit()
    print("Received data:", data)
    return jsonify({"message": "Data received successfully"})

# '''
# : WHEN USER AND SUBMISSION PAGES ARE CONNECTED TO DATABASES
# @flaskApp.route('/submit', methods=["POST"])
# def submit():
#     return render_template('listGroup.html')
# '''


