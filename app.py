"""This flask app prints Hello from GitHub Actions!"""
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    """Function printing Hello from GitHub Actions!"""
    return "Hello from GitHub Actions!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
