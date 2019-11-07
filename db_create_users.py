from project import db
from project.models import User

# insert data
db.session.add(User("huhu@realpython.com", "haha", "","","",""))

# commit the changes
db.session.commit()