from app import db
class Report(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(80), unique=True, nullable=False)
  content = db.Column(db.Text, unique=True, nullable=False)

  def __init__(self, title, content):
    self.title = title
    self.content = content

  def serialize(self):
    return {"id": self.id,
      "title": self.title,
      "content": self.content}

  def __repr__(self):
    return '<Report {}>'.format(self.username)