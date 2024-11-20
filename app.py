from flask import Flask,redirect,render_template, request, session, make_response

from movie_engine import search as msearch
from movie_engine import find_similar_movies as findsim
from movie_engine import top_hundred
from movie_engine import suggest

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search",methods=["GET","POST"])
def search():
    if request.method == "POST":
        query = request.get_json()
        res = msearch(query)
        res = res[["movieId","title"]].to_json(orient="records")
        res = make_response(res,200)
        return res
      
    
    return render_template("index.html")

@app.route("/recommend",methods=["GET","POST"]) 
def recommend():
    if request.method == "POST":
        qid = request.form.get('movieId')
        if not qid:
            return render_template("sorry.html")
        qid = int(qid)
        rec = findsim(qid)
        if rec.empty:
            return render_template("sorry.html")
        rec = rec.iloc[range(1,11)]
        rec = rec[["title","genres"]].to_dict('records')
        return render_template("recommend.html",rec=rec)

    return render_template("recommend.html")

@app.route("/top")
def top():
    toph = top_hundred()
    toph = toph.to_dict('records')
    return render_template("top.html",toph=toph)

@app.route("/suggest")
def sug_mov():
    sug = suggest()
    sug = sug.to_dict('records')
    return render_template("suggest.html",sug=sug)