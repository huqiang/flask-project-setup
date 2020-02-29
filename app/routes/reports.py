from app import app, db
from app.models.report import Report
from flask import request, jsonify
from flask_jwt_extended import jwt_required

import time

@app.route('/reports', methods=['POST'])
@jwt_required
def create():
  if not request.json or not 'title' in request.json:
    abort(400)
  r = request.json
  report = Report(r['title'], r['content'])
  db.session.add(report)
  db.session.commit()
  return jsonify({'report': report.serialize()}), 201

@app.route('/reports/<int:id>', methods=['PUT'])
@jwt_required
def update(id):
  if not request.json or not 'title' in request.json:
    abort(400)
  r = request.json
  report = Report.query.get(id)
  report.title = r['title']
  report.content = r['content']
  # db.session.add(report)
  db.session.commit()
  return jsonify({'report': report.serialize()}), 201

@app.route('/reports', methods=['GET'])
@jwt_required
def get_all_reports():
  return jsonify({'reports': list(map(lambda rpt: rpt.serialize(), Report.query.all()))})

@app.route('/reports/<int:id>', methods=['GET'])
@jwt_required
def get(id):
  print(id)
  return jsonify({'report': Report.query.get(id).serialize()})



