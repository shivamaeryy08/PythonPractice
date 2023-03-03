from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
question_bank = []

for questions in question_data:
    text = questions["text"]
    answer = questions["answer"]
    question_bank.append(Question(text,answer))

quiz = QuizBrain(question_bank)
while quiz.has_questions():
    quiz.next_question()


