from flask import request, render_template
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Controllers import parityCheckWeb
import flask


application = flask.Flask(__name__)
message = ""
res_a = ""

@application.route('/')
def serve():
    return flask.render_template("index.html", result="", a="")

@application.route('/index.html')
def returnHome():
    return flask.render_template("index.html", result="", a="")


@application.route('/submit', methods=['POST'])
def submit():
    message = request.form["message"]
    print(message)
    print(parityCheckWeb.parityCheck(message))
    res_a = parityCheckWeb.parityCheck(message)
    return flask.render_template("index.html", result=message, a=res_a)

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 33507))
    application.run(host='0.0.0.0',port=port)