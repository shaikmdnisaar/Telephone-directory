from flask import Flask, render_template, request

app = Flask(__name__)

global database

database={}

@app.route("/",methods=['POST','GET'])
def index():
	return render_template("index.html")

@app.route("/display",methods=['POST','GET'])
def display():
	Name = request.form.get('Name')
	MobileNo = request.form.get('MobileNo')
	database[Name]=MobileNo
	return render_template("display.html",Name = Name,  MobileNo=MobileNo, database= database)

@app.route("/add",methods=['GET','POST'])
def add():
    Name = request.form.get('Name')
    MobileNo = request.form.get('MobileNo')
    database[Name]=MobileNo
    return render_template("add.html", Name = Name, MobileNo=MobileNo, database= database)

@app.route("/search",methods=['GET','POST'])
def search():
	Search_Name=request.form.get('Name')
	return render_template("search.html",Search_Name=Search_Name, database=database)

if __name__ == '__main__':
	app.run(debug=True)