from flask import Flask, request, jsonify
from app.services import Services


def create_app():
    app = Flask(__name__)
    services = Services()

    @app.route("/hello", methods=["GET"])
    def hello():
        return "Hello World!"

    @app.route("/get_data", methods=["GET"])
    def get_data():
        return jsonify(services.k_dict)

    @app.route("/post_data", methods=['POST'])
    def post_data():
        response = request.get_json()
        services.k_dict.append(response)
        return jsonify({"msg": "success", "data": services.k_dict})

    return app

if __name__ == "__main__":
    myapp = create_app()
    myapp.run()








