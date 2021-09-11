import sqlite3

conn = sqlite3.connect('sozluk.db')
c = conn.cursor()
c.execute('create table data(ID INTEGER PRIMARY KEY AUTOINCREMENT, baslik TEXT, icerik TEXT, tarih TEXT)')
conn.commit()
c.execute("insert into data(baslik, icerik, tarih) values (?,?,?)", ("deneme","deneme","deneme"))
conn.commit()
