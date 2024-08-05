from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///habits.db'
db = SQLAlchemy(app)

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    habit = db.Column(db.String(100), nullable=False)
    habit_description = db.Column(db.String(300), nullable=False)
    frequency = db.Column(db.String(100), nullable=False)
    difficulty = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
'''
def create_app():

    with app.app_context():
        db.create_all() 
    return app 

'''
@app.route('/')

def home():
   return render_template('homePage.html')

@app.route('/login')
def login():
    return render_template('loginPage.html')



@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboardPage.html')

@app.route('/habitPage', methods=['GET', 'POST'])
def habitPage():
    '''
    if request.method == "POST":
        habit = request.form['habit']
        habit_description = request.form['habit_description']
        frequency = request.form['frequency']
        difficulty = request.form['difficulty']
        email = request.form['email']
        print(habit)
        print(habit_description)
        print(frequency)
        print(difficulty)
        print(email)


        new_habit = Profile(
            habit=habit,
            habit_description=habit_description,
            frequency=frequency,
            difficulty=difficulty,
            email=email
        )
        db.session.add(new_habit)
        db.session.commit()

        return redirect(url_for('dashboard'))  # Redirect to the form page or another page after submission
        '''
    return render_template('habitPage.html')

@app.route('/submit', methods=['POST'])
def submit():
    return "Form submitted"

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5200)

