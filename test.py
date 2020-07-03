import sqlite3
dbs = sqlite3.connect('data.db')
kur = dbs.cursor()
a = input("Какого персонажа смотрим?:")
b = input("Какой удар изучаем?:")
kur.execute(f"SELECT * FROM '{a}' WHERE Move='{b}'")
print (kur.fetchone())
input()