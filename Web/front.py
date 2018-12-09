from flask import request, render_template
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Controllers import parityCheckWeb, hadamard
import flask


application = flask.Flask(__name__)
message = ""
res_a = ""
res_b = ""
res_c = ""
noise = 0.05

@application.route('/')
def serve():
    return flask.render_template("index.html", result="", noisy=noise, a="", b="")

@application.route('/index.html')
def returnHome():
    return flask.render_template("index.html", result="", noisy=noise, a="", b="")


@application.route('/submit', methods=['POST'])
def submit():
    message = request.form["message"]
    noise = float(request.form["noise"])/500.0
    print(message)
    print(parityCheckWeb.parityCheck(message,noise=noise))
    res_a = parityCheckWeb.parityCheck(message,noise=noise)
    res_b = hadamard.hadamardDecoding(message,probability=noise)
    return flask.render_template("index.html", result=message, noisy=noise*500, a=res_a, b=res_b)

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 33507))
    application.run(host='0.0.0.0',port=port)