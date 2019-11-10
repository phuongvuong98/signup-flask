import unittest

from flask import current_app

from project.users.oauth import OAuthSignIn, FacebookSignIn, TwitterSignIn
from project.utils import Utils
from tests.base import BaseTestCase
from project import bcrypt, db
from project.models import User


class TestUser(BaseTestCase):

    # Ensure email is empty
    def test_empty_email(self):
        with self.client:
            response = self.client.post('/register', data=dict(
                email="",
                password="huhuhu"
            ), follow_redirects=True)
            self.assertIn(b'This field is required.', response.data)

    # Ensure psw is empty
    def test_psw_email(self):
        with self.client:
            response = self.client.post('/register', data=dict(
                email="vuong@gmail.com",
                password=""
            ), follow_redirects=True)
            self.assertIn(b'This field is required.', response.data)

    # Ensure email is correct by format
    def test_format_email(self):
        with self.client:
            response = self.client.post('/register', data=dict(
                email="huhu@1asdsad",
                password="huhuhu"
            ), follow_redirects=True)
            self.assertIn(b'Invalid email address.', response.data)

    # Ensure user can register by input username and password
    def test_user_registeration(self):
        with self.client:
            response = self.client.post('/register', data=dict(
                email='vuong@gmail.com',
                password='huhuhuhu'
            ), follow_redirects=True)
            self.assertIn(b'You sign up successful.', response.data)
            user = User.query.filter_by(email='vuong@gmail.com').first()
            self.assertTrue(str(user) == '<email - vuong@gmail.com>')

    # Ensure errors are thrown during an incorrect user registration
    def test_incorrect_user_registeration(self):
        with self.client:
            response = self.client.post('/register', data=dict(
                email='vuongvuong',
                password='huhuhu'
            ), follow_redirects=True)
            self.assertIn(b'Invalid email address.', response.data)

    # Ensure given password is correct after unhashing
    def test_check_password(self):
        psw = Utils.hash_password("password")
        self.assertTrue(bcrypt.check_password_hash(psw, 'password'))

    # Ensure class OAuthSignIn inited
    def test_OAuthSignIn_inited(self):
        with self.client:
            oauth = OAuthSignIn('facebook')
            self.assertTrue(oauth.get_callback_url(), current_app.config['OAUTH_CREDENTIALS']['facebook']['callbackUrl'])

    # Ensure class FacebookSignIn inited
    def test_FacebookSignIn_inited(self):
        with self.client:
            oauth_fb = FacebookSignIn()
            self.assertTrue(oauth_fb.get_callback_url(), current_app.config['OAUTH_CREDENTIALS']['facebook']['callbackUrl'])

    # Ensure class TwitterSignIn inited
    def test_TwitterSignIn_inited(self):
        with self.client:
            oauth_tw = TwitterSignIn()
            self.assertTrue(oauth_tw.get_callback_url(), current_app.config['OAUTH_CREDENTIALS']['twitter']['callbackUrl'])

    # Ensure class user modal inited
    def test_user_modal_inited(self):
        user = User(email="haha3@gmail.com", password="huhu")
        db.session.add(user)
        db.session.commit()
        user_check = User.query.filter_by(email='haha3@gmail.com').first()
        self.assertTrue(user_check.email, 'haha3@gmail.com')


if __name__ == '__main__':
    unittest.main()
