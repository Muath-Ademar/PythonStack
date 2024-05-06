from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def user():
    return render_template ("index.html", num = 4) 

@app.route("/<num>")
def user2(num):
    return render_template("index.html", num = int(num))
if __name__ =="__main__":
    app.run(debug=True)