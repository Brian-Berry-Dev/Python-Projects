class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0


    def check_ans(self, user, correct):
        if user == correct:
            print("That is correct")
            self.score += 1

        print(f"Current score: {self.score}/{self.question_number}")
        print("\n")



    def has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            return False




    def next_question(self):
        current_q = self.question_list[self.question_number]
        self.question_number += 1
        user_ans = input(f"Q.{self.question_number}: {current_q.text} (True/False?): ")
        self.check_ans(user_ans, current_q.answer)

