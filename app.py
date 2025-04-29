from flask import Flask

app = Flask(__name__)


app.route('/')
def home():
    return "Hello developer! This template kickstarts Flask + CI/CD."

if __name__ == '__main__':
    app.run(debug=True)