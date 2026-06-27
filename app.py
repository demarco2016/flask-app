from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
    return """
<!DOCTYPE html>
<html>
<head>
    <meta name="base:app_id" content="6a0b13de7abfff0aca7b175a" />
</head>
<body>
    <h1>🚀 Flask App by demarco2016</h1>
    <p>Web3 Builder | Arc Ecosystem | Base Chain</p>
</body>
</html>
"""
if __name__ == "__main__":
    app.run(debug=True)
