from google import genai

print("Welcome to the Quiz! ")
subject = input("Enter a subject name: ")
question_number = input("Enter a question number: ")


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
            print(f"Wrong! The correct answer is '{self.answer}'.")
            return False

    @classmethod
    def get_score(cls) -> str:
        if cls.count == 0:
            return "No questions attempted yet!"
        percentage = (cls.total_score / cls.count) * 100
        return f"Final Score: {cls.total_score}/{cls.count} ({percentage:.1f}%)"

    @classmethod
    def reset_quiz(cls) -> None:
        cls.total_score = 0
        cls.count = 0



client = genai.Client(api_key="YOUR_API_KEY_HERE")#!!! change this line


with open("myquestion.txt", "w") as f:
    f.write("")


for x in range(int(question_number)):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"Generate a quiz question about {subject}. The question must be answerable with a single word. Provide the response in the following exact format: question ; answer"
    )


    with open("myquestion.txt", "a") as f:
        f.write(response.text + "\n")


quiz_questions = []
with open("myquestion.txt", "r") as f:
    for line in f:
        line = line.strip()
        if line and ';' in line:
            try:
                question_text, answer_text = line.split(' ; ', 1)
                quiz_obj = Quiz(question_text.strip(), answer_text.strip())
                quiz_questions.append(quiz_obj)
            except ValueError:
                print(f"Skipping malformed line: {line}")


print(f"\nStarting quiz with {len(quiz_questions)} questions...\n")
for i, quiz_question in enumerate(quiz_questions, 1):
    print(f"Question {i}:")
    quiz_question.ask_question()
    print()


print(Quiz.get_score())
