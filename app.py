from flask import Flask,redirect,render_template, request, session, make_response

from movie_engine import search as msearch
from movie_engine import find_similar_movies as findsim

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
        qid = int(request.form.get('movieId'))
        rec = findsim(qid)
        rec = rec[["title","genres"]].to_dict('records')
        print(rec)
        return render_template("recommend.html",rec=rec)

      
    
    return render_template("recommend.html")