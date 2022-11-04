from flask import Flask, request, abort, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)
@app.route('/', methods=['GET'])
def something():
    return "vibes"
@app.route('/api/v1', methods=['POST'])
def calculatorApi():
    body = request.get_json()

    operation_types = body['operation_type']
    op_types = operation_types.split()
    for op in op_types:
        if op == "addition" or op == "add" or op == "plus" or op == "sum":
            operation_type = "addition"
        elif op == "subtraction" or op == "minus" or op == "subtract" or op == "difference":
            operation_type = "subtraction"
        elif op == "multiplication" or op == "times" or op == "multiply" or op == "product":
            operation_type = "multiplication"
    x = body['x']
    y = body['y']

    try:
        if operation_type != None and x != None and y != None:
            operation_type = operation_type.lower().strip()
            if (operation_type == "addition" or operation_type == "subtraction" or operation_type == "multiplication"):
                if operation_type == "addition":
                    result = x + y
                elif operation_type == "subtraction":
                    result = x - y
                elif operation_type == "multiplication":
                    result = x * y
            else:
                abort(400)
        else:
            abort(400)
    except Exception as e:
        return e
    
    return jsonify({
            'slackUsername': 'Uncle-Solomon',
            'result': result,
        })

if __name__=='__main__':
    app.run(debug=True)
