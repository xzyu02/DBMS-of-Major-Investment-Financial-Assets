/* Find all stocks’ historical data preserved in the db */
DELIMITER $$
CREATE PROCEDURE find_all_stock()
BEGIN
SELECT * FROM stock ;
END $$
DELIMITER 

/* Search for a specific commodity’s symbol & name preserved in db */
DELIMITER $$
CREATE PROCEDURE find_commodities_by_symbol(in a_symbol VARCHAR(255))
BEGIN
SELECT * FROM commo WHERE symbol=a_symbol;
END $$
DELIMITER ;

/* Find all commodities’ symbol and their names preserved in db */
delimiter $$
CREATE PROCEDURE find_all_commodity()
BEGIN
SELECT * FROM commo;
end $$ 
delimiter;

/* Search for stocks’ historical data by country */
DELIMITER $$
CREATE PROCEDURE find_stocks_by_country(in a_country VARCHAR(255))
BEGIN
SELECT name, country FROM stock WHERE country=a_country;
END $$
DELIMITER ;

