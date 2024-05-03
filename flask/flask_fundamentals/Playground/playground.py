from flask import Flask, render_template  # added render_template!
app = Flask(__name__)                     
    
@app.route('/play')                           
def boxes():
    return render_template("index.html") 
@app.route('/play/<num>')
def display_boxes(num):
    return render_template("index1.html", element="h2", times=int(num))
@app.route('/play/<num>/<color>')
def coloR(num, color):

    return render_template ("index2.html", color=color, element = "h2", times=int(num))
if __name__=="__main__":
    app.run(debug=True)                   

