from app import app
from app.models.report import Report
from flask import request, jsonify
import time

@app.route('/reports', methods=['GET'])
def get_all_reports():
  return jsonify({'reports': list(map(lambda rpt: rpt.serialize(), Report.query.all()))})


