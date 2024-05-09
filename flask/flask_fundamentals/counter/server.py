from flask import Flask, render_template, session, redirect  # type: ignore # Import Flask to allow us to create our app
app = Flask(__name__)
app.secret_key ='keep it secret'               # Create a new instance of the Flask class called "app"
@app.route('/')
def count():
    if 'counter' not in session:
        session['counter'] = 0
    else:
        session['counter'] = session['counter'] +1
    return render_template('index.html', counter= session['counter'])
@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')
@app.route('/plus2', methods = ['POST'])
def count2():
    if 'counter' not in session:
        session['counter'] = 0
    else:
        session['counter'] = session['counter'] +1
    return redirect('/')

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True) 
