from question_model import Question
from data import question_data2
from quiz_brain import QuizBrain

question_bank = []
for i in question_data2:
    question = Question(text=i["question"], answer=i["correct_answer"])
    question_bank.append(question)

quiz = QuizBrain(questions_list=question_bank)
quiz.next_question()
while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz.")
print(f"Your final score is {quiz.score}/{quiz.question_number}")
