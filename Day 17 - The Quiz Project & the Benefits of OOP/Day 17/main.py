from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Create a question bank using the data from the question_data list as attributes to pass to Question objects initialized from the Question class

# Variable list question_bank that will hold the Question objects initialized
question_bank = []

# Loop through each question from the question_bank
for question in question_data:
    # On each iteration: create a Question object, with attributes of the current question and answer
    my_question = Question(question["text"], question["answer"])
    # question_text = question["text"]
    # question_answer = question["answer"]
    # my_question = Question(question_text, question_answer)

    # Append the created question object to the question_bank list
    question_bank.append(my_question)

# print(question_bank)
# print(question_bank[0].text) # A slug's blood is green.
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
