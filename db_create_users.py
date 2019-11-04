from project import db
from project.models import User

# insert data
db.session.add(User("huhu@realpython.com", "haha", "","","",""))
# db.session.add(User("admin", "ad@min.com", "admin"))
# db.session.add(User("mike", "mike@herman.com", "tell"))

# commit the changes
db.session.commit()
