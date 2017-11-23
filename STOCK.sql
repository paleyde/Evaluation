CREATE TABLE Company (
    company_id INTEGER PRIMARY KEY,
    name TEXT,
    code TEXT
 );
  
 
CREATE TABLE Exchange (
    Exchange_id INTEGER PRIMARY KEY,
    code TEXT,
    name TEXT
 ); 

CREATE TABLE Stock (
    Stock_id INTEGER PRIMARY KEY,
    symbol TEXT,
    company_ID INTEGER,
    exchange_ID INTEGER,
    FOREIGN KEY (company_ID) REFERENCES Company(company_id),
    FOREIGN KEY (exchange_ID) REFERENCES Exchange(exchange_id)  
 );

CREATE TABLE Price (
    open_price FLOAT,
    high_price FLOAT,
    low_price FLOAT,
    close_price FLOAT,
    volume INTEGER,
    last_price FLOAT,
    turnover FLOAT,
    UpdatingDates DATE,
    stock_ID INTEGER,
    FOREIGN KEY (stock_ID) REFERENCES Stock(stock_id),
    PRIMARY KEY (stock_ID, UpdatingDates)
 );

