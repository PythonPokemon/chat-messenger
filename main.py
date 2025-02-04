from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route("/")
def start_page():
    return "<h1>Hello, World!</h1><a href='https://google.de' >Google</a>"

if __name__ == "__main__":
    app.run(debug=True)
