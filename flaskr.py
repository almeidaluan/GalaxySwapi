from flask import Flask

# creates main app for Gunicorn
app = Flask(__name__)

if __name__ == "__main__":
    app.run()