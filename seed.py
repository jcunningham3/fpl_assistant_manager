from app import app
from models import Chat, Users, db

#drop and create tables
db.drop_all()
db.create_all()
