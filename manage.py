import unittest
import os
import coverage

from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand

from project import app, db


# app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqldb://root@localhost:3306/BLOG_EX?charset=utf8mb4"
app.config['SECRET_KEY'] = '\xbf\xb0\x11\xb1\xcd\xf9\xba\x8bp\x0c...'
# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqldb://root:Admin123@35.198.199.71/BLOG?unix_socket=/cloudsql/original-glider-246113:asia-southeast1:data-blog-93123"
app.config['SQLALCHEMY_ECHO'] = False
app.config['SQLALCHEMY_RECORD_QUERIES'] = "enable"
app.config['MYSQL_DATABASE_CHARSET'] = 'utf8mb4'

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


@manager.command
def test():
    """Runs the unit tests without coverage."""
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


# @manager.command
# def cov():
#     """Runs the unit tests with coverage."""
#     cov = coverage.coverage(
#         branch=True,
#         include='project/*'
#     )
#     cov.start()
#     tests = unittest.TestLoader().discover('tests')
#     unittest.TextTestRunner(verbosity=2).run(tests)
#     cov.stop()
#     cov.save()
#     print 'Coverage Summary:'
#     cov.report()
#     basedir = os.path.abspath(os.path.dirname(__file__))
#     covdir = os.path.join(basedir, 'coverage')
#     cov.html_report(directory=covdir)
#     cov.erase()


if __name__ == '__main__':
    manager.run()
