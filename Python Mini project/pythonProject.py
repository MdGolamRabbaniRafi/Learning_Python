

def read_quiz_file(file_path):
    quiz_data = {}

    with open(file_path, 'r') as file:
        for line in file:
            question, options_str, correct_option = line.strip().split(';')
            options = options_str.split(',')
            quiz_data[question] = (options, correct_option)

    return quiz_data

# def print_quiz_data(quiz_data):
#     for question, (options, correct_option) in quiz_data.items():
#         print(f"Question: {question}")
#         print("Options:", ", ".join(options))
#         print(f"Correct Answer: {options[ord(correct_option) - ord('A')]}\n")

def start_quiz(quiz_data):
    print("Welcome to the Quiz Game!")
    print("Answer the following questions:")

    score = 0
    total_questions = len(quiz_data)

    for question, (options, correct_option) in quiz_data.items():
        print(f"\n{question}")
        for i, option in enumerate(options, start=1):
            print(f"{i}. {option}")

        user_answer = input("Enter your choice (1-4): ").strip().upper()

        if user_answer == str(ord(correct_option) - ord('A') + 1):
            print("Correct Answer!\n")
            score += 1
        else:
            correct_answer = options[ord(correct_option) - ord('A')]
            print(f"Wrong Answer! The correct answer is: {correct_answer}\n")

    print(f"Quiz Completed! Your Score: {score}/{total_questions}")

if __name__ == "__main__":
    file_path = "quiz.txt"
    quiz_data = read_quiz_file(file_path)

    while True:
        print("Quiz Game ---------")
        print("1. Start Quiz")
        print("2. Exit")

        choice = input("Enter your choice (1-2): ").strip()

        if choice == '1':
            start_quiz(quiz_data)
        elif choice == '2':
            print("Goodbye! Exiting the Quiz Game.")
            break  
        else:
            print("Invalid choice. Please select either 1 or 2.")
