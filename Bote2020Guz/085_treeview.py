import os
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('320x240')
f = tk.Frame(root)
tv = ttk.Treeview(f, show='tree')
ybar = tk.Scrollbar(f, orient=tk.VERTICAL,
                    command=tv.yview)
tv.configure(yscroll=ybar.set)
directory = './..'
tv.heading('#0', text='Dir：' + directory, anchor='w')
path = os.path.abspath(directory)
node = tv.insert('', 'end', text=path, open=True)


def traverse_dir(parent, path):
    for d in os.listdir(path):
        full_path = os.path.join(path, d)
        isdir = os.path.isdir(full_path)
        id = tv.insert(parent, 'end', text=d, open=False)
        if isdir:
            traverse_dir(id, full_path)


traverse_dir(node, path)
ybar.pack(side=tk.RIGHT, fill=tk.Y)
tv.pack()
f.pack()
root.mainloop()
