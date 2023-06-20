from flask import Flask, jsonify, render_template
import socket


def getServerData():
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    return str(host_name), str(host_ip)


app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello World!</p>"


@app.route("/health")
def health():
    return jsonify(status="UP")


@app.route("/details")
def details():
    host_name, host_ip = getServerData()
    return render_template("index.html", hostname=host_name, hostip=host_ip)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
