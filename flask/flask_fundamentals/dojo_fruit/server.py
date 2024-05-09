from flask import Flask, render_template, request, redirect
app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    id = request.form['student_id']
    quan = request.form['apple']
    quan2 = request.form['strawberry']
    quan3 = request.form['raspberry']
    count =int(quan) + int(quan2) + int(quan3) 
    print(request.form)
    print(f" charging{first_name}{last_name} for {count}")
    return render_template("checkout.html",first_name = first_name, last_name = last_name, id = id, quan = quan, quan3 =quan3, quan2= quan2, count =count)

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    


    # it sends the date that the user have enterd again which in a webapp like this would charge users every time they refresh the page 