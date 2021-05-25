from flask import Flask, request, jsonify, make_response
import json
app = Flask(__name__)


@app.route("/api/v1/iconimage", methods=['GET'])
def getData():
    # URLパラメータ
    params = request.args
    response = {}
    if 'param' in params:
        print(params.get('param'))
        response.setdefault('res', 'param is : ' + params.get('param'))
    return make_response(jsonify(response))


@app.route("/api/v1/iconimage", methods=['POST'])
def postData():
    json_dict = request.get_json()
    print(json_dict["image"])


if __name__ == "__main__":
    app.run(debug=True)
