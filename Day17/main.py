from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# question_bank = [ the questions from data]
question_bank = []
for index in question_data:
    # print(index)
    # could also split the text and answer before making the question
    # index["question"] is set to match the key in the question_data dictionary
    new_question = Question(index["question"], index["correct_answer"])
    # question_bank.append(Question(index["text"], index["answer"]))
    question_bank.append(new_question)


# print(new_question)
# print(new_question.text)
# print(new_question.answer)
# print(question_bank)
# print(question_bank[0].text)

my_quiz = QuizBrain(question_bank)
# my_quiz.still_has_questions()
while my_quiz.still_has_questions():
    my_quiz.next_question()

user_score = my_quiz.score
question_count = my_quiz.question_number
print("You've completed the quiz")
print(f"Your final score is {user_score}/{question_count}")
