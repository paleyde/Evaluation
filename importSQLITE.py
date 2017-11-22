import csv
import sqlite3
conn = sqlite3.connect('STOCK.db')
c = conn.cursor()

    
    
with open('comp.csv','rb') as fin1:
    
    dr1 = csv.DictReader(fin1) 
    to_db1 = [(i['id'], i['code'], i['name']) for i in dr1]
c.executemany("INSERT INTO Company (Company_id, code, name) VALUES (?, ?, ?);", to_db1)
conn.commit()
conn.close()

for row1 in conn.execute("select Company_id,code,name from Company"):
    print (row1)    

