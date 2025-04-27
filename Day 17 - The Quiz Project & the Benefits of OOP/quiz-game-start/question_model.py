# Create a model for a Question object in our game.
# Attributes: !uestion Text, Correct Answer
# The attributes should be initialized when creating a mnew object

# Create the class Question
class Question:
    # Initialize the question and answer
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer
