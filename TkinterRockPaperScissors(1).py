import tkinter as tk, random
from PIL import Image, ImageTk

win = tk.Tk()
win.geometry("600x600")
win.resizable(width = True, height = True)
win.title = "Rock, Paper, Scissors"
win.configure(bg = "gray")

heading = tk.Label(win, text = "Rock, Paper, Scissors", bg = "gray", font = ("Sans", 25))
heading.pack()

instructions = tk.Label(win, text = "Rock > Scissors, Scissors > Paper, Paper > Rock.", bg = "gray", font = ("Sans", 15))
instructions.pack()

def throw_rock():
  global user
  user = rock_btn
  if user == rock_btn and computer == scissors_btn:
    replace_label.config(image = rock)
    replace_label.pack()
    vic.pack()
    return replace_label
  elif user == rock_btn and computer == rock_btn:
    replace_label.config(image = rock)
    replace_label.pack()
    tie.pack()
    return replace_label
  elif user == rock_btn and computer == paper_btn:
    replace_label.config(image = rock)
    replace_label.pack()
    lose.pack()
  else:
    error.pack()
    return error

def throw_paper():
  global user
  user = paper_btn
  if user == paper_btn and computer == rock_btn:
    replace_label.config(image = paper)
    replace_label.pack()
    vic.pack()
    return replace_label
  elif user == paper_btn and computer == paper_btn:
    replace_label.config(image = paper)
    replace_label.pack()
    tie.pack()
    return replace_label
  elif user == paper_btn and computer == scissors_btn:
    replace_label.config(image = paper)
    replace_label.pack()
    lose.pack()
    return replace_label
  else:
    error.pack()
    return error

def throw_scissors():
  global user
  user = scissors_btn
  if user == scissors_btn and computer == paper_btn:
    replace_label.config(image = scissors)
    replace_label.pack()
    vic.pack()
    return replace_label
  elif user == scissors_btn and computer == scissors_btn:
    replace_label.config(image = scissors)
    replace_label.pack()
    tie.pack()
    return replace_label
  elif user == scissors_btn and computer == rock_btn:
    replace_label.config(image = scissors)
    replace_label.pack()
    lose.pack()
    return replace_label
  else:
    error.pack()
    return error

rock_btn = tk.Button(win, text = "Rock", command = throw_rock)
rock_btn.pack()
paper_btn = tk.Button(win, text = "Paper", command = throw_paper)
paper_btn.pack()
scissors_btn = tk.Button(win, text = "Scissors", command = throw_scissors)
scissors_btn.pack()

computer = random.choice([rock_btn, paper_btn, scissors_btn])

replace_label = tk.Label(win, text = "")

error = tk.Label(win, text = "Error...", bg = "gray")
tie = tk.Label(win, text = "It's a tie!", bg = "gray")
lose = tk.Label(win, text = "You lost!", bg = "gray")
vic = tk.Label(win, text = "You won!", bg = "gray")

rock_img = Image.open("Python/rock.png")
paper_img = Image.open("Python/paper.png")
scissors_img = Image.open("Python/scissors.png")
rock = ImageTk.PhotoImage(image = rock_img)
paper = ImageTk.PhotoImage(image = paper_img)
scissors = ImageTk.PhotoImage(image = scissors_img)

win.mainloop()