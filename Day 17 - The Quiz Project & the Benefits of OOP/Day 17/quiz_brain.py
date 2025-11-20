# A Class called QuizBrain that will perform the function of keeping track which question the user is currently in and proceed to display the question to the user for answers
# class QuizBrain attributes: question_number = 0 (The question_bank list starts at index 0) and the whole question_list (question_bank)
class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        # Variable that will hold the users score and updates on each question, incrementing if the user answer matches the question answer
        self.score = 0

    # Method that retrieves current question using the question_number from the question_list
    # Uses input() to display current question and prompt user for an answer
    def next_question(self):
        # Retrieve current question using the question_number attribute and from the question_list
        """ Remember that current_question below is a dictionary with the keys 'text and answer'. So to get the actual question text, we need to user  'current_question.text'"""
        current_question = self.question_list[self.question_number]

        # For display purposes, increases the question index by one
        self.question_number += 1

        # Prompt user with the question and store the answer in a variable
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False?)")

        # Call the check answer method below
        self.check_answer(user_answer, current_question.answer)

    # Method that returns a boolean depending on the value of the question_number. This method will be used to loop through the entire list of questions using a while loop
    def still_has_questions(self):
        # Use if stmt to check whether the current question number is past the size of the question_list
        if self.question_number < len(self.question_list):
            return True
        else:
            return False
        
    # Method that compares the user inputted answer and the correct answer for the Question object
    # Arguments: user_answer and correct_answer
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            # Increment scrore
            self.score += 1
            print("You got it right!")
        else:
            print("You got it wrong")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("/n")
