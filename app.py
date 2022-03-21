import flask
from flask import render_template, request, jsonify, send_file, make_response
import requests as reqs
from gtts import gTTS
from search import search
from get_paper import get_paper
import arxiv
import pdfminer
from pdfminer.high_level import extract_text, extract_pages
from pdfminer.layout import LTTextContainer

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route("/", methods=['GET'])
def get_index():
    return render_template("index.html")


@app.route("/papers", methods=['GET', 'POST'])
def get_papers():
    query = request.form['query']
    print(query)
    lst = search(query)
    temp = ["paper1", "paper2", "paper3"]

    return render_template("second.html", qry=query, paperlst=lst)


@app.route("/paperselect", methods=['GET', 'POST'])
def get_details():
    global pname, pgs
    pname = request.form['papername']
    paper = get_paper(pname)
    tpages = len(list(extract_pages(paper.title+'.pdf')))
    print("total pages=", tpages)
    lmt = 10
    pgs = [i+1 for i in range(tpages)]
    return render_template("third.html", pname=pname, pgs=pgs, n1=1, n2=tpages, status=0)


@app.route("/audio", methods=['GET', 'POST'])
def download_audio():
    start = int(request.form['start'])
    end = int(request.form['end'])
    print(pname)
    print(pgs)
    print(start)
    print(end)
    return render_template("third.html", pname=pname, pgs=pgs, n1=start, n2=end, status=1)


if __name__ == '__main__':
    app.run()
