import pandas as pd
import urllib2

def construct_futures_symbols(symbol, start_year=2010, end_year=2015):
    futures = []
    months = 'HMUZ'  # March, June, September and December delivery codes
    for y in range(start_year, end_year+1):
        for m in months:
            futures.append("%s%s%s" % (symbol, m, y))
    return futures


def download_contract_from_quandl(contract, auth_token, dl_dir):
    api_call_head = "https://www.quandl.com/api/v3/datasets/CME/%s.csv" % contract
    params = "?&api_key=%s&sort_order=asc" % auth_token
    
    data = urllib2.urlopen("%s%s" % (api_call_head, params)).read()
    
    fc = open('%s/%s.csv' % (dl_dir, contract), 'w')
    fc.write(data)
    fc.close()


def download_historical_contracts(symbol, auth_token, dl_dir, start_year=2010, 
        end_year=2015):
    contracts = construct_futures_symbols(symbol, start_year, end_year)
    for c in contracts:
        download_contract_from_quandl(c, auth_token, dl_dir)
        
download_historical_contracts(
    'ES',
    'TVyxcTwsaXs2SnBXCEz2',
    '/Users/connorstauffer/Trading/quandl/futures/ES'
)