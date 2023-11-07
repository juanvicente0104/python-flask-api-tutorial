from flask import Flask, jsonify, request
app = Flask(__name__)

todos = [{"label": "My first task", "done":False}]

@app.route('/todos',methods=['GET'])
def hello_world():
    # convert the data into a json string
    json_todos = jsonify(todos)
    return json_todos

# @app.route('/todos',methods=['POST'])
# def add_new_todo():
#     request_body = request.data
#     print("Incoming request with the following body", request_body)
#     return jsonify('Response for the POST todo')

@app.route('/todos',methods=['POST'])
def add_new_todo():
      request_body = request.get_json()
      #print(request_body)
      todos.append(request_body)
      #print(todos)
      return jsonify(todos)

@app.route('/todos/<int:position>',methods=['DELETE'])
def delete_todo(position):
     todos.pop(position)
     return jsonify(todos)

#This goes at the end of the document
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=3245,debug=True)