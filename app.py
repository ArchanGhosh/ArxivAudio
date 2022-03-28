from importlib.resources import contents
import flask
from flask import render_template, request, jsonify, send_file, make_response
import requests as reqs
from gtts import gTTS
import arxiv
import pdfminer
from pdfminer.high_level import extract_text, extract_pages
from pdfminer.layout import LTTextContainer
from modules.search import search
from modules.get_paper import get_paper
from modules.get_pages import get_pages
from modules.text_to_speech import text_to_speech

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route("/", methods=['GET'])
def get_index():
    return render_template("index.html")


@app.route("/papers", methods=['GET', 'POST'])
def get_papers():
    query = request.form['query']
    print(query)
    sort_by = str(request.form['sort_by'])
    order_by = str(request.form['order_by'])
    print(sort_by, order_by)
    lst = search(query=query, sort_by=sort_by, sort_order=order_by)
    # temp = ["paper1", "paper2", "paper3"]
    if len(lst) != 0:
        qry = "Papers for " + query
    else:
        qry = "No paper found for " + query

    return render_template("paperslist.html", qry=qry, paperlst=lst)


@app.route("/paperselect", methods=['GET', 'POST'])
def get_details():
    global pname, name, pgs
    pname = request.form['papername']
    print(pname)
    # delete previous paper here

    paper = get_paper(pname)
    print(paper)

    name = paper.title+'.pdf'
    name = name.replace('?', '')
    name = "downloads/" + name

    tpages = len(list(extract_pages(name)))
    print("total pages=", tpages)
    pgs = [i+1 for i in range(tpages)]

    return render_template("paperdetails.html", pname=pname, pgs=pgs, n1=1, n2=tpages, status=0)


@app.route("/audio", methods=['GET', 'POST'])
def download_audio():
    start = int(request.form['start'])
    end = int(request.form['end'])
    print("----name: ", name)
    # print(pgs)
    print(start)
    print(end)
    if start <= end:
        content = get_pages(name, start, end)
        print(content[:500])
        # delete previous audio here
        audio_loc = text_to_speech(name, content)
        # content = "xyz"
        msg = "Audio downloaded ✓"
        flag = 1
        return render_template("paperdetails.html", pname=pname, pgs=pgs, n1=start, n2=end, msg=msg, status=flag)
    else:
        msg = "Enter valid start and end page."
        flag = 2
        return render_template("paperdetails.html", pname=pname, pgs=pgs, n1=start, n2=end, msg=msg, status=flag)


@app.route("/download", methods=['GET', 'POST'])
def save():
    path = name + ".mp3"
    # path = "sample.mp3"
    return send_file(path, as_attachment=True)


if __name__ == '__main__':
    app.run()
