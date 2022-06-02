"""
A crawler to get prices of all the stocks from The Investor's Exchange api
"""

import pandas_datareader.data as web

from datetime import datetime
from concurrent import futures

failed_queries = []
current_time = datetime.now()
start_time = datetime(current_time.year - 5, current_time.month, current_time.day)


def query_the_iex_for(stock):
    try:
        print(stock)
        stock_df = web.DataReader(stock, 'yahoo', start_time, current_time)
        stock_df['Name'] = stock
        output_file_name = 'stocks_csvs/' + stock + '_data.csv'
        stock_df.to_csv(output_file_name)
    except:
        failed_queries.append(stock)
        print('Query failed: {}'.format(stock))


def write_failed_queries_to(failed_queries, destination_path):
    with open(destination_path, 'w') as outfile:
        for name in failed_queries:
            outfile.write(name + '\n')


if __name__ == '__main__':
    stock_names = ['MMM', 'ABT', 'ABBV', 'ABMD', 'ACN', 'ATVI', 'ADBE', 'AMD', 'AAP', 'AES', 'AFL', 'A', 'APD', 'AKAM',
               'ALK', 'ALB',
               'ARE', 'ALGN', 'ALLE', 'LNT', 'ALL', 'GOOGL', 'GOOG', 'MO', 'AMZN', 'AMCR', 'AEE', 'AAL', 'AEP', 'AXP',
               'AIG', 'AMT',
               'AWK', 'AMP', 'ABC', 'AME', 'AMGN', 'APH', 'ADI', 'ANSS', 'ANTM', 'AON', 'AOS', 'APA', 'AAPL', 'AMAT',
               'APTV', 'ADM',
               'ANET', 'AJG', 'AIZ', 'T', 'ATO', 'ADSK', 'ADP', 'AZO', 'AVB', 'AVY', 'BKR', 'BLL', 'BAC', 'BBWI', 'BAX',
               'BDX', 'BRK.B',
               'BBY', 'BIO', 'TECH', 'BIIB', 'BLK', 'BK', 'BA', 'BKNG', 'BWA', 'BXP', 'BSX', 'BMY', 'AVGO', 'BR', 'BRO',
               'BF.B', 'CHRW',
               'CDNS', 'CZR', 'CPB', 'COF', 'CAH', 'KMX', 'CCL', 'CARR', 'CTLT', 'CAT', 'CBOE', 'CBRE', 'CDW', 'CE',
               'CNC', 'CNP', 'CDAY',
               'CERN', 'CF', 'CRL', 'SCHW', 'CHTR', 'CVX', 'CMG', 'CB', 'CHD', 'CI', 'CINF', 'CTAS', 'CSCO', 'C', 'CFG',
               'CTXS', 'CLX',
               'CME', 'CMS', 'KO', 'CTSH', 'CL', 'CMCSA', 'CMA', 'CAG', 'COP', 'ED', 'STZ', 'COO', 'CPRT', 'GLW',
               'CTVA', 'COST', 'CTRA',
               'CCI', 'CSX', 'CMI', 'CVS', 'DHI', 'DHR', 'DRI', 'DVA', 'DE', 'DAL', 'XRAY', 'DVN', 'DXCM', 'FANG',
               'DLR', 'DFS', 'DISCA',
               'DISCK', 'DISH', 'DG', 'DLTR', 'D', 'DPZ', 'DOV', 'DOW', 'DTE', 'DUK', 'DRE', 'DD', 'DXC', 'EMN', 'ETN',
               'EBAY', 'ECL',
               'EIX', 'EW', 'EA', 'EMR', 'ENPH', 'ETR', 'EOG', 'EFX', 'EQIX', 'EQR', 'ESS', 'EL', 'ETSY', 'EVRG', 'ES',
               'RE', 'EXC', 'EXPE',
               'EXPD', 'EXR', 'XOM', 'FFIV', 'FB', 'FAST', 'FRT', 'FDX', 'FIS', 'FITB', 'FE', 'FRC', 'FISV', 'FLT',
               'FMC', 'F', 'FTNT', 'FTV',
               'FBHS', 'FOXA', 'FOX', 'BEN', 'FCX', 'GPS', 'GRMN', 'IT', 'GNRC', 'GD', 'GE', 'GIS', 'GM', 'GPC', 'GILD',
               'GL', 'GPN', 'GS',
               'GWW', 'HAL', 'HBI', 'HIG', 'HAS', 'HCA', 'PEAK', 'HSIC', 'HSY', 'HES', 'HPE', 'HLT', 'HOLX', 'HD',
               'HON', 'HRL', 'HST', 'HWM',
               'HPQ', 'HUM', 'HBAN', 'HII', 'IEX', 'IDXX', 'INFO', 'ITW', 'ILMN', 'INCY', 'IR', 'INTC', 'ICE', 'IBM',
               'IP', 'IPG', 'IFF', 'INTU',
               'ISRG', 'IVZ', 'IPGP', 'IQV', 'IRM', 'JKHY', 'J', 'JBHT', 'SJM', 'JNJ', 'JCI', 'JPM', 'JNPR', 'KSU', 'K',
               'KEY', 'KEYS', 'KMB',
               'KIM', 'KMI', 'KLAC', 'KHC', 'KR', 'LHX', 'LH', 'LRCX', 'LW', 'LVS', 'LEG', 'LDOS', 'LEN', 'LLY', 'LNC',
               'LIN', 'LYV', 'LKQ',
               'LMT', 'L', 'LOW', 'LUMN', 'LYB', 'MTB', 'MRO', 'MPC', 'MKTX', 'MAR', 'MMC', 'MLM', 'MAS', 'MA', 'MTCH',
               'MKC', 'MCD', 'MCK', 'MDT',
               'MRK', 'MET', 'MTD', 'MGM', 'MCHP', 'MU', 'MSFT', 'MAA', 'MRNA', 'MHK', 'TAP', 'MDLZ', 'MPWR', 'MNST',
               'MCO', 'MS', 'MOS', 'MSI', 'MSCI',
               'NDAQ', 'NTAP', 'NFLX', 'NWL', 'NEM', 'NWSA', 'NWS', 'NEE', 'NLSN', 'NKE', 'NI', 'NSC', 'NTRS', 'NOC',
               'NLOK', 'NCLH', 'NRG', 'NUE',
               'NVDA', 'NVR', 'NXPI', 'ORLY', 'OXY', 'ODFL', 'OMC', 'OKE', 'ORCL', 'OGN', 'OTIS', 'PCAR', 'PKG', 'PH',
               'PAYX', 'PAYC', 'PYPL',
               'PENN', 'PNR', 'PBCT', 'PEP', 'PKI', 'PFE', 'PM', 'PSX', 'PNW', 'PXD', 'PNC', 'POOL', 'PPG', 'PPL',
               'PFG', 'PG', 'PGR', 'PLD',
               'PRU', 'PTC', 'PEG', 'PSA', 'PHM', 'PVH', 'QRVO', 'PWR', 'QCOM', 'DGX', 'RL', 'RJF', 'RTX', 'O', 'REG',
               'REGN', 'RF', 'RSG',
               'RMD', 'RHI', 'ROK', 'ROL', 'ROP', 'ROST', 'RCL', 'SPGI', 'CRM', 'SBAC', 'SLB', 'STX', 'SEE', 'SRE',
               'NOW', 'SHW', 'SPG', 'SWKS',
               'SNA', 'SO', 'LUV', 'SWK', 'SBUX', 'STT', 'STE', 'SYK', 'SIVB', 'SYF', 'SNPS', 'SYY', 'TMUS', 'TROW',
               'TTWO', 'TPR', 'TGT', 'TEL',
               'TDY', 'TFX', 'TER', 'TSLA', 'TXN', 'TXT', 'TMO', 'TJX', 'TSCO', 'TT', 'TDG', 'TRV', 'TRMB', 'TFC',
               'TWTR', 'TYL', 'TSN', 'UDR',
               'ULTA', 'USB', 'UAA', 'UA', 'UNP', 'UAL', 'UNH', 'UPS', 'URI', 'UHS', 'VLO', 'VTR', 'VRSN', 'VRSK', 'VZ',
               'VRTX', 'VFC', 'VIAC',
               'VTRS', 'V', 'VNO', 'VMC', 'WRB', 'WAB', 'WMT', 'WBA', 'DIS', 'WM', 'WAT', 'WEC', 'WFC', 'WELL', 'WST',
               'WDC', 'WU', 'WRK', 'WY',
               'WHR', 'WMB', 'WLTW', 'WYNN', 'XEL', 'XLNX', 'XYL', 'YUM', 'ZBRA', 'ZBH', 'ZION', 'ZTS']
    max_thread_workers = 50

    # If number of stocks is less than maxmium workers, then select the minimum number.
    workers = min(max_thread_workers, len(stock_names))
    with futures.ThreadPoolExecutor(workers) as executor:
        res = executor.map(query_the_iex_for, stock_names)

    if len(failed_queries) > 0:
        destination_path = 'failed_queries.txt'
        write_failed_queries_to(failed_queries, destination_path)