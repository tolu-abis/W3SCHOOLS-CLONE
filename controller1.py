from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def welcome():
    return render_template("index.html")

@app.route("/courses/html")
def html():
    return render_template("HTML.html")

@app.route("/courses/css")
def css():
    return render_template("CSS.html")

if __name__ == "__name__":
    app.run(debug=True)
