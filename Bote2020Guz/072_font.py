import tkinter as tk

pencere = tk.Tk()
pencere.title("Font")
pencere.geometry("300x300-10+50")

lbl = tk.Label(pencere, text="BÖTE", font=("Comic Sans MS", 40), bg="CadetBlue2", fg="red")
lbl["fg"] = "LemonChiffon"
lbl.pack()

pencere.mainloop()
