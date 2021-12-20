from flask import Flask, render_template

# Flask 객체 생성
app = Flask(__name__)

# 0.0.0.0:5000/
@app.route("/")
def hello():
    return render_template("hello.html")
@app.route("/first")
def first():
    return render_template("first.html",
    title = "H2, Flask!!")

@app.route("/second")
def second():
    return render_template("second.html",
    title = "hi falsk")
# 터미널에서 직접 실행시킨 경우
if __name__ == "__main__":
    app.run(host = "0.0.0.0")