from flask import Flask,redirect,render_template, request, session

from movie_engine import search as msearch

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search",methods=["GET","POST"])
def search():
    if request.method == "GET":
        query = request.args.get("search")
        print(query)
        res = msearch(query)
        print(res[["movieId","title"]].to_json(orient="records"))
        return res
    
    return render_template("index.html")