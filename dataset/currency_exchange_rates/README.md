# NOTE ABOUT correct using two `_scrape.py` script

data cleaning is done in two scripts (both named `scrape.ipynb`). Please read this instruction carefully in order to acquire correct data cleaning result!

File directory introduction:
- **`./_WS_XRU_D_csv_row.csv`:** most original data from [source](https://www.bis.org/statistics/xrusd.htm)
- **`./_exchange_rate_against_usd.csv`:** pre-processed file for further cleaning & format adjusting in `./_scrape.py`
- **`./_exchangeRate_merged.csv`:** the final cleaned version of data
- **`./_metadata.txt`:** important matadata for query
- **`./_scrape.py`:** first data cleaning script: cleaning `NaN` values in `./_exchange_rate_against_usd.csv` & separate to multi csvs by country/region
- **`./separated/_scrape.py`:** handle further col re-naming, date re-formating, & col adding thing, etc.
  
**Please NOTE** that you have to delete all csv files under `./separated` folder to **run scripts successfuly**. Please run `./_scrape.py`first. After running that, please remember to go into the `./separated` folder and delete `USD.csv` manually as 1. we don't need this file for final data and 2.it will cause script running errors.Finally, please run `./separated/_scrape.py` to get `./_exchangeRate_merged.csv`.




Please contact [Author](mailto::shikwkevin@outlook.com) for further questions.

Date: 2022.8.3


