/* command to enter mysql database: 
    mysql -u shikw -h mysql.cs.wisc.edu -p
    password: 12345678
*/ 

/* create tables in database */
create table cs564_final_proj.assets (
    symbol VARCHAR(50),
    date DATE,
    open DOUBLE,
    high DOUBLE,
    low DOUBLE,
    close DOUBLE,
    volume DOUBLE,
    PRIMARY KEY (symbol, date));

create table cs564_final_proj.commo (
    symbol VARCHAR(50),
    name VARCHAR(50),
    PRIMARY KEY (symbol));

create table cs564_final_proj.stock (
    symbol VARCHAR(50),
    name VARCHAR(50),
    country VARCHAR(50),
    continent VARCHAR(50),
    PRIMARY KEY (symbol));

/* load data into the database */
load data local infile 'commo_merged.csv' into table cs564_final_proj.assets fields terminated by ',' lines terminated by '\n';
load data local infile 'stock_merged.csv' into table cs564_final_proj.assets fields terminated by ',' lines terminated by '\n';

load data local infile '_metadata_commo.csv' into table cs564_final_proj.commo fields terminated by ',' lines terminated by '\n';

load data local infile '_metadata_stock.csv' into table cs564_final_proj.stock fields terminated by ',' lines terminated by '\n';