from flask import Flask, render_template 
#app = Flask("이름")에서 이름 부분에 공백(space)이 있으면 안된다.
app = Flask("JobScrapper")

@app.route("/")
def home():
    return render_template("home.html",name="nico")

app.run("0.0.0.0")