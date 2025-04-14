"""import random
import tkinter as tk
from tkinter import messagebox

def play_game(user_choice):
    youdict = {"snake": 1, "water": -1, "gun": 0}
    computer_choice = random.choice(list(youdict.keys()))
    user_value = youdict.get(user_choice)
    comp_value = youdict.get(computer_choice)

    if comp_value == user_value:
        result = "😒 Game Tie!"
    elif (comp_value == -1 and user_value == 1) or (comp_value == 1 and user_value == 0) or (comp_value == 0 and user_value == -1):
        result = "😍 You Win!"
    else:
        result = "😫 You Lose!"
    
    messagebox.showinfo("Game Result", f"Computer chose {computer_choice}\nYou chose {user_choice}\n{result}")

# Create GUI window
root = tk.Tk()
root.title("Snake Water Gun Game")
root.geometry("300x250")

tk.Label(root, text="Choose One:", font=("Arial", 14)).pack(pady=10)

tk.Button(root, text="Snake", font=("Arial", 12), command=lambda: play_game("snake")).pack(pady=5)
tk.Button(root, text="Water", font=("Arial", 12), command=lambda: play_game("water")).pack(pady=5)
tk.Button(root, text="Gun", font=("Arial", 12), command=lambda: play_game("gun")).pack(pady=5)

root.mainloop()"""



"""its more attractive"""

import random
import tkinter as tk
from tkinter import messagebox

# Initialize win counter
win_count = 0  

def play_game(user_choice):
    global win_count  # Use global variable for win count
    youdict = {"snake": 1, "water": -1, "gun": 0}
    
    computer_choice = random.choice(list(youdict.keys()))
    user_value = youdict.get(user_choice)
    comp_value = youdict.get(computer_choice)

    if comp_value == user_value:
        result = "😒 Game Tie!"
    elif (comp_value == -1 and user_value == 1) or (comp_value == 1 and user_value == 0) or (comp_value == 0 and user_value == -1):
        result = "😍 You Win!"
        win_count += 1  # Increase win count when the user wins
    else:
        result = "😫 You Lose!"
    
    score_label.config(text=f"🏆 Wins: {win_count}")  # Update the score label
    messagebox.showinfo("Game Result", f"🤖 Computer chose: {computer_choice.capitalize()}\n😊 You chose: {user_choice.capitalize()}\n\n{result}")

# Create GUI window
root = tk.Tk()
root.title("🐍💦🔫 Snake-Water-Gun Game")
root.geometry("400x350")
root.configure(bg="#222831")  # Dark background

# Title label
title_label = tk.Label(root, text="Choose One", font=("Arial", 16, "bold"), fg="white", bg="#222831")
title_label.pack(pady=20)

# Score label
score_label = tk.Label(root, text=f"🏆 Wins: {win_count}", font=("Arial", 14), fg="yellow", bg="#222831")
score_label.pack(pady=5)

# Button styling
btn_style = {"font": ("Arial", 14, "bold"), "width": 12, "height": 2, "bd": 3}

# Snake button 🐍
snake_btn = tk.Button(root, text="🐍 Snake", bg="#FF9801", fg="white", command=lambda: play_game("snake"), **btn_style)
snake_btn.pack(pady=10)

# Water button 💦
water_btn = tk.Button(root, text="💦 Water", bg="#03A9F4", fg="white", command=lambda: play_game("water"), **btn_style)
water_btn.pack(pady=10)

# Gun button 🔫
gun_btn = tk.Button(root, text="🔫 Gun", bg="#E91E63", fg="white", command=lambda: play_game("gun"), **btn_style)
gun_btn.pack(pady=10)

# Run the app
root.mainloop()

