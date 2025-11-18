from flask import Flask,request,jsonify
app=Flask(__name__)
users={}
next_id=1
@app.route("/")
def home():
    return jsonify({"message":"User API is running"})
@app.route("/users",methods=['GET'])
def get_users():
    return jsonify(list(users.values())),200
@app.route("/users/<int:user_id>",methods=["GET"])
def get_user(user_id):
    user=users.get(user_id)
    if not user:
        return jsonify({"error":"User not found"}),404
    return jsonify(user),200
@app.route('/users',methods=['POST'])
def create_user():
    global next_id
    data=request.get_json()
    if not data:
        return jsonify({"error":"Request body must be JSON"}),400
    name=data.get("name")
    age=data.get("age")
    if not name or not age:
        return jsonify({"error":"Both 'name' and 'age' are required"}),400
    user={
        "id":next_id,"name":name,"age":age
    }
    users[next_id]=user
    next_id+=1
    return jsonify(user),201
@app.route('/users/<int:user_id>',methods=['PUT'])
def update_user(user_id):
    data=request.get_json()
    if not data:
        return jsonify({"error":"Request body must be JSON"}),400
    user=users.get(user_id)
    if not user:
        return jsonify({"error":"User not found"}),404
    user["name"]=data.get("name",user["name"])
    user["age"]=data.get("age",user["age"])
    return jsonify(user),200
@app.route('/users/<int:user_id>',methods=['DELETE'])
def delete_user(user_id):
    user=users.pop(user_id,None)
    if not user:
        return jsonify({"error":"User not found"}),404
    return jsonify({"message":"User not found"}),404

if __name__=="__main__":
    app.run(debug=True)
