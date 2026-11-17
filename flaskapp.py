from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Flsk web app begins"

if __name__ == "__main__":
    app.run(debug=True)