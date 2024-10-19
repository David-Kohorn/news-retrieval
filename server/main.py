from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, origins="*")

@app.route("/", methods=["GET"])
def fun():
    return jsonify(
        {
            "names": ["kevin", "sally", "bart"]
        }
    )

if __name__ == "__main__":
    app.run(debug=True, port=8080)

