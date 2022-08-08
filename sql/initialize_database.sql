/* create tables in database */
CREATE TABLE assets (
	symbol VARCHAR(50), 
	date DATE,
	open DOUBLE,
	high DOUBLE,
	low DOUBLE,
	close DOUBLE,
	volume DOUBLE,
	PRIMARY KEY (symbol, date));

CREATE TABLE commo (
	symbol VARCHAR(50), 
	name VARCHAR(50), 
	PRIMARY KEY (symbol));

CREATE TABLE stock (
	symbol VARCHAR(50), 
	name VARCHAR(50), 
	country VARCHAR(50), 
	continent VARCHAR(50), 
	PRIMARY KEY (symbol));

CREATE TABLE crypto (
	symbol VARCHAR(50), 
	name VARCHAR(50), 
	PRIMARY KEY (symbol));

CREATE TABLE login (
	user VARCHAR(50), 
	password VARCHAR(50), 
	PRIMARY KEY (user, password));

CREATE TABLE watchlist (
	user VARCHAR(50), 
	symbol VARCHAR(50), 
	name VARCHAR(50), 
	type VARCHAR(50), 
	PRIMARY KEY (user, symbol));

CREATE TABLE currency (
	name VARCHAR(50), 
	symbol VARCHAR(50), 
	date DATE, 
	price VARCHAR(50), 
	PRIMARY KEY (symbol, date));

CREATE TABLE country (
	symbol VARCHAR(50), 
	name VARCHAR(50), 
	continent VARCHAR(50), 
	PRIMARY KEY (symbol));

/* please replace file path manually */
load data local infile '/Users/yuxizheng/xizheng/2022-SUMMER/CS564-Final-Project/dataset/commo_merged.csv' into table assets fields terminated by ',' lines terminated by '\n';
load data local infile '/Users/yuxizheng/xizheng/2022-SUMMER/CS564-Final-Project/dataset/stock_merged.csv' into table assets fields terminated by ',' lines terminated by '\n';
load data local infile '/Users/yuxizheng/xizheng/2022-SUMMER/CS564-Final-Project/dataset/crypto_merged.csv' into table assets fields terminated by ',' lines terminated by '\n';
load data local infile '/Users/yuxizheng/xizheng/2022-SUMMER/CS564-Final-Project/dataset/_metadata_commo.csv' into table commo fields terminated by ',' lines terminated by '\n';
load data local infile '/Users/yuxizheng/xizheng/2022-SUMMER/CS564-Final-Project/dataset/_metadata_stock.csv' into table stock fields terminated by ',' lines terminated by '\n';
load data local infile '/Users/yuxizheng/xizheng/2022-SUMMER/CS564-Final-Project/dataset/_metadata_crypto.csv' into table crypto fields terminated by ',' lines terminated by '\n';
load data local infile '/Users/yuxizheng/xizheng/2022-SUMMER/CS564-Final-Project/dataset/exchangeRate_merged.csv' into table currency fields terminated by ',' lines terminated by '\n';
