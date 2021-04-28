# pip list
# python -m pip install --upgrade pip
# pip install prettytable

from prettytable import PrettyTable

x = PrettyTable()
x.field_names = ("sn", "no", "isim")

x.add_rows([
    [1, 302323, "Ali"],
    [2, 4545, "Veli"],
    [3, 65645, "Can"]
])

print(x)
