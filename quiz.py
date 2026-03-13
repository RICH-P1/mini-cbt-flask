# Step 1: Setup - list of dictionaries
quiz_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
        "correct_answer": "C"
    },
    {
        "question": "Which language is used for Data Science?",
        "options": ["A. HTML", "B. Python", "C. CSS", "D. Java"],
        "correct_answer": "B"
    },
    {
        "question": "What is 10 + 5?",
        "options": ["A. 12", "B. 13", "C. 14", "D. 15"],
        "correct_answer": "D"
    }
]

# Step 5: Function to calculate result
def calculate_result(score, total):
    percentage = (score / total) * 100
    print("\nFinal Score:", score, "/", total)
    print("Percentage:", percentage, "%")

    if percentage >= 50:
        print("You passed the quiz 🎉")
    else:
        print("You failed the quiz ❌")


# Step 2: Score variable
score = 0

# Step 3: Loop through questions
for q in quiz_questions:
    print("\n" + q["question"])

    # Step 4: Show options
    for option in q["options"]:
        print(option)

    # Step 3: User input
    user_answer = input("Enter your answer (A/B/C/D): ").upper()

    # Step 4: Evaluate answer
    if user_answer == q["correct_answer"]:
        print("Correct! ✅")
        score += 1
    else:
        print("Wrong! ❌ The correct answer is", q["correct_answer"])


# Step 5: Output result
calculate_result(score, len(quiz_questions))