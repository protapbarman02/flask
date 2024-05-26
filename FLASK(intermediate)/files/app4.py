from flask import Flask, request
import mysql.connector

app = Flask(__name__)

connection = mysql.connector.connect(host="localhost",user="root",password="")
cursor=connection.cursor()

# used to view student after post/patch/put
# used id in post req, as we can last insert id easily after insert query
# used email in case of update query
def global_get_student_by_id(id=None,email=None):
    if id is not None:
        cursor.execute(f"select name,email,age from students where s_id={id} and status=1")
    if email is not None:
        cursor.execute(f"select name,email,age from students where email='{email}' and status=1")
    rows = cursor.fetchall()    
    students = [{"name": row[0], "email": row[1], "age": row[2]} for row in rows]
    return students

# used to check student if present or not before post/patch/put/delete
def global_check_student_present(email):
    cursor.execute(f"select name from students where email='{email}' and status=1")
    row = cursor.fetchone()
    if row:
        return 1    #already exist
    else:
        return 0    #does not exist


# please test this first
# database initialization endpoint
@app.get('/')
def db_check():
    cursor.execute("show databases")
    dbs=cursor.fetchall()
    for db in dbs:
        if "py_students" == db[0]:
            cursor.execute("use `py_students`")
            return "database working" 
    cursor.execute("create database `py_students`")
    cursor.execute("use `py_students`")
    cursor.execute("create table `students` (`s_id` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,`name` varchar(128) DEFAULT NULL,`email` varchar(128) DEFAULT NULL,`age` int(3) DEFAULT NULL,`status` int(1) NOT NULL)")
    return "database setup complete"

# view all students
@app.get('/students')
def view_students():
    cursor.execute("select name,email,age from students where status=1")
    rows = cursor.fetchall()
    if not rows:
        return "empty"
    else:
        students = [{"name": row[0], "email": row[1], "age": row[2]} for row in rows]
        return students

# add single student per req
@app.post('/students')
def add_student():
    name=request.json["name"]
    age=request.json["age"]
    email=request.json["email"]
    if not global_check_student_present(email):
        cursor.execute(f"insert into students(`name`,`age`,`email`,`status`) values('{name}',{age},'{email}',1)")
        connection.commit()     # not working without commit
        # here we view the student added based on last insert id
        return global_get_student_by_id(id=cursor.lastrowid)
    return "student is already present, can't add"


# update student name
@app.patch('/students')
def update_student_name():
    email=request.json["email"]
    name=request.json["name"]
    if global_check_student_present(email):
        cursor.execute(f"update students set `name`='{name}' where `email`='{email}' and status=1")
        connection.commit()
        return global_get_student_by_id(email=email)
    return "student does not exist"

#update student name,age
@app.put('/students')
def update_student():
    email=request.json["email"]
    name=request.json["name"]
    age=request.json["age"]
    if global_check_student_present(email):
        cursor.execute(f"update students set `name`='{name}', `age`={age} where `email`='{email}' and status=1")
        connection.commit()
        return global_get_student_by_id(email=email)
    return "student does not exist"

# delete student(set as status 0)
@app.delete('/students')
def delete_student():
    email=request.json["email"]
    if global_check_student_present(email):
        cursor.execute(f"update students set `status`=0 where `email`='{email}'")
        connection.commit()
        return f"student : {email} is deleted'"
    return "student does not exist"

# closing the connection
@app.get('/close')
def close():
    cursor.close()
    connection.close()
    return "cursor and connection is closed. you have to restart flask to use again"
