# NOTE ABOUT `STOCK` DATASET

The following dataset contains the historical prices of major world indexes. 

## File naming principle

~~All dataset files are named in the following format: `COUNTRY_STOCK Name.csv`~~
All dataset files are named in the following format: `Name.csv`

**UPDATE 7.27:** processed final big dataset is `_stock_merged.csv`, with to extra cols add at right-most: `Name`, `Symbol`.
## Query method

We can search for a specific index's historical price by: `country`;`STOCK_ID` (shown as the `Symbol` in `./_metadata.txt`);`FUll_Name`(shown as `Name` in `./metadata.txt`).

To check by continent, we can simply type: `America`, `Asia`, or `EUROPE` / `EMEA`.

The dataset is collected from *Yahoo Finance* using the open-source package `yfinance`. Link to yfinance official document is [here](https://github.com/ranaroussi/yfinance). All data are collected from the possible earliest date to 2022.7.1.

`_scrape.ipynb` is used to complete the data collecting & converting process. See details in the jupyter notebook.
`_metadata.txt` contains all basic information of stocks that we collected.

## REF: Country code:

[USED: Olympic Ref Wikipedia](https://zh.wikipedia.org/wiki/%E5%9C%8B%E9%9A%9B%E5%A5%A7%E5%A7%94%E6%9C%83%E5%9C%8B%E5%AE%B6%E6%88%96%E5%9C%B0%E5%8D%80%E7%B7%A8%E7%A2%BC%E5%88%97%E8%A1%A8)


[NOT USED; 2 LETTER POSTAL REF](https://www.post.gov.tw/post/internet/Postal/sz_a_e_info.jsp) 

## Contact

Please contact [comtributor](mailto:kshi42@wisc.edu) for further clarifications. 