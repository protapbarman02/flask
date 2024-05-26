from flask import Flask, request

app = Flask(__name__)

bca = [
    {"sem": 2, "papers": 4, "programming": "C"},
    {"sem": 3, "papers": 6, "programming": "C++"},
    {"sem": 4, "papers": 7, "programming": "Java"},
    {"sem": 5, "papers": 9, "programming": "JS"}
]

@app.get('/')
def simple_data():
    return "Home Ppapers"

@app.get('/html_data')
def html_data():
    return "<h1>Hello</h1>"

@app.get('/json_data')
def json_data():
    return {"sem": 1, "programming": "protap"}

@app.get('/bca')
def get_bca():
    return bca

@app.post('/bca')
def add_bca():
    bca.append(request.json)
    return bca

@app.patch('/bca')
def update_programming():
    for semester in bca:
        if semester["sem"]==request.json["sem"]:
            semester["programming"]=request.json["programming"]
            return semester
    return "x",204

@app.put('/bca')
def update_semester():
    for semester in bca:
        if(semester["sem"]==request.json["sem"]):
            semester["programming"]=request.json["programming"]
            semester["papers"]=request.json["papers"]
            return semester
    return "x",204

@app.delete('/bca')
def delete_semester():
    for semester in bca:
        if semester["sem"]==request.json["sem"]:
            bca.remove(semester)
            return "removed",200
    return "x",204

FLASK_APP=app
FLASK_DEBUG=1