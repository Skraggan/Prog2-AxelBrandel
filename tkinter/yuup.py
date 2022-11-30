import tkinter as tk

root=tk.Tk()
f1 = tk.Frame(width=200, height=200, background="red")
f2 = tk.Frame(width=100, height=100, background="blue")

f1.pack(fill="both", expand=True, padx=20, pady=20)
f2.place(in_=f1, anchor="c", relx=.5, rely=.5)

root.mainloop()