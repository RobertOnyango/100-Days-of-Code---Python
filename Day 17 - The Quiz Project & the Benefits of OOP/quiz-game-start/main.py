from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Create a question bank: A list of Question objects whose attributes are the dcitonary items from the question_data

# List to hold the questions i.e. question_bank
question_bank = []

# Task 1: Iterate over the question_data
for question in question_data:
    # print(question)
    # print(item["text"])
    # print(item["answer"])

    # Task 2: At each iteration, create a Question Object
    new_question = Question(question["text"], question["answer"])

    # Task 3: Append each new Question to the question bank
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

# Game condition: while current question count is less than the length of the list, play game
while quiz.still_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")