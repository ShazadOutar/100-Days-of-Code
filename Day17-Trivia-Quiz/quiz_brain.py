class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        # return True if there are still questions in the question list
        # print(type(self.question_list))
        if self.question_number >= len(self.question_list):
            return False
        return True
        # could also reduce code by doing
        # return self.question_number >= len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        # increment the question number to get the next questions
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True or False) ")
        # user_answer = input(f"Q.{self.question_number + 1}: {current_question.text} (True or False) ")
        # print(user_answer)
        self.check_answer(user_answer, current_question.answer)
        print(f"Your current score is: {self.score}/{self.question_number}\n")

    def check_answer(self, user_answer, correct_answer):
        # print(f"User answer {user_answer}")
        # print(f"Correct answer {correct_answer}")
        # if the users answer is the same as the correct answer
        if user_answer.lower() == correct_answer.lower():
            print("You got it right")
            self.score += 1
        else:
            print("That's wrong")
        print(f"The correct answer was: {correct_answer}")
