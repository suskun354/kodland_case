from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/Yunus Emre Duran/Desktop/kodland_case/instance/exams.db'
db = SQLAlchemy(app)

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String(100), nullable=False)
    question_text = db.Column(db.String(200), nullable=False)
    correct_answer = db.Column(db.String(100), nullable=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/exam/<topic>', methods=['GET', 'POST'])
def exam(topic):
    questions = Question.query.filter_by(topic=topic).all()
    if request.method == 'POST':
        score = 0
        for question in questions:
            user_answer = request.form.get(f'answer{question.id}')
            if user_answer and user_answer.lower() == question.correct_answer.lower():
                score += 100
        
        session['score'] = score
        if 'high_score' not in session or score > session['high_score']:
            session['high_score'] = score
        
        return redirect(url_for('result'))
    return render_template('exam.html', topic=topic, questions=questions)

@app.route('/result')
def result():
    score = session.get('score', 0)
    high_score = session.get('high_score', 0)
    return render_template('result.html', score=score, high_score=high_score)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
