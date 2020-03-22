from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html", subject="안녕하세요 반갑습니다.")


if __name__ == "__main__":
    host_addr = "127.0.0.1"
    portNumber = "4040"

    app.run(host=host_addr,port=portNumber)