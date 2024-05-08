from flask import Flask, render_template,request,redirect, session
app = Flask(__name__)
app.secret_key = 'Ola'
@app.route("/")
def survey():
    return render_template("index.html")

@app.route('/result', methods=['POST'])
def survey1():
    name = request.form['username']
    location = request.form['location']
    language = request.form['language']
    comment = request.form['comment']
    yes_no= request.form ['Op']
    check = request.form.getlist('check[]')
    if len(check) > 1:
        check_st = ', '.join(check[:-1]) + ', and ' + check[-1]
    elif len(check) == 0:
        check_st=''
    else:
        check_st = check[0]

    return render_template("show.html", name =name, location=location, language=language,comment = comment, opt = yes_no, ch = check_st)

@app.route('/login', methods=['POST'])
def survey2():

    return render_template("index.html" )

if __name__ == "__main__":
    app.run(debug = True) 
