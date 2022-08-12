from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from logging.config import dictConfig
from flask_restful import Api, Resource
from app.services import Services

dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app, resources={r"/parse": {"origins": "http://localhost:port"}})

services = Services()

@app.route('/')
def doc() -> str:
    app.logger.info("doc - Got request")
    with open("web/project.html", "r") as f:
        return f.read()

@app.route("/get", methods=["GET"])
def get_data():
    repo = services.repo
    app.logger.info("/get - Generated words.")
    return jsonify({'msg': "success"})

# This is to be called with Postman
@app.route("/post/<string:word>", methods=['POST'])
def post_word(word):
    for i in services.k_dict:
        if i['word'] == word:
            return i

    for i in services.j_dict:
        if i['word'] == word:
            return i

# This is to be used with project.html - requires user input and return
# the word, tfidf, japanese, english and pos for the korean word input.
@app.route("/post_data", methods=['POST'])
def post_data():
    word = request.form.get("word")
    language = request.form.get('language')
    if language == 'korean':
        for i in services.k_dict:
            if i['word'] == word:
                return i
    if language == 'japanese':
        for i in services.j_dict:
            if i['word'] == word:
                return i

    return render_template("web/project.html")

'''
#This is the code for pytest test file "api_test.py", which doesn't work on 
#automated pytest on github.

api = Api(app)

class FlaskApi(Resource):
    def get(self, name):
        for i in services.j_dict:
            if i['word'] == name:
                return i

api.add_resource(FlaskApi, "/word/<string:name>")
'''
if __name__ == "__main__":
    app.run(host='0.0.0.0')








