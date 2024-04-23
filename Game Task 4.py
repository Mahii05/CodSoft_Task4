import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Rock Paper Scissors Game")

        self.create_widgets()

    def create_widgets(self):
        self.label_instruction = tk.Label(self.master, text="Choose Rock, Paper, or Scissors:")
        self.label_instruction.pack(pady=10)

        self.button_rock = tk.Button(self.master, text="Rock", width=10, command=lambda: self.play_game("rock"))
        self.button_rock.pack(pady=5)

        self.button_paper = tk.Button(self.master, text="Paper", width=10, command=lambda: self.play_game("paper"))
        self.button_paper.pack(pady=5)

        self.button_scissors = tk.Button(self.master, text="Scissors", width=10, command=lambda: self.play_game("scissors"))
        self.button_scissors.pack(pady=5)

        self.label_result = tk.Label(self.master, text="")
        self.label_result.pack(pady=10)

    def play_game(self, user_choice):
        computer_choice = random.choice(["rock", "paper", "scissors"])
        
        result = self.determine_winner(user_choice, computer_choice)
        message = f"You chose {user_choice.capitalize()}. Computer chose {computer_choice.capitalize()}.\n"

        if result == "win":
            message += "You win!"
        elif result == "lose":
            message += "You lose!"
        else:
            message += "It's a tie!"
        
        self.label_result.config(text=message)

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "tie"
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            return "win"
        else:
            return "lose"

def main():
    root = tk.Tk()
    app = RockPaperScissorsGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
