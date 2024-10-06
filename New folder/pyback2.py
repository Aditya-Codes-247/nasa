import tkinter as tk
from tkinter import messagebox
import time

# Quiz questions and answers
quiz_data = [
    {"question": "Which planet is known as the Red Planet?", "options": ["Earth", "Mars", "Jupiter", "Saturn"], "answer": "Mars"},
    {"question": "How many moons does Earth have?", "options": ["1", "2", "3", "4"], "answer": "1"},
    {"question": "Which planet is the largest in our solar system?", "options": ["Earth", "Jupiter", "Saturn", "Neptune"], "answer": "Jupiter"},
    {"question": "What is the name of Earth's satellite?", "options": ["Moon", "Io", "Titan", "Europa"], "answer": "Moon"},
    {"question": "Which planet is closest to the Sun?", "options": ["Venus", "Mercury", "Mars", "Earth"], "answer": "Mercury"}
]

class PlanetQuiz:
    def __init__(self, root):
        self.root = root
        self.root.title("Planet Quiz Game")
        self.root.geometry("500x400")
        self.root.config(bg="#333")  # Set background color

        # Variables
        self.question_index = 0
        self.score = 0
        self.time_left = 10  # Timer set to 10 seconds per question
        self.selected_option = tk.StringVar()

        # Welcome screen
        self.welcome_screen()

    def welcome_screen(self):
        # Display welcome screen with a start button
        self.clear_screen()
        welcome_label = tk.Label(self.root, text="Welcome to Planet Quiz!", font=("Arial", 24), bg="#333", fg="white")
        welcome_label.pack(pady=50)
        start_button = tk.Button(self.root, text="Start Quiz", font=("Arial", 16), command=self.start_quiz, bg="#28a745", fg="white")
        start_button.pack(pady=20)

    def start_quiz(self):
        # Initialize the timer and display the first question
        self.time_left = 10
        self.load_question()

    def load_question(self):
        # Load question and options
        self.clear_screen()
        question_data = quiz_data[self.question_index]

        # Question label
        self.question_label = tk.Label(self.root, text=question_data["question"], wraplength=400, font=("Arial", 16), bg="#333", fg="white")
        self.question_label.pack(pady=20)

        # Radio buttons for options
        self.radio_buttons = []
        self.selected_option.set(None)
        for i, option in enumerate(question_data["options"]):
            rb = tk.Radiobutton(self.root, text=option, variable=self.selected_option, value=option, font=("Arial", 14), bg="#333", fg="white", selectcolor="#444")
            rb.pack(anchor="w", pady=5)
            self.radio_buttons.append(rb)

        # Next button
        self.next_button = tk.Button(self.root, text="Next", command=self.next_question, bg="#28a745", fg="white", font=("Arial", 14))
        self.next_button.pack(pady=20)

        # Timer display
        self.timer_label = tk.Label(self.root, text=f"Time left: {self.time_left}", font=("Arial", 14), bg="#333", fg="red")
        self.timer_label.pack(pady=10)
        
        # Start countdown
        self.countdown()

    def countdown(self):
        if self.time_left > 0:
            self.timer_label.config(text=f"Time left: {self.time_left}")
            self.time_left -= 1
            self.root.after(1000, self.countdown)
        else:
            self.next_question()  # Auto move to next question when time is up

    def next_question(self):
        selected = self.selected_option.get()
        correct_answer = quiz_data[self.question_index]["answer"]

        if selected == correct_answer:
            self.score += 1
        
        # Move to the next question or show the final score
        self.question_index += 1
        if self.question_index < len(quiz_data):
            self.time_left = 10  # Reset the timer for the next question
            self.load_question()
        else:
            self.show_score()

    def show_score(self):
        # Clear screen and show final score
        self.clear_screen()
        score_label = tk.Label(self.root, text=f"Your final score is {self.score}/{len(quiz_data)}", font=("Arial", 20), bg="#333", fg="white")
        score_label.pack(pady=50)
        restart_button = tk.Button(self.root, text="Restart Quiz", command=self.restart_quiz, font=("Arial", 16), bg="#28a745", fg="white")
        restart_button.pack(pady=20)

    def restart_quiz(self):
        # Reset quiz variables and restart
        self.question_index = 0
        self.score = 0
        self.time_left = 10
        self.start_quiz()

    def clear_screen(self):
        # Utility to clear all widgets from the screen
        for widget in self.root.winfo_children():
            widget.destroy()

# Create the application window
root = tk.Tk()
app = PlanetQuiz(root)
root.mainloop()
