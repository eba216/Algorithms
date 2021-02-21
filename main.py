from flask import Flask, render_template, url_for, request
from Strings import Strings

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
@app.route('/index', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        string = request.args.get("string","")
        alg = request.args.get("alg", "")
        print(string)
        print(alg)
        Str = Strings(string=string, alg=alg)

        return Str.do_alg()

    return "Could not process"


if __name__ == '__main__':
    app.run(debug=True)