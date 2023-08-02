import tkinter as tk

def on_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.title("Calculator")
root.geometry("390x420")

entry = tk.Entry(root, font=("Arial", 20))
entry.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

r, c = 0, 0
for button_text in buttons:
    button = tk.Button(button_frame, text=button_text, font=("Arial", 15), padx=20, pady=20)
    button.grid(row=r, column=c)
    button.bind("<Button-1>", on_click)
    c += 1
    if c > 3:
        c = 0
        r += 1

root.mainloop()
