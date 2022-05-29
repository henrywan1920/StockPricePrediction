# StockPricePrediction

## Stock information crawler
1. cd workspace
2. rm -rf stocks_csvs (if want to update stock price)
3. mkdir stocks_csvs
4. rm stocks_in_recent_5_years.csv
5. touch stocks_in_recent_5_years.csv
6. pip install -r requirements.txt
7. python3 get_stock_price.py
8. ./merge.sh
9. Finally, the latest stock prices will be put into stocks_in_recent_years
