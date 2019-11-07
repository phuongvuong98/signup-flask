from flask.ext.testing import TestCase

from project import app, db
from project.models import User


class BaseTestCase(TestCase):
    """A base test case."""

    def create_app(self):
        app.config.from_object('config.TestConfig')
        return app

    def setUp(self):
        db.create_all()
        db.session.add(User("vuongvuong@gmail.com", "huhu", "", "", "", ""))
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
