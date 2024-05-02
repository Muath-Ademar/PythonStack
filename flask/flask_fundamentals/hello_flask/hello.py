from flask import Flask  # type: ignore # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!' 
@app.route('/dojo')          # The "@" decorator associates this route with the function immediately following
def dojo():
    return 'dojo' 
@app.route('/say/<name>')          # The "@" decorator associates this route with the function immediately following
def flsk(name):
    return "hi "+name 

@app.route('/repeat/<num>/<name>')          # The "@" decorator associates this route with the function immediately following
def number(num,name):
    return int(num)*name
@app.route('/<path:path>')
def catch_all(path):
    return "Sorry! No response. Try again."
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
