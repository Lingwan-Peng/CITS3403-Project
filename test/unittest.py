import os
import unittest

from unittest import TestCase

from app import create_app, db
from app.models import User, Station, Post
from config import TestConfig
from app.controllers import GroupCreationError, create_group


class BasicUnitTests(TestCase):

    def setUp(self):
        testApp = create_app(TestConfig)
        self.app_context = testApp.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"map-display", response.data)

    def test_login_page(self):
        response = self.client.get('/login')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"userLogin", response.data)

    def test_submission_page(self):
        response = self.client.get('/submission')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"user_submission", response.data)

    def test_leaderboard_page(self):
        response = self.client.get('/leaderboard')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"leaderboard", response.data)

    def test_profile_page_get(self):
        response = self.client.get('/userProfile')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"userProfile", response.data)

    def test_profile_page_post(self):
        with self.app.app_context():
            user = User(user_name='testuser', user_email='test@example.com', user_password_hash='test', user_phone=1234567890)
            db.session.add(user)
            db.session.commit()

        response = self.client.post('/userProfile', data={
            'oldName': 'testuser',
            'newName': 'newname',
            'newEmail': 'newemail@example.com',
            'newPhone': 9876543210,
            'newDOB': '2000-01-01',
            'newBio': 'This is a test bio.'
        })

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['message'], 'Profile updated successfully')

        with self.app.app_context():
            user = User.query.filter_by(user_name='newname').first()
            self.assertIsNotNone(user)
            self.assertEqual(user.user_email, 'newemail@example.com')

    def test_trial_post(self):
        with self.app.app_context():
            station = Station(station_name='Test Station', station_postcode=12345, station_phone_number='555-5555', station_address='123 Test St')
            db.session.add(station)
            db.session.commit()

        response = self.client.post('/trial', data={'place': 'Test'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('Test Station', response.json['text'][0])

    def test_map_input_post(self):
        response = self.client.post('/map-submit', data={
            'station_name': 'New Station',
            'address': '456 New St',
            'postcode': 67890,
            'phone_num': '555-6789'
        })

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json['message'], 'Data received successfully')

        with self.app.app_context():
            station = Station.query.filter_by(station_name='New Station').first()
            self.assertIsNotNone(station)
            self.assertEqual(station.station_address, '456 New St')

    def test_make_unique_nickname(self):
        u = User(nickname='john', email='john@example.com')
        db.session.add(u)
        db.session.commit()
        nickname = User.make_unique_nickname('john')
        assert nickname != 'john'
        u = User(nickname=nickname, email='susan@example.com')
        db.session.add(u)
        db.session.commit()
        nickname2 = User.make_unique_nickname('john')
        assert nickname2 != 'john'
        assert nickname2 != nickname

if __name__ == '__main__':
    unittest.main()