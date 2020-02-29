from app import app
from app.models.report import Report
from flask import request, jsonify
import time

@app.route('/reports', methods=['POST'])
def create():
  if not request.json or not 'title' in request.json:
    abort(400)
  r = request.json
  report = Report(r['title'], t['content'])
  db.session.add(report)
  db.session.commit()
  return jsonify({'report': report.serialize()}), 201

@app.route('/reports', methods=['GET'])
def get_all_reports():
  return jsonify({'reports': list(map(lambda rpt: rpt.serialize(), Report.query.all()))})

@app.route('/reports/<int:id>', methods=['GET'])
def get(id):
  print(id)
  return jsonify({'report': Report.query.get(id).serialize()})



