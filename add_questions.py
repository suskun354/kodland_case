from app import app, db, Question

questions = [
    {"topic": "python-ai", "question_text": "What is AI?", "correct_answer": "Artificial Intelligence"},
    {"topic": "python-ai", "question_text": "What is Machine Learning?", "correct_answer": "A subset of AI"},
    {"topic": "computer-vision", "question_text": "What is Computer Vision?", "correct_answer": "A field of AI"},
    {"topic": "computer-vision", "question_text": "What is Image Processing?", "correct_answer": "Manipulating images"},
    {"topic": "nlp", "question_text": "What is NLP?", "correct_answer": "Natural Language Processing"},
    {"topic": "nlp", "question_text": "What is Tokenization?", "correct_answer": "Splitting text into tokens"},
    {"topic": "ai-applications", "question_text": "How to implement AI models?", "correct_answer": "Using Python"},
    {"topic": "ai-applications", "question_text": "What is TensorFlow?", "correct_answer": "An AI library"},
]

with app.app_context():
    for q in questions:
        question = Question(topic=q["topic"], question_text=q["question_text"], correct_answer=q["correct_answer"])
        db.session.add(question)
    db.session.commit()
