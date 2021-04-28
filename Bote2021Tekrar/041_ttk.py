from tkinter import ttk  # Normal Tkinter.* widgets are not themed!
# pip install ttkthemes
from ttkthemes import ThemedTk

# https://ttkthemes.readthedocs.io/en/latest/example.html
window = ThemedTk(theme="equilux")
ttk.Button(window, text="Quit", command=window.destroy).pack()
window.mainloop()
