from taskmanager import db


class Category(db.Model):
    # schema for the Category model
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(25), unique=True, nullable=False)
    # relationship() to reference the relation but not displayed like Column():
    tasks = db.relationship(
        "Task", backref="category", cascade="all, delete", lazy=True
        )

    def __repr__(self):
        # __repr__ to represent iself in the form of a string
        # like "this" in JS
        return self.category_name


class Task(db.Model):
    # schema for the Task model
    id = db.Column(db.Integer, primary_key=True)
    task_name = db.Column(db.String(50), unique=True, nullable=False)
    task_description = db.Column(db.Text, nullable=False)
    is_urgent = db.Column(db.Boolean, default=False, nullable=False)
    due_date = db.Column(db.DateTime, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey(
        "category.id", ondelete="CASCADE"), nullable=False
        )

    def __repr__(self):
        # __repr__ to represent iself in the form of a string
        return f"#{self.id} - Task:{self.task_name} | Urgent:{self.is_urgent}"
        