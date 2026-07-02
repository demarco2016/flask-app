from flask import Flask, render_template
from routes.invoices import invoices_bp

app = Flask(__name__)

# register API routes
app.register_blueprint(invoices_bp)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
