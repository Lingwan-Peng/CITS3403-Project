from os import path
import csv
from app import flaskApp
from flask import render_template, redirect, request, flash, jsonify

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


@flaskApp.route('/profile')
def profile_func():
    return render_template('userProfile.html')

@flaskApp.route('/trial', methods = ["POST"])
def trial_func():
    input_data = request.form
    street = input_data.get('place')
    print(street)
    file_path = path.join(flaskApp.root_path, 'static', 'trial.csv')
    with open(file_path, newline='') as csvfile:
        reader = list(csv.reader(csvfile))
        reader = reader[1:]
        returned_rows = []
        # Iterate over each row in the CSV file
        for row in reader:
            if street in row[0]:
                returned_rows.append(row)
            elif street in row[1]:
                returned_rows.append(row)
    return jsonify({"text": returned_rows})


'''
: WHEN USER AND SUBMISSION PAGES ARE CONNECTED TO DATABASES
@flaskApp.route('/submit', methods=["POST"])
def submit():
    return render_template('listGroup.html')
'''
