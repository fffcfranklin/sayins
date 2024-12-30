from flask import Flask, render_template

app = Flask(__name__)


#create a route decorator
@app.route('/')
def index():
    sayinList = ["image", "audio", "Sayin", "Explanation"]
    sayin_text = "whoop tee doo"
    sayin_explanation = "i dont really get it"
    return render_template("index.html", 
        sayin_text = sayin_text,
        sayin_explanation = sayin_explanation,
        sayinList = sayinList)

#route page by sayin_title
#http://127.0.0.1:5000/
@app.route('/sayin/<sayin_title>')
def sayin(sayin_title):
    return render_template("sayin.html", sayin_title = sayin_title)