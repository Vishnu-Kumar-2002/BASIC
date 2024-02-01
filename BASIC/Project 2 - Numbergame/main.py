import tkinter as tk
from tkinter import messagebox
import random

class NumberGuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Guess the Number")

        self.number = random.randint(1, 200)
        self.guesses_taken = 0

        self.intro_label = tk.Label(master, text="May I ask you for your name?")
        self.intro_label.pack()

        self.name_entry = tk.Entry(master)
        self.name_entry.pack()

        self.intro_button = tk.Button(master, text="Start Game", command=self.start_game)
        self.intro_button.pack()

    def start_game(self):
        self.name = self.name_entry.get()
        self.intro_label.pack_forget()
        self.name_entry.pack_forget()
        self.intro_button.pack_forget()

        self.message_label = tk.Label(self.master, text=f"{self.name}, I am thinking of a number between 1 and 200")
        self.message_label.pack()

        self.guess_entry = tk.Entry(self.master)
        self.guess_entry.pack()

        self.guess_button = tk.Button(self.master, text="Guess", command=self.make_guess)
        self.guess_button.pack()

    def make_guess(self):
        self.guesses_taken += 1
        guess = self.guess_entry.get()
        try:
            guess = int(guess)

            if 1 <= guess <= 200:
                if guess < self.number:
                    messagebox.showinfo("Guess Result", "The guess of the number that you have entered is too low")
                elif guess > self.number:
                    messagebox.showinfo("Guess Result", "The guess of the number that you have entered is too high")
                elif guess != self.number:
                    messagebox.showinfo("Guess Result", "Try Again!")

                if guess == self.number:
                    self.show_congratulations_message()

            elif guess > 200 or guess < 1:
                messagebox.showinfo("Invalid Input", "Silly Goose! That number isn't in the range!\nPlease enter a number between 1 and 200")

        except ValueError:
            messagebox.showinfo("Invalid Input", f"I don't think that {guess} is a number. Sorry")

    def show_congratulations_message(self):
        message = f'Good job, {self.name}! You guessed my number in {self.guesses_taken} guesses!'

        # Create a custom dialog with a larger size
        custom_dialog = tk.Tk()
        custom_dialog.geometry("100x100")  # Set the width and height

        # Display the message in the center of the dialog
        tk.Label(custom_dialog, text=message).pack(expand=True)

        play_again = messagebox.askquestion("Play Again", "Do you want to play again?")
        custom_dialog.destroy()  # Destroy the custom dialog after asking the question

        if play_again == 'yes':
            self.reset_game()
        else:
            self.master.destroy()

    def reset_game(self):
        self.number = random.randint(1, 200)
        self.guesses_taken = 0
        self.message_label.pack_forget()
        self.guess_entry.pack_forget()
        self.guess_button.pack_forget()

        self.intro_label.pack()
        self.name_entry.pack()
        self.intro_button.pack()


if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()
