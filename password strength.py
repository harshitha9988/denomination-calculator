import tkinter as tk
from tkinter import messagebox

def check_strength():
    password = entry.get()
    length = len(password)

    if length == 0:
        result_label.config(text="Please enter a password.", fg="red")
    elif length < 6:
        result_label.config(text="Weak Password (Too Short)", fg="red")
    elif 6 <= length < 10:
        result_label.config(text="Moderate Password", fg="orange")
    else:
        result_label.config(text="Strong Password", fg="green")

root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("350x200")
root.resizable(False, False)

tk.Label(root, text="Enter Password:", font=("Arial", 12)).pack(pady=10)

entry = tk.Entry(root, show="*", width=30, font=("Arial", 12))
entry.pack()

check_button = tk.Button(root, text="Check Strength", command=check_strength, font=("Arial", 12))
check_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack()
root.mainloop()