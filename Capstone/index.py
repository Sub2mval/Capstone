from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Define User table
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    birthdate = db.Column(db.Date, nullable=True)
    height = db.Column(db.Float, nullable=True)
    gender = db.Column(db.String(10), nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=True)

    def __init__(self, name, username, birthdate=None, height=None, gender=None, email=None):
        self.name = name
        self.username = username
        self.birthdate = birthdate
        self.height = height
        self.gender = gender
        self.email = email

# Define DailyLog table
class DailyLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    hr_variability = db.Column(db.Integer, nullable=True)

    def __init__(self, user_id, hr_variability=None):
        self.user_id = user_id
        self.hr_variability = hr_variability

# Define Food and Exercise models for the DailyLog table
class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    daily_log_id = db.Column(db.Integer, db.ForeignKey('daily_log.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    portion_size = db.Column(db.String(50), nullable=False)
    calories = db.Column(db.Float, nullable=False)
    proteins = db.Column(db.Float, nullable=False)
    fats = db.Column(db.Float, nullable=False)
    carbs = db.Column(db.Float, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, daily_log_id, name, portion_size, calories, proteins, fats, carbs):
        self.daily_log_id = daily_log_id
        self.name = name
        self.portion_size = portion_size
        self.calories = calories
        self.proteins = proteins
        self.fats = fats
        self.carbs = carbs

class Exercise(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    daily_log_id = db.Column(db.Integer, db.ForeignKey('daily_log.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    weight = db.Column(db.Float, nullable=True)
    sets = db.Column(db.Integer, nullable=True)
    reps = db.Column(db.Integer, nullable=True)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __init__(self, daily_log_id, name, weight=None, sets=None, reps=None):
        self.daily_log_id = daily_log_id
        self.name = name
        self.weight = weight
        self.sets = sets
        self.reps = reps

# Define HealthData table
class HealthData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    cholesterol = db.Column(db.Float, nullable=True)
    blood_sugar = db.Column(db.Float, nullable=True)
    heart_rate = db.Column(db.Float, nullable=True)
    blood_pressure = db.Column(db.Float, nullable=True)
    score = db.Column(db.Float, nullable=True)

    def __init__(self, user_id, cholesterol=None, blood_sugar=None):
        self.user_id = user_id
        self.cholesterol = cholesterol
        self.blood_sugar = blood_sugar

# Create the tables
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    return render_template('profile.html')

@app.route('/food', methods=['GET', 'POST'])
def food():
    return render_template('food.html')

@app.route('/test', methods=['GET', 'POST'])
def test():
    return render_template('test.html')

@app.route('/workout', methods=['GET', 'POST'])
def workout():
    return render_template('workout.html')

if __name__ == '__main__':
    app.run(debug=True)