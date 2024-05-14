from os import path
import csv
from app import flaskApp, models, db
from .models import User, Station, Post
from flask import render_template, redirect, request, flash, jsonify
import sqlalchemy as sa

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
    return render_template('leaderboard.html')


@flaskApp.route('/userProfile', methods = ['GET', 'POST'])
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

# New route to fetch user's rank
@flaskApp.route('/leaderboard/user', methods=['GET'])
def get_user_rank():
    # Placeholder logic to fetch user's rank from the database
    user_rank = {'rank': 5}  # Placeholder for actual user rank
    return jsonify(user_rank)


# New login route
@flaskApp.route('/login', methods=['GET', 'POST'])
def login_func():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            # Redirect to the user profile page with the user's ID
            return redirect(url_for('profile_func', user_id=user.user_id))
        else:
            flash('Invalid username or password', 'error')
            return redirect(url_for('login_func'))

    return render_template('userLogin.html', is_submission_page=True)


# New user profile route
@flaskApp.route('/userProfile/<int:user_id>', methods=['GET'])
def profile_func(user_id):
    user = User.query.get(user_id)
    if user:
        return render_template('userProfile.html', user=user)
    else:
        flash('User not found', 'error')
        return redirect(url_for('login_func'))

'''
: WHEN USER AND SUBMISSION PAGES ARE CONNECTED TO DATABASES
@flaskApp.route('/submit', methods=["POST"])
def submit():
    return render_template('listGroup.html')
'''





