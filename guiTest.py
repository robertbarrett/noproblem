import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image


root =tk.Tk()
root.geometry('1000x900+100+100')
root.title('Haunted Story')

notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

frame1 = tk.Frame(notebook, width=1000, height=800)
frame2 = tk.Frame(notebook, width=1000, height=800)
frame3 = tk.Frame(notebook, width=1000, height=800)
frame4 = tk.Frame(notebook, width=1000, height=800)

notebook.add(frame1, text='Story')
notebook.add(frame2, text='Inventory')
notebook.add(frame3, text='Map')
notebook.add(frame4, text='History')

filename = "house.jpg"
img = Image.open(filename)
img = img.resize((400, 340))
img = ImageTk.PhotoImage(img)
panel = ttk.Label(frame1, image=img)
panel.image = img
panel.pack()

Story="The storm raged as you arrived at Ashford Manor, drawn by a cryptic letter promising “answers and rewards.” Inside the grand parlor, ten strangers mingled uneasily, their faces as stormy as the weather outside. Lord Harrington, the manor’s reclusive owner, entered, his voice heavy with mystery.\n“You’re all here because of an old truth—or an old lie,” he said. But before he could explain, the lights flickered, and a scream pierced the dark. When the lights returned, Harrington lay dead on the floor, blood pooling beneath him.\nA voice crackled over a hidden speaker: “The game has begun. Find the truth—or die.”"

T = tk.Text(frame1, height = 15, width = 115, wrap="word", font=("Consolas", 13))
T.pack()
T.insert(tk.END, Story)


options=["Examine Harrington’s body","Search the room for hidden clues","Question the other guests","Inspect your mysterious letter"]
  
Combo = ttk.Combobox(frame1, state='readonly', values = options, width=115, font=("Consolas", 13))
Combo.set("Pick an Option")
Combo.pack(padx = 5, pady = 5)

def option_selected(self):
  selected_option = Combo.get()
  if selected_option=="Examine Harrington’s body":
    Story="You kneel beside Harrington’s body, your pulse racing. The wound on his chest is deep, likely from a knife or some sharp object. His hand is clenched tightly around something—a piece of crumpled paper. Carefully, you pry it free.\nThe note reads:\n'The past is never buried. Trust no one.'\nYou glance at his face and notice something odd. His lips are tinged blue, which seems strange for a stab wound. Was poison involved?\nAround you, the other guests murmur anxiously. Someone—a woman in an emerald dress—gasps. “The windows! They’ve been locked from the outside.”\nA stocky man in a trench coat steps forward. “We need to stick together,” he says, his voice firm. “But first, let’s make one thing clear: who here has something to hide?”\nTension thickens in the air. Harrington’s cryptic note, the locked windows, the panic in the room—all point to one unsettling truth. The killer is still here."
    T.insert(tk.END, Story)
    Combo['values']=("Confront the man in the trench coat about his confidence","Ask the woman in emerald why she checked the windows","Examine the windows yourself","Search Harrington’s pockets for more clues")
    Combo.set("")
  
    filename = "body.png"
    img = Image.open(filename)
    img = img.resize((400, 340))
    img = ImageTk.PhotoImage(img)
    panel.configure(image=img)
    panel.image = img


Combo.bind("<<ComboboxSelected>>", option_selected)


root.mainloop()


