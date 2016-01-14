import socket
from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello():
    _ip = socket.gethostbyname(socket.gethostname())
    _version = '1.2'
    return 'ip: {0}\nversion: {1}'.format(_ip, _version)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
