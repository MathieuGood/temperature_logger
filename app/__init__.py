from flask import Flask

app = Flask(__name__)

from main import app


if __name__ == "__main__":
    app.run(debug=True)
