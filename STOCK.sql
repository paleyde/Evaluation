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
    Stock_id INTEGER ,
    symbol TEXT,
    company_id INTEGER,
    exchange_id INTEGER,
    FOREIGN KEY (company_id) REFERENCES Company(company_id),
    FOREIGN KEY (exchange_id) REFERENCES Exchange(exchange_id),
    PRIMARY KEY (company_id, exchange_id)
 );

CREATE TABLE Price (
    stock_id INTEGER,
    open_price FLOAT,
    high_price FLOAT,
    low_price FLOAT,
    close_price FLOAT,
    volume INTEGER,
    last_price FLOAT,
    turnover FLOAT,
    UpdatingDates DATE,
    FOREIGN KEY (stock_id) REFERENCES Stock(stock_id),
    PRIMARY KEY (stock_id, UpdatingDates)
 );



