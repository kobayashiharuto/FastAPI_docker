from flask import Flask, request, jsonify, make_response
app = Flask(__name__)


@app.route("/api/v1/iconimage", methods=['GET'])
def getHoge():
    # URLパラメータ
    params = request.args
    response = {}
    print(request.get_data())
    if 'param' in params:
        response.setdefault('res', 'param is : ' + params.get('param'))
    return make_response(jsonify(response))


if __name__ == "__main__":
    app.run(debug=True)
