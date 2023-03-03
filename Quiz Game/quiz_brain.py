class QuizBrain:
    def __init__(self, questions_list):
        self.question_number = 0
        self.questions_list = questions_list
        self.score = 0

    def has_questions(self):
        if self.question_number < len(self.questions_list):
            return True
        else:
            self.completed_quiz()
            return False

    def next_question(self):
        question = self.questions_list[self.question_number]
        q_answer = self.questions_list[self.question_number].answer
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number} : {question.text} (True/False)?: ")
        self.check_answer(user_answer, q_answer)

    def check_answer(self, user_answer, q_answer):
        if user_answer.lower() == q_answer.lower():
            print(f"You got the question correct, the answer was {q_answer}")
            self.score += 1
            print(f"You have a total score of {self.score}/{self.question_number}\n")
        else:
            print("You got the question incorrect")
            print(f"The question answer was {q_answer}")
            print(f"You have a total score of {self.score}/{self.question_number}\n")

    def completed_quiz(self):
        print("You've completed the quiz")
        print(f"Your final score was: {self.score}/{self.question_number}\n")
