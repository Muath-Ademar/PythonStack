from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def user():
    return render_template ("index.html", num = 4 , num2=4) 

@app.route("/<num>")
def user2(num):
    return render_template("index.html", num = int(num) ,num2=int(num))
@app.route("/<num>/<num2>")
def user3(num, num2):
    return render_template("index.html", num= int(num), num2 = int(num2))
@app.route("/<num>/<num2>/<color1>/<color2>")
def color(num, num2, color1, color2):
    return render_template("index.html", num= int(num), num2 = int(num2), color1 = color1, color2 = color2)

if __name__ =="__main__":
    app.run(debug=True)
