import flask
from flask import render_template, request, jsonify, send_file, make_response
import requests as reqs
from gtts import gTTS

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route("/", methods=['GET'])
def get_index():
    return render_template("index.html", flag=0)


@app.route("/papers", methods=['GET', 'POST'])
def get_papers():
    query = request.form['query']
    print(query)
    temp = ["paper1", "paper2", "paper3"]
    return render_template("index.html", qry=query, lst=temp, flag=1)


if __name__ == '__main__':
    app.run()
