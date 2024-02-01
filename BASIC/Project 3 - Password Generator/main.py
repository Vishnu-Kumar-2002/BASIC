import tkinter as tk
from tkinter import ttk, messagebox
import random
import string
import pyperclip

class PasswordGeneratorGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Generator")

        self.create_widgets()

    def create_widgets(self):
        self.label_length = ttk.Label(self.master, text="Password Length:")
        self.label_length.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

        self.entry_length = ttk.Entry(self.master)
        self.entry_length.grid(row=0, column=1, padx=10, pady=10)

        self.label_options = ttk.Label(self.master, text="Character Set Options:")
        self.label_options.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

        self.use_lowercase_var = tk.BooleanVar()
        self.checkbox_lowercase = ttk.Checkbutton(self.master, text="Include lowercase letters", variable=self.use_lowercase_var)
        self.checkbox_lowercase.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W)

        self.use_uppercase_var = tk.BooleanVar()
        self.checkbox_uppercase = ttk.Checkbutton(self.master, text="Include uppercase letters", variable=self.use_uppercase_var)
        self.checkbox_uppercase.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W)

        self.use_digits_var = tk.BooleanVar()
        self.checkbox_digits = ttk.Checkbutton(self.master, text="Include digits", variable=self.use_digits_var)
        self.checkbox_digits.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W)

        self.use_special_chars_var = tk.BooleanVar()
        self.checkbox_special_chars = ttk.Checkbutton(self.master, text="Include special characters", variable=self.use_special_chars_var)
        self.checkbox_special_chars.grid(row=5, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W)

        self.generate_button = ttk.Button(self.master, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

        self.copy_button = ttk.Button(self.master, text="Copy to Clipboard", command=self.copy_to_clipboard)
        self.copy_button.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

    def generate_password(self):
        try:
            length = int(self.entry_length.get())
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter a valid number for password length.")
            return

        use_lowercase = self.use_lowercase_var.get()
        use_uppercase = self.use_uppercase_var.get()
        use_digits = self.use_digits_var.get()
        use_special_chars = self.use_special_chars_var.get()

        try:
            password = self._generate_password(length, use_lowercase, use_uppercase, use_digits, use_special_chars)
            self.display_password(password)
        except ValueError as e:
            messagebox.showwarning("Error", str(e))

    def _generate_password(self, length, use_lowercase, use_uppercase, use_digits, use_special_chars):
        characters = ""

        if use_lowercase:
            characters += string.ascii_lowercase
        if use_uppercase:
            characters += string.ascii_uppercase
        if use_digits:
            characters += string.digits
        if use_special_chars:
            characters += string.punctuation

        if not characters:
            raise ValueError("At least one character set should be selected.")

        password = ''.join(random.choice(characters) for _ in range(length))
        return password

    def display_password(self, password):
        self.displayed_password = password
        messagebox.showinfo("Generated Password", f"Generated Password: {password}")

    def copy_to_clipboard(self):
        password = getattr(self, 'displayed_password', None)
        if password:
            pyperclip.copy(password)
            messagebox.showinfo("Copied to Clipboard", "Password copied to clipboard.")
        else:
            messagebox.showwarning("No Password", "No password generated to copy.")

def main():
    root = tk.Tk()
    password_generator_gui = PasswordGeneratorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
