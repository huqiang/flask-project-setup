from app import app
from app.models.user import User
from flask import request, jsonify
import time

@app.route('/users/authenticate', methods=['POST'])
def authenticate():
    u = request.json
    print(hash(u['password']))
    authenticated = user.login(u)
    print(authenticated)
    if authenticated:
        u['token'] = time.time()
    return jsonify(u)


@app.route('/users/register', methods=['POST'])
def register():
    u = request.json
    authenticated = user.insertUser(u)
    if authenticated:
        u['token'] = time.time()
    return jsonify(authenticated)
