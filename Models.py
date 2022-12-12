from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Posts(db.Model):
    rowid = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), unique=True, nullable=False)
    date = db.Column(db.String(200), nullable=False)
    content = db.Column(db.String(), nullable=False)

    def __str__(self):
        return "\nTitle: {}. \ndate: {}. \nContent: {}.\n\n".format(
            self.title,
            self.date,
            self.content
        )

    def serialize(self):
        return {
            'rowid': self.rowid,
            'title': self.title,
            'date': self.date,
            'content': self.content
        }