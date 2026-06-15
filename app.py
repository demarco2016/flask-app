from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>🚀 Flask App by demarco2016</h1><p>Web3 Builder | Arc Ecosystem | Base Chain</p>"

if __name__ == "__main__":
    app.run(debug=True)
