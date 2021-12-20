from flask import Flask

# Flask 객체 생성
app = Flask(__name__)

# 0.0.0.0:5000/
@app.route("/")
def hello():
    return '''
    <p>Hello, Flask!!</p>
    <a href = "/first">Go first </a>
    <a href = "/second">Go second </a>
    '''
@app.route("/first")
def first():
    return '''
    <p>Fisrst Page</p>
    <a herf="/">Go home</a>'''

@app.route("/second")
def second():
    return '''
    <p>second Page</p>
    <a herf="/">Go home</a>'''
# 터미널에서 직접 실행시킨 경우
if __name__ == "__main__":
    app.run(host = "0.0.0.0")