# Quiz1
AI Quiz Generator
Overview

This project uses Google’s Generative AI (Gemini) to automatically create and run quizzes directly from the command line. The program allows users to enter a subject  and specify the number of questions to generate.
The Gemini model then creates quiz questions with single-word answers, saves them to a text file, and runs an interactive quiz session where the user can answer each question. The program tracks the user’s score and displays the final results at the end.
Requirements

- Python 3.9 or later

- Google Generative AI library (google-generativeai)

- A valid Google Gemini API key (available from Google AI Studio, https://aistudio.google.com/apikey)

When prompted:

-Enter a subject name.

-Enter the number of questions you want to generate.

The program will:

-Use Gemini to create the requested number of single-word-answer questions about your chosen topic.

-Save the questions and answers to a file named myquestion.txt.

-Load the questions and start the quiz session.

Display whether each answer is correct or incorrect.

Show your final score and percentage when all questions are complete.
