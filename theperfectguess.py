#without gui  
"""import random 

random_number=random.randint(0,99)
player_no=-1
Number_guess =0
while(player_no != random_number):
    Number_guess+=1
    player_no = int(input("Enter The Number:  "))
    if player_no > random_number :
        print(f"Your No {player_no} Is Greater Than Actual Number Please Enter Lower No.: ")
    elif player_no < random_number :
        print(f"Your No {player_no} Is Less Than Actual Number Please Enter Greater No.: ")
    else :
        print(f"Hurray😍😍 You Guess The Right No. {Number_guess}")
        break"""


#with gui
import random
import tkinter as tk
from tkinter import messagebox

#
random_number = random.randint(0, 99)
number_guess = 0

def check_guess():
    global number_guess
    try:
        player_no = int(entry.get())
        number_guess += 1
        
        if player_no > random_number:
            result_label.config(text=f"Your No {player_no} is Too High! ⬇️", fg="red")
        elif player_no < random_number:
            result_label.config(text=f"Your No {player_no} is Too Low! ⬆️", fg="blue")
        else:
            messagebox.showinfo("Congratulations!", f"Hurray! 🎉 You Guessed The Right Number in {number_guess} attempts!")
            root.quit()
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number!")

# GUI Setup
root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("400x300")
root.configure(bg="#f0f0f0")

# Widgets
title_label = tk.Label(root, text="Guess the Number (0-99)", font=("Arial", 16, "bold"), bg="#f0f0f0")
title_label.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14), justify="center")
entry.pack(pady=5)

submit_button = tk.Button(root, text="Submit Guess", font=("Arial", 12), command=check_guess, bg="#4CAF50", fg="white")
submit_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), bg="#f0f0f0")
result_label.pack(pady=10)

# Run the GUI
root.mainloop()
