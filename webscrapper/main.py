from flask import Flask
#app = Flask("이름")에서 이름 부분에 공백(space)이 있으면 안된다.
app = Flask("JobScrapper")

#@app.route("/") = decorator / @가 있는 코드위에 함수를 위치 시켜야 한다.
#func와 붙어 놓으면 flask는 주소(route 괄호 안)의 page 방문했을 때 아래 함수를 호출 시켜야하는 걸 안다.
@app.route("/")
def home():
    return 'hey there!'

app.run("0.0.0.0")