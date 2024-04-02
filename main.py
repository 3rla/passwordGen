# pip install pyperclip
# pip install tk

import random
import string
import tkinter as tk
import pyperclip

def generate():
    try:
        password_length = int(placeholder.get())  # Get password length from entry widget
    except ValueError:
        print("Please enter a valid number for password length")
        return

    if password_length < 1:
        print("Password length must be greater than 0")
        return
    elif password_length > 100:
        print("Password length must be less than 100")
        return
    else:
        symbols = ''
        if include_symbols.get():
            symbols += string.punctuation
        if include_numbers.get():
            symbols += string.digits
        if include_lowercase.get():
            symbols += string.ascii_lowercase
        if include_uppercase.get():
            symbols += string.ascii_uppercase

        if not symbols:
            print("Please select at least one character type")
            return

        password = ''.join(random.choice(symbols) for _ in range(password_length))
        password_label.config(text=password)
        pyperclip.copy(password)  # Copy the generated password to the clipboard


root = tk.Tk()

root.geometry("600x500")
root.title("Password Generator")

label1 = tk.Label(root, text="Password Generator", font=("Arial", 24))
label1.pack()

label2 = tk.Label(root, text="Enter password length", font=("Arial", 16))
label2.pack()

validate_cmd = root.register(lambda P: P.isdigit() or P == "")  # Validation function allowing only digits
placeholder = tk.Entry(root, font=("Arial", 16), validate="key", validatecommand=(validate_cmd, '%P'))
placeholder.pack()

include_symbols = tk.BooleanVar()
include_symbols.set(False)
include_symbols_checkbox = tk.Checkbutton(root, text="Include Symbols", variable=include_symbols)
include_symbols_checkbox.pack()

include_numbers = tk.BooleanVar()
include_numbers.set(False)
include_numbers_checkbox = tk.Checkbutton(root, text="Include Numbers", variable=include_numbers)
include_numbers_checkbox.pack()

include_lowercase = tk.BooleanVar()
include_lowercase.set(False)
include_lowercase_checkbox = tk.Checkbutton(root, text="Include Lowercase", variable=include_lowercase)
include_lowercase_checkbox.pack()

include_uppercase = tk.BooleanVar()
include_uppercase.set(False)
include_uppercase_checkbox = tk.Checkbutton(root, text="Include Uppercase", variable=include_uppercase)
include_uppercase_checkbox.pack()

button = tk.Button(root, text="Generate", font=("Arial", 16), command=generate)
button.pack()

password_label = tk.Label(root, text="", font=("Arial", 16), wraplength=500)
password_label.pack()

root.mainloop()