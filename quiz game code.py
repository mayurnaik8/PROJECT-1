
# Define the quiz questions, options, and answers
quiz = {
    "What is the capital of France?": {
        "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
        "answer": "C"
    },
    "What is 2 + 2?": {
        "options": ["A. 3", "B. 4", "C. 5", "D. 6"],
        "answer": "B"
    },
    "Which planet is known as the Red Planet?": {
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
        "answer": "B"
    }
}

def run_quiz(quiz):
    score = 0
    total_questions = len(quiz)
    
    for question, details in quiz.items():
        print(question)
        for option in details["options"]:
            print(option)
        
        # Get the user's answer
        user_answer = input("Please enter the letter of your answer: ").strip().upper()
        
        # Check if the answer is correct
        if user_answer == details["answer"]:
            print("Correct!")
            score += 1
        else:
            print("Wrong! The correct answer was", details["answer"])
        
        print()  # Print a blank line for better readability

    # Print the final score
    print(f"You got {score} out of {total_questions} correct.")

if __name__ == "__main__":
    run_quiz(quiz)
