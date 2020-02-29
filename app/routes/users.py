from app import app, db
from app.models.user import User
from flask import request, jsonify
import time

@app.route('/users/authenticate', methods=['POST'])
def authenticate():
  if not request.json or not 'username' in request.json:
        abort(400)
  u = request.json
  user = User.query.filter_by(username=u['username']).first();
  if user is None:
    return jsonify({'status': False}), 401
  authenticated = user.check_password(u['password'])
  print(authenticated)
  if authenticated:
      u['token'] = time.time()
      u['role'] = user.role
  return jsonify(u), 200 if authenticated else 401


@app.route('/users/register', methods=['POST'])
def register():
  if not request.json or not 'username' in request.json:
      abort(400)
  u = request.json
  user = User(u['username'], u['password'], u['role'])
  db.session.add(user)
  db.session.commit()
  return jsonify({'user': user.serialize()}), 201
