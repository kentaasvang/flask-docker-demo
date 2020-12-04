from flask import Flask, render_template_string
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return render_template_string(f"<h1> The time is: {datetime.now()} </h1>")


if __name__ == "__main__": 
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
