from flask import Flask
app = Flask(__name__)

@app.route('/')
def greeting():
    return "This is Test API !"


@app.route('/add', methods=['POST'])
def get_add():
    if request.method == 'POST':
        a = request.json["a"]
        b = request.json["b"]
        c = add(a, b)
        result = json.dumps(c)
    return result, status.HTTP_200_OK, {"Content-Type": "application/json; charset=utf-8", "Acess-Control-Allow-Origin": "*"}

@app.route('/same', methods=['POST'])
def get_same():
    if request.method == 'POST':
        a = request.json["a"]
        b = request.json["b"]
        c = same(a,b)
        result = json.dumps(c)
    return result, status.HTTP_200_OK, {"Content-Type": "application/json; charset=utf-8", "Access-Control-Allow-Origin": "*"}

set FLASK_APP=app.py
flask run --host=0.0.0.0
