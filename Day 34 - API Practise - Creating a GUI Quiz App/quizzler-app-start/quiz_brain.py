import html

class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        # ---------- HTML ENTITIES REMOVAL ----------#
        # Get the current question and use unescape method from html module to add escape characters back to teh questions
        q_text = html.unescape(self.current_question.text)    
        return f"Q.{self.question_number}: {q_text}"
        # user_answer = input(f"Q.{self.question_number}: {q_text} (True/False): ")
        # self.check_answer(user_answer)

    # Receives the strings true or false from the buttons pressed on the UI class
    def check_answer(self, user_answer: str) -> bool:
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False
