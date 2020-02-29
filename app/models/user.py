import bcrypt
from datetime import datetime
from app import db

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(80), unique=True, nullable=False)
  password = db.Column(db.String(80), unique=True, nullable=False)
  role = db.Column(db.String(80), unique=True, nullable=False)

  def insertUser(user):
    con = sql.connect("db/db.db")
    cur = con.cursor()
    hashpw = get_hashed_password(user['password'])
    cur.execute("INSERT INTO users (username,password, role) VALUES (?,?,?)", \
      (user['username'],\
        hashpw,\
          user['role']))
    con.commit()
    con.close()

  def retrieveUsers():
    con = sql.connect("db/db.db")
    cur = con.cursor()
    cur.execute("SELECT username, password, role FROM users")
    users = cur.fetchall()
    con.close()
    return users

  def login(user):
    con = sql.connect("db/db.db")
    cur = con.cursor()
    cur.execute("SELECT username, password, role FROM users where username=?",(user['username'],))
    u = cur.fetchone()
    con.close()
    if check_password(user['password'], u[1]):
      user['role'] = u[2]
      return True
    return False

  def get_hashed_password(plain_text_password):
    # Hash a password for the first time
    #   (Using bcrypt, the salt is saved into the hash itself)
    return bcrypt.hashpw(plain_text_password, bcrypt.gensalt())

  def check_password(plain_text_password, hashed_password):
    # Check hashed password. Using bcrypt, the salt is saved into the hash itself
    return bcrypt.checkpw(plain_text_password, hashed_password)

  def serialize(self):
    return {"id": self.id,
      "username": self.username,
      "role": self.role}

  def __repr__(self):
    return '<User {}>'.format(self.username)