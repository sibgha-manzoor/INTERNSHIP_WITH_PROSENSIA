def get_questions_and_answers():
    questions_and_answers = {
        "What is 7 + 5?": "12",
        "What is 15 - 9?": "6",
        "What is 3 * 4?": "12",
        "What is 16 / 2?": "8",
        "What is 2 ** 3?": "8",
        "What is the remainder when 10 is divided by 3?": "1",
        "What is 8 + 3 * 2?": "14",
        "What is (8 + 3) * 2?": "22",
        "What is 18 // 5?": "3",
        "What is 25 % 4?": "1"
    }
    return questions_and_answers

def ask_question(question, correct_answer):
    user_answer = input(question + " ")
    if user_answer.strip() == correct_answer:
        print("Correct!")
        return True
    else:
        print(f"Incorrect. The correct answer is {correct_answer}.")
        return False

def main():
    questions_and_answers = get_questions_and_answers()
    score = 0
    total_questions = len(questions_and_answers)

    for question, correct_answer in questions_and_answers.items():
        if ask_question(question, correct_answer):
            score += 1

    print(f"\nQuiz Over! Your final score is {score}/{total_questions}.")

if __name__ == "__main__":
    main()