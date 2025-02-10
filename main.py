from datetime import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'  # wo die Datenbank liegt
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(200), nullable=True)
    content = db.Column(db.String(500), nullable=True)
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)

@app.route("/")
def start_page():
    return "<h1>Hello, World!</h1><a href='https://google.de'>Google</a>"

def create_db():
    """Erstellt die Datenbanktabellen innerhalb des App-Kontexts."""
    with app.app_context():
        db.create_all()
        print("Datenbanktabellen wurden erstellt.")

if __name__ == "__main__":
    create_db()  # Erstellt die Datenbanktabellen beim Start
    app.run(debug=True)
