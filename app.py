from flask import Flask,redirect,render_template, request, session, make_response

from movie_engine import search as msearch

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
        print(res)
        res = make_response(res,200)
        return res
      
    
    return render_template("index.html")