from flask.cli import FlaskGroup
from api import app,db

cli=FlaskGroup(app)
@app.cli.command("create_db")
def create_db():
    with app.app_context():
        db.create_all()
        print('db created')