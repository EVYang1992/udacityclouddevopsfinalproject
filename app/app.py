# This application aims to create a static website for udacity cloud devops nanodegree
# Author : Devin Yang
# Revision: v0.0.1
# Date: 2020.02.23

from flask import Flask, render_template
 
app = Flask(__name__)
 
@app.route('/')
def hello_world():
    return render_template("index.html")
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)