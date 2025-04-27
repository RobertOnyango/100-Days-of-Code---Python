# Class that handles the questioning of the user
# Attributes: question_number -> Keep track of the number of questions we're in and questions_list -> Will be initialized when you create a new quiz brain. question_bank will be passed to question_list. 
# Methods: next_question() -> Will pull up the next question depending on what question number we are on

# Create the QuizBrain class
class QuizBrain:
    def __init__(self, q_list):
        # New Object = Starting at question 0
        self.question_number = 0
        # The question bank will be passed as an attribute to this object
        self.question_list = q_list
        # Attribute that keeps tarck if users score
        self.score = 0

    # Method that checks if we still have questions in the question list and returns true or false
    def still_questions(self):
        # Get the number of questions from the list
        question_count = len(self.question_list)

        if self.question_number < question_count:
            return True
        else:
            return False
        
    '''
    Shorter Version:
    def still_questions(self):
        return self.qustion_number < len(self.question_list)
    '''   

    # Method that asks the user next question based on current question
    def next_question(self):
        # Get hold of the question list and then get the question at the current question number
        current_question = self.question_list[self.question_number]
        '''
        For example, to get the current question text, current_question.text
        '''
        # Increase question number by 1
        self.question_number += 1

        # Prompt user for answer: Remeber question has two attributes from the Question Class: text and answer
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False?:")

        # Call method that checks user answers
        self.check_answer(user_answer, current_question.answer)

    # Method that compares with question answer and checks if the user answer is correct
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right")
            # Increment score attribute plus one
            self.score += 1
        else:
            print("That's wrong")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
