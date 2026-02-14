from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

# A class that will have interface objects
class QuizInterface:
    # quize_brain: QuizBrain is a line that says we MUST pass in an object,quiz_brain, that is of type class QuizBrain
    def __init__(self, quiz_brain: QuizBrain):
        # Variable that holds the quiz_brain object
        self.quiz = quiz_brain

        # Create the window
        self.window = Tk()
        # Set window title
        self.window.title("Quizzer")
        # Set the window padding and background color
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Score Label
        self.score_label = Label(text=f"Score: {self.quiz.score}", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        # Canvas that will display the questions
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(
            150, # Width in relation to canvas width
            125, # Height in relation to canvas height
            width=280,
            text="Question goes here", 
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Get the images
        correct_image = PhotoImage(file="images/true.png")
        wrong_image = PhotoImage(file="images/false.png")
        # Set the buttons
        self.correct_button = Button(image=correct_image, highlightthickness=0, command=self.true_pressed)
        self.wrong_button = Button(image=wrong_image, highlightthickness=0, command=self.false_pressed)
        # Place the buttons on the grid
        self.correct_button.grid(row=2, column=0)
        self.wrong_button.grid(row=2, column=1)
        
        # Call next question
        self.get_next_question()

        # #Ensure the window always runs
        self.window.mainloop()

    def get_next_question(self):
         # reset canvas to white everytime we move to the next question
        self.canvas.config(bg="white")
        # Make sure we still have questions
        if self.quiz.still_has_questions():
            # Get the score from the quiz_brain and output it for the user
            self.score_label.config(text=f"Score: {self.quiz.score}")
            # Call the next question object from the QuizBrain class
            question = self.quiz.next_question()
            # Configure the canvas to display the question text
            self.canvas.itemconfig(self.question_text, text=question)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz.")
            # Disable the buttons at the end of the quiz
            self.correct_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    # Function that returns true when the correct_button is pressed
    def true_pressed(self):
        answer = "True"
        # Call the check_answer method from the quiz_brain class and pass in the text true
        self.give_feedback(self.quiz.check_answer(answer))

    def false_pressed(self):
        answer = "False"
        # Call the check_answer method from the quiz_brain class and pass in the text false
        is_right = self.quiz.check_answer(answer)
        self.give_feedback(is_right)

    # Func that gives users UI feedback on right va wrong answers
    def give_feedback(self, is_right):
        # Change canvas depending on user answers RED->wrong = quiz_brain.check_answer->False or GREEN->right quiz_brain.check_answer->True
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        # Time which the canvas resets bg color to white before moving to next question
        self.window.after(1000, self.get_next_question)
        

