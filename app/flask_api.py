from flask import Flask, render_template, request, jsonify
from flask_restful import Api, Resource, reqparse
from flask_cors import CORS, cross_origin
from logging.config import dictConfig
from services import Services
'''
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

#k_dict = Services('단일화', 'korean').k_dict
j_dict = Services('天守', 'japanese').j_dict

@app.route('/')
def doc() -> str:
    app.logger.info("doc - Got request")
    with open("app/doc.html", "r") as f:
        return f.read()


@app.route("/generate", methods=["GET"])
def get_words():
    services.generate_words()
    app.logger.info("/get_word - Get word info")
    return jsonify({"msg": "success"})


'''
app = Flask(__name__)

api = Api(app)

j_dict = Services().j_dict

word_args = reqparse.RequestParser()
word_args.add_argument("word", type=str, help="Japanese Word", required=True)
word_args.add_argument("korean", type=str, help="Korean", required=False)
word_args.add_argument("english", type=str, help="English", required=False)
word_args.add_argument("pos", type=str, help="POS", required=False)

class FlaskApi(Resource):
    def get(self, name):
        for i in j_dict:
            if i['word'] == name:
                return i

    def put(self, name):
        args = word_args.parse_args()
        print(args)
        j_dict[name] = args
        print(j_dict[name])
        return j_dict[name], 201

api.add_resource(FlaskApi, "/word/<string:name>")
'''
#app = Flask(__name__)

@app.route("/")
def index():
    return render_template('project.html')

@app.route("/post_data/", methods=['POST'])
def post_data():
    word = request.form.get("word")
    for i in j_dict:
        if i['word'] == word:
            return i
    return render_template("project.html")

'''
if __name__ == "__main__":
    app.run(debug=True)
