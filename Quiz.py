import random

class Quiz:
    total_score = 0
    count = 0

    def __init__(self, question: str, answer: str) -> None:
        self.question = question
        self.answer = answer

    def ask_question(self) -> bool:

        user_answer = input(f"{self.question}: ").strip().lower()
        Quiz.count += 1
        if user_answer == self.answer.lower():
            Quiz.total_score += 1
            print("Correct!")
            return True
        else:
            print(f" Wrong! The correct answer is '{self.answer}'.")
            return False

    @classmethod
    def get_score(cls) -> str:

        if cls.count == 0:
            return " No questions attempted yet!"
        percentage = (cls.total_score / cls.count) * 100
        return f" Final Score: {cls.total_score}/{cls.count} ({percentage:.1f}%)"

    @classmethod
    def reset_quiz(cls) -> None:

        cls.total_score = 0
        cls.count = 0


# Example usage:
if __name__ == "__main__":
    questions = [
        Quiz("What is the next number after 45?", "46"),
        Quiz("What is 5 + 7?", "12"),
        Quiz("Capital of France?", "Paris")
    ]
    random.shuffle(questions)

    print("Welcome to the Quiz! ")

    for question in questions:
        question.ask_question()

    print(Quiz.get_score())
