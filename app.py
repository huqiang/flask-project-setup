
from app import app, db
from app.models.user import User
from app.models.report import Report


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Report': Report}
