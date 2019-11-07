import unittest

from tests.base import BaseTestCase
from project import bcrypt
from project.models import User


class TestUser(BaseTestCase):

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
        response = self.client.post('/register', data=dict(
            email='vuong@gmail.com',
            password='huhuhuhu'
        ), follow_redirects=True)
        user = User.query.filter_by(email='vuong@gmail.com').first()
        self.assertTrue(bcrypt.check_password_hash(user.password, 'huhuhuhu'))
        self.assertFalse(bcrypt.check_password_hash(user.password, '1234'))

if __name__ == '__main__':
    unittest.main()
