from flask import Flask, render_template, request

app = Flask(__name__)

questions = [
    {
        "question": "What is 2 + 2?",
        "options": ["1","2","4","5"],
        "answer": "4"
    },
    {
        "question": "Capital of France?",
        "options": ["London","Paris","Rome","Madrid"],
        "answer": "Paris"
    },
    {
        "question": "HTML stands for?",
        "options": ["Hyper Text Markup Language","Home Tool Markup Language","Hyperlinks Text","HighText Machine"],
        "answer": "Hyper Text Markup Language"
    },
    {
        "question": "Which language is used with Flask?",
        "options": ["Java","Python","C++","PHP"],
        "answer": "Python"
    },
    {
        "question": "Which symbol starts a comment in Python?",
        "options": ["//","#","<!--","**"],
        "answer": "#"
    },
    {
        "question": "Which company created Python?",
        "options": ["Microsoft","Google","Python Software Foundation","Apple"],
        "answer": "Python Software Foundation"
    },
    {
        "question": "Which HTML tag is used for a paragraph?",
        "options": ["<p>","<h1>","<div>","<span>"],
        "answer": "<p>"
    },
    {
        "question": "Which method sends form data in HTML?",
        "options": ["POST","GET","SEND","PUSH"],
        "answer": "POST"
    },
    {
        "question": "Which file runs a Flask application?",
        "options": ["main.py","run.py","app.py","server.py"],
        "answer": "app.py"
    },
    {
        "question": "What does CPU stand for?",
        "options": ["Central Processing Unit","Computer Personal Unit","Central Power Unit","Control Processing Unit"],
        "answer": "Central Processing Unit"
    },
    {
    "question": "Which protocol is used to load web pages?",
    "options": ["FTP","HTTP","SMTP","SSH"],
    "answer": "HTTP"
    }
]

@app.route("/", methods=["GET","POST"])
def home():

    if request.method == "POST":

        score = 0

        for i, q in enumerate(questions):

            user_answer = request.form.get(f"q{i}")

            if user_answer == q["answer"]:
                score += 1

        return render_template("result.html", score=score, total=len(questions))

    return render_template("home.html", questions=questions)


if __name__ == "__main__":
    app.run(debug=True)
