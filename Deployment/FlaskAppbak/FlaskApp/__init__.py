from flask import Flask,render_template,Response
import cv2
import time

time.sleep(2)

app = Flask(__name__) 

@app.route("/") 
def hello():
    return render_template("index.html") 

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
    #app.run()
