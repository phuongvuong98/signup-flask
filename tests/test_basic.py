import unittest

from tests.base import BaseTestCase


class FlaskTestCase(BaseTestCase):

    # Ensure that register page loads
    def test_register_route_works_as_expected(self):
        response = self.client.get('/register', follow_redirects=True)
        self.assertIn(b'Register', response.data)


if __name__ == '__main__':
    unittest.main()