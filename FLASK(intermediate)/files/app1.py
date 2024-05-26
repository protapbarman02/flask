# from flask import Flask, request
# # app = Flask(__name__)
 
# # @app.route("/")
# # def hello_world():
# #     return "<p>Hello, World!</p>"


# @app.get("/")
# def get_data():
#     return "This is a simple app"


# @app.get("/simple-html-response")
# def get_html_data():
#     return "<b style='color:red;'>This is a simple app</b>"


# @app.get("/simple-json-response")
# def get_json_data():
#     return 


# users = [{"id": 1, "name": "Protap", "age": 24}, {"id": 2, "name": "Sujit", "age": 21}]


# @app.get("/user")
# def get_user():
#     return users


# @app.post("/user")
# def create_user():
#     users.append(request.json)
#     return users, 201


# @app.patch("/user")
# def update_user_name():
#     for user in users:
#         if request.json["id"] == user["id"]:
#             user["name"] = request.json["name"]
#             return user["id"]
#     return "user not found", 204


# @app.put("/user")
# def update_user():
#     return "entry updated", 201


# @app.delete("/user")
# def delete_user():
#     return "entry deleted", 201



# # if __name__ == '__main__':  
# #    app.run()