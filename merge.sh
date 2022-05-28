#!/bin/bash

echo "date,open,high,low,close,volume,adj_close,name" > stocks_in_recent_5_years.csv
cd stocks_csvs
stock_files=$(ls *.csv)
for stock_file in $stock_files
do
	tail -n +2 $stock_file >> ../stocks_in_recent_5_years.csv
done
