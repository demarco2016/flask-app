from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, render_template
from routes.invoices import invoices_bp 

app = Flask(__name__)

app.register_blueprint(invoices_bp) 

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)    
