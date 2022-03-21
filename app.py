import flask
from flask import render_template, request, jsonify, send_file, make_response
import requests as reqs
from gtts import gTTS

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route("/", methods=['GET'])
def get_index():
    return render_template("index.html")


@app.route("/papers", methods=['GET', 'POST'])
def get_papers():
    query = request.form['query']
    print(query)
    temp = ["paper1", "paper2", "paper3"]

    return render_template("second.html", qry=query, paperlst=temp)


@app.route("/paperselect", methods=['GET', 'POST'])
def get_details():
    pname = request.form['papername']
    lmt = 10
    pgs = [i+1 for i in range(lmt)]
    return render_template("third.html", pname=pname, pgs=pgs)


@app.route("/audio", methods=['GET', 'POST'])
def download_audio():
    start = request.form['start']
    end = request.form['end']
    print(start)
    print(end)


if __name__ == '__main__':
    app.run()
