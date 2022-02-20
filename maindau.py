from flask import Flask,render_template, request , redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime 

maindau = Flask(__name__)
maindau.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///TO DO.sqlite"
maindau.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(maindau)

class Todo(db.Model):
    no = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(45),nullable = False)
    des = db.Column(db.String(500),nullable = False)
    date4 = db.Column(db.DateTime, default = datetime.utcnow)


    def __repr__(self) -> str:
        return f"{self.no} - {self.title} - {self.des} - {self.date4}"
    

@maindau.route("/", methods= ['GET','POST'])
def hello_world():
    if request.method == "POST":
        title = request.form['title']
        des = request.form['des']
        todo = Todo(title = title ,des = des)
        db.session.add(todo)
        db.session.commit()
    
    alltodo = Todo.query.all()
    return render_template("home.html",alltodo = alltodo)


@maindau.route("/delete/<int:no>")
def delete(no):   
    todo = Todo.query.filter_by(no = no).first()
    # print(todo)
    db.session.delete(todo)
    db.session.commit()
    return redirect("/")       


@maindau.route("/update/<int:no>")
def update(no):
    todo = Todo.query.filter_by(no = no).first()   
    alltodo = Todo.query.all()
    print(alltodo)
    return render_template("update.html",alltodo = alltodo)

     
    
if __name__ == "__main__":
    maindau.run(debug=False)