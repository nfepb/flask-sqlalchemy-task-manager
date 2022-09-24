from taskmanager import db


class Category(db.Model):
    # schema for the Category model
    id = db.Column(db.Integer, primary_key=True)



class Task(db.Model):
    # schema for the Task model
