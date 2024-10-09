import os
from flask import Flask, render_template, request, render_template_string
from flask_sqlalchemy import SQLAlchemy
from logic import data
import re
from tabulate import tabulate

app = Flask(__name__)

database_url = os.environ.get('DATABASE_URL', 'sqlite:///default.db')

if not database_url:
    raise RuntimeError("DATABASE_URL environment variable is not set.")

app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    income = db.Column(db.Float, nullable=False)
    
def dict_to_html_table(data):
    headers = data.keys()
    rows = [list(data.values())]
    table_html = tabulate(rows, headers, tablefmt='html')
    return table_html

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_input', methods=['POST'])
def process_input():
    user_input = request.form.get('user_input')
    email_pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if re.match(email_pattern, user_input):
        a = render_template('Details.html')
        return a
    else:
        a = render_template('index.html')
        return a
    return 0

@app.route('/logic', methods=['POST'])
def logic():
    try:
        name = request.form.get('name')
        age = int(request.form.get('age'))
        income = float(request.form.get('income'))

        print(f"Received - Name: {name}, Age: {age}, Income: {income}")

        result_data = data(age, 100)
        print(f"Logic function output: {result_data}")

        calculated_income = 0.7 * income
        
        html_table = dict_to_html_table(result_data)
        
        new_user = db(username=name, email=f"{name}@example.com", age=age, income=income)
        db.session.add(new_user)
        db.session.commit()
        
        return render_template('logic.html', name=name, age=age, calculated_income=calculated_income, table=html_table)
    
    except Exception as e:
        db.session.rollback() 
        print(f"Error: {str(e)}")
        return f"Error processing data: {str(e)}", 400  
    
@app.route('/users')
def view_users():
    users = db.query.all()
    return render_template('users.html', users=users)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=8000, debug=True)
