from flask import Flask, render_template, request

app = Flask(__name__)

questions = [
    {
        "question": "1.What is 2 + 2?",
        "options": ["1","2","4","5"],
        "answer": "4"
    },
    {
        "question": "2.Capital of France?",
        "options": ["London","Paris","Rome","Madrid"],
        "answer": "Paris"
    },
    {
        "question": "3.HTML stands for?",
        "options": ["Hyper Text Markup Language","Home Tool Markup Language","Hyperlinks Text","HighText Machine"],
        "answer": "Hyper Text Markup Language"
    },
    {
        "question": "4.Which language is used with Flask?",
        "options": ["Java","Python","C++","PHP"],
        "answer": "Python"
    },
    {
        "question": "5.Which symbol starts a comment in Python?",
        "options": ["//","#","<!--","**"],
        "answer": "#"
    },
    {
        "question": "6.Which company created Python?",
        "options": ["Microsoft","Google","Python Software Foundation","Apple"],
        "answer": "Python Software Foundation"
    },
    {
        "question": "7.Which HTML tag is used for a paragraph?",
        "options": ["<p>","<h1>","<div>","<span>"],
        "answer": "<p>"
    },
    {
        "question": "8.Which method sends form data in HTML?",
        "options": ["POST","GET","SEND","PUSH"],
        "answer": "POST"
    },
    {
        "question": "9.Which file runs a Flask application?",
        "options": ["main.py","run.py","app.py","server.py"],
        "answer": "app.py"
    },
    {
        "question": "10.What does CPU stand for?",
        "options": ["Central Processing Unit","Computer Personal Unit","Central Power Unit","Control Processing Unit"],
        "answer": "Central Processing Unit"
    },
    {
    "question": "11.Which protocol is used to load web pages?",
    "options": ["FTP","HTTP","SMTP","SSH"],
    "answer": "HTTP"
    },
    {
    "question": "12.What does IP stand for in internet terminology?",
    "options": ["internet patg","internet provider","internet protocol","internet process"],
    "answer": "internet protocol"
    },
    {
    "question": "13.Which of these is the correct file extension for a Python file?",
    "options": [".java", ".py", ".html", ".txt"],
    "answer": ".py"
    },
    {
    "question": "14.What does the '=' operator do in most programming languages?",
    "options": ["Checks if values are equal", "Assigns a value to a variable", "Adds two numbers", "Deletes a variable"],
    "answer": "Assigns a value to a variable"
    },
    {
    "question": "15.Which symbol is used to start a comment in Python?",
    "options": ["//", "/*", "#", "<!--"],
    "answer": "#"
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

# List of CBT questions

# calculate user score