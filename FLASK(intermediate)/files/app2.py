from flask import Flask, request
app=Flask(__name__)

@app.get('/')
def simple_data():
    return "Home Page"

@app.get('/html_data')
def html_data():
    return "<h1>Hello</h1>"

@app.get('/json_data')
def json_data():
    return {"id":1,"name":"protap"}


users=[{"id":2,"name":"priyash","age":27},{"id":3,"name":"sujit","age":21}]
bca = [
    {"sem": 2, "papers":4, "programming":"C"},
    {"sem": 3, "papers":6, "programming":"C++"},
    {"sem": 4, "papers":7, "programming":"Java"},
    {"sem": 5, "papers":9, "programming":"JS"}
]

@app.get('/user')
def get_users():
    return users

@app.post('/user')
def add_users():
    users.append(request.json)
    return users

@app.patch('/user')
def update_username():
    for user in users:
        if user["id"]==request.json["id"]:
            user["name"]=request.json["name"]
            return user
    return "x",204

@app.put('/user')
def update_user():
    for user in users:
        if(user["id"]==request.json["id"]):
            user["name"]=request.json["name"]
            user["age"]=request.json["age"]
            return user
    return "x",204

@app.delete('/user')
def delete_users():
    for user in users:
        if user["id"]==request.json["id"]:
            users.remove(user)
            return "removed",200
    return "x",204

