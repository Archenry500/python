from flask import Flask, render_template,request, redirect, url_for      #we import flask from flask
from flask_sqlalchemy import SQLAlchemy       #this  is n Object relational maping model that enables the creation of database models in the form of classes

app = Flask(__name__)        #Instanciate /Creating an intance of the flask class

# Configure your flask object with SQLAlchemy
app.config['SECRET_KEY'] = 'abcd123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///form_database.db'
db = SQLAlchemy(app)

# Define a model to represent the data you want to store into the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    Quantity = db.Column(db.Integer, nullable=False)
    phone_num = db.Column(db.String(15), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    Address = db.Column(db.String(120), nullable=False)

@app.route('/')              #here we created the route/view function
def index():
    # return "Hello World!"
    return render_template('as1.html')

@app.route('/ass')              
def ass():
    return render_template('as2.html')

@app.route('/ab', methods=['GET', 'POST'])              
def ab():
    if request.method == 'POST':
        name = request.form['name']
        Quantity = request.form['quantity']
        phone_num = request.form['phonenumber']
        email = request.form['email']
        Address = request.form['delivery_add']



        user = User(name=name, Quantity=Quantity, phone_num=phone_num, email=email, Address=Address)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('ab'))
    return render_template('myform.html')

if __name__ == '__main__':    # here __main__ is the w
    with app.app_context():
        db.create_all()
    app.run(debug=True)

