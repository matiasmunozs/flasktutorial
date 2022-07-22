from flask import Flask
from flask import jsonify
from flask import request
from flask import json
app = Flask(__name__)


todos = [{ "label": "My first task", "done": False }]


# # @app.route('/todos', methods=['GET'])
# # def hello_world():
# #     return "<h1>Hello!</h1>"

@app.route('/todos', methods=['GET'])
def returning_json():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    print("Incoming request with the following body", request_body)
    decoded_object = json.loads(request_body)
    todos.append(decoded_object)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ",position)
    todos.pop(position)
    return jsonify(todos)



# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)





