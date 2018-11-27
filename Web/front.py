
import flask

application = flask.Flask(__name__)

@application.route('/')
def serve():
    return flask.render_template("index.html")

@application.route('/index.html')
def returnHome():
    return flask.render_template("index.html")

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 33507))
    application.run(host='0.0.0.0',port=port)