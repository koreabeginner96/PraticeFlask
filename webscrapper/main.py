from flask import Flask, render_template, request
from extractors.indeed  import extract_indeed_jobs
from extractors.wwr import extract_wwr_jobs

#app = Flask("이름")에서 이름 부분에 공백(space)이 있으면 안된다.
app = Flask("JobScrapper")
db={}

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/search")
def search():
    if keyword in db:
        jobs=db[keyword]
    else:
        keyword=request.args.get("keyword")
        indeed=extract_indeed_jobs(keyword)
        wwr=extract_wwr_jobs(keyword)
        jobs=indeed+wwr
        db[keyword] = jobs
    return render_template("search.html",keyword=keyword , jobs= jobs)

app.run("0.0.0.0")