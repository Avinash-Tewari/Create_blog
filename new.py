from flask import Flask,render_template
app = Flask(__name__)

@app.route("/index1")
def row():
        return render_template("index1.html")

@app.route("/abt1")
def rex():
        return render_template('abt.html',)


@app.route("/bootstrap")
def avi():
        
        return render_template('bootstrap1.html')

app.run(debug=True) 