#!/usr/bin/env python
# coding: utf-8

# In[3]:


import tkinter as tk

def on_click(event):
    text = event.widget.cget("text")
    
    if text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        current_text = entry.get()
        entry.delete(0, tk.END)
        entry.insert(tk.END, current_text + text)

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root, font=("Arial", 20))
entry.pack(fill=tk.BOTH, expand=True, padx=10, pady=10, ipadx=10, ipady=10)

button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row, col = 1, 0
for button_text in buttons:
    button = tk.Button(button_frame, text=button_text, font=("Arial", 20), padx=20, pady=20)
    button.grid(row=row, column=col)
    button.bind("<Button-1>", on_click)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()


# In[ ]:




