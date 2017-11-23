import csv, sqlite3

con = sqlite3.connect("STOCK.db")
cur = con.cursor()
 
with open('comp.csv','rb') as csvfile: 
    
    d = csv.DictReader(csvfile) 
    to_db = [(i['company_id'], i['code'],i['name']) for i in d]

cur.executemany("INSERT INTO Company(company_id,code,name) VALUES (?, ?, ?);", to_db)
con.commit()
con.close()

con = sqlite3.connect("STOCK.db")
cur = con.cursor()
 
with open('exchange_data.csv','rb') as csvfile: 
    
    d = csv.DictReader(csvfile) 
    to_db = [(i['id'], i['code'],i['name']) for i in d]

cur.executemany("INSERT INTO exchange(exchange_id,code,name) VALUES (?, ?, ?);", to_db)
con.commit()
con.close()


con = sqlite3.connect("STOCK.db")
cur = con.cursor()
 
with open('stock_data.csv','rb') as csvfile: 
    
    d = csv.DictReader(csvfile) 
    to_db = [(i['Stock_id'], i['symbol'],i['company_ID'],i['exchange_ID']) for i in d]

cur.executemany("INSERT INTO Stock(Stock_id, symbol, company_ID,exchange_ID) VALUES (?, ?, ?, ?);", to_db)
con.commit()
con.close()


    
 
