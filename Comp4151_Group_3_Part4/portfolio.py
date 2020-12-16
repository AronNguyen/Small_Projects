import requests
import pandas
import datetime
import os
import csv
import math
import pandas_datareader.data as web

class Portfolio:

    """
    Variables stocks and allocation were initialize
    """
    stocks = {}
    allocation = []
    capital_allocations=[]

    """
    add_stock_symbol: adds the stock symbol into the stock dictionary
    check_stock_symbol: returns a T or F depending if the key exist
    """
    def add_stock_symbol(self, stock_symbol):

        self.stocks[stock_symbol] = 1

    def check_stock_symbol(self, stock_symbol):

        if stock_symbol in self.stocks:
            return True
        else:
            return False

    """
    download_stock_summary: First checks if a StockSummary csv file exist
                            If it doesnt it creates one in the current directory
                            Makes a requests to from yahoo finance and writes the html file as a text file
                            Opens the new csv file and adds in PE_ratio and market_cap while cleaning it up
                            i.e. strips the letters off and multiply by whatever letter was strip
    """
    def download_stock_summary(self, stock_symbol):

        if not os.path.isfile('StockSummary.csv'):
            df = pandas.DataFrame(columns=['stock_symbol', 'PE_ratio', 'market_cap'])
            df.to_csv('StockSummary.csv', index=False)

        r = requests.get(f'https://finance.yahoo.com/quote/{stock_symbol}?p={stock_symbol}')
        temp = open(f'yf_{stock_symbol}.html', 'w')
        temp.write(r.text)
        temp.close()

        df = pandas.read_html(r.text)
        with open('StockSummary.csv', 'a') as csvfile:

            df_stock_sum = pandas.read_csv('StockSummary.csv')
            if stock_symbol not in df_stock_sum.values:

                csvwriter = csv.writer(csvfile)
                mk_cap = -1
                if df[1].iloc[0][1][-1] == 'T':

                    mk_cap =  float(df[1].iloc[0][1].strip('MBT')) * math.pow(10, 12)
                elif df[1].iloc[0][1][-1] == 'B':

                    mk_cap =  float(df[1].iloc[0][1].strip('MBT')) * math.pow(10, 9)
                elif df[1].iloc[0][1][-1] == 'M':

                    mk_cap =  float(df[1].iloc[0][1].strip('MBT')) * math.pow(10, 6)
                else:

                    mk_cap =  float(df[1].iloc[0][1].strip('MBT'))
                csvwriter.writerow([stock_symbol, float(df[1].iloc[2][1]), mk_cap])

    """
    initialize_stock: assigns market_cap and pe_ratio
    """
    def initialize_stock(self, company, stock_symbol, file_name):

        if self.check_stock_symbol(stock_symbol):
            self.stocks[stock_symbol] = Stock(company, stock_symbol)
            df = pandas.read_html(file_name)
            self.stocks[stock_symbol].market_cap = float(df[1].iloc[0][1].strip('MBT'))
            self.stocks[stock_symbol].pe_ratio = float(df[1].iloc[2][1])
        else:
            self.check_stock_symbol(stock_symbol)

    """
    add_stock_price: Gets the stock prices from a starting date to and end date
                     Also initializes the volatility and ROI of the stock
    """
    def add_stock_price(self, stock_symbol, start_date, end_date):

        df = web.DataReader(stock_symbol, 'yahoo', start_date, end_date)
        self.stocks[stock_symbol].prices = df
        df.to_csv('StockPrices' + f'\{stock_symbol}.csv')

        self.volatility(stock_symbol, start_date, end_date)
        self.ROI()

    '''
    stock_ROI: Then it calculates  ROI and returns the value rounded to 2 trailing
    '''
    def stock_ROI(self, stock_symbol, start_date, end_date):

        df = self.stocks[stock_symbol].prices

        start_close = df.loc[start_date][3]
        end_close = df.loc[end_date][3]

        ROI = ((end_close-start_close)/start_close) * 100

        return round(ROI, 2)

    """
    allocate: calculates the total ROI and volality base on the percentages given
    """
    def allocate(self, list):

        for i in list:
            if i not in self.allocation:
                self.allocation.append(i)
        total_ROI = 0
        total_vol_p1 = 0
        total_vol_p2 = 0
        n = 0

        for i in self.stocks:

            # total_ROI += self.stocks[i].ROI * self.allocation[n][1]
            self.stocks[i].weighted_ROI= self.stocks[i].ROI * self.allocation[n][1]

            # total_vol_p1 += self.stocks[i].volality[0] * self.allocation[n][1]
            self.stocks[i].weighted_vol = self.stocks[i].volality[0] * self.allocation[n][1]

            total_vol_p2 += self.stocks[i].volality[1] * self.allocation[n][1]
            n+=1

        # return (total_ROI, (total_vol_p1, total_vol_p2))

    """
    ROI: calls stock ROI with a given start and end date
         Then saves it to the stock class ROI
    """
    def ROI(self):

        for i in self.stocks:

            # roi_temp = self.stock_ROI(i, '01-02-2019', '10-20-2020')
            df = self.stocks[i].prices

            start_date = df.index.strftime('%Y-%m-%d')[0]
            end_date = df.index.strftime('%Y-%m-%d')[-1]
            roi_temp = self.stock_ROI(i, start_date, end_date)

            self.stocks[i].ROI = roi_temp

    """
    volatility: Calcuates the volatillity in two different ways
                1st by squared average
                2nd by absolute max
                returns a tuple with index[0] and index[1] being squared average and absolute max
    """
    def volatility(self, stock_symbol, start_date, end_date):

        if type(start_date) != str:
            start_date = start_date.strftime('%Y-%m-%d')
            end_date = end_date.strftime('%Y-%m-%d')

        volatility = []
        df = self.stocks[stock_symbol].prices
        df = df[start_date:end_date]
        open = df['Open'].tolist()
        close = df['Close'].tolist()

        n = len(open)
        for i in range(n):
            vol = close[i] - open[i]
            volatility.append(vol)

        squared_volatility = sum([ x*x for x in volatility]) / len(volatility)

        self.stocks[stock_symbol].volality = (squared_volatility,
                                              max([ abs(x) for x in volatility])
                                             )
        # return squared_volatility, max([ abs(x) for x in volatility])

    def allocation_manager(self,L, cap):
        symbols=L[0]
        allocations=L[1]
        err=''
        cap_list=[]
#
        if len(symbols)!=len(allocations):
            print("lists given are of different sizes")
            return None
        count=0
        for x in range(len(allocations)):
            count+=allocations[x]

        if(count > 1):

            err = 'Allocations Greater than 1'
            print(allocations)
            # cap_list=[]
            return (err, cap_list)

        f = open("my_portfolio.csv",'w')
        f.close()

        for x in range(len(symbols)):
            self.add_stock_portfolio(symbols[x],allocations[x])

        if(cap > 0):
            # print(self.distribute_capital(cap, allocations))
            cap_list = self.distribute_capital(cap, allocations)
        # self.capital_allocations=[]
        return (err, cap_list)


    #code written by collin
    """
    adds stock to portfolio given stock symbol
    stock allocation needs to be managed in allocation manager method
    """
    def add_stock_portfolio(self,symb,allocation):

        #creates dataframe to be appended
        stock = {'stock_symbol':[symb],'allocation':[allocation]}
        stock_df = pandas.DataFrame(stock)

        #reads from csv file to check for stock symbol and updates
        if(os.path.isfile("my_portfolio.csv")==False):
            f = open("my_portfolio.csv",'w')
            f.close()

        #checks to see if file is empty
        filesize = os.path.getsize("my_portfolio.csv")
        if (filesize == 0):
            stock_df.to_csv("my_portfolio.csv",index=False)

        #need to change this bit to fit actual function
        else:
            df = pandas.read_csv("my_portfolio.csv")
            stock_list = df["stock_symbol"].tolist()
            index=0
            found=False
            while index < len(stock_list): #searches list for position of stock if it exists
                if (stock_list[index] == symb):
                    found=True
                    break
                index=index+1
            if(found==True):
                df.iloc[index].iloc[1]=allocation #updates allocation if changed
            else:
                stock_df=stock_df.append(df,ignore_index = True)#appends the new stock to list if absent
            stock_df.to_csv("my_portfolio.csv",index=False)#new data overwrites old csv data

    # code by Stephen Hooker
    '''
    takes capital to be added, and the list of allocations
    then makes a list of how the capital will be distributed
    then returns the list of the allocated capital
    '''
    def distribute_capital(self, cap, allo):
        self.capital_allocations = [0] * len(allo)
        for i in range(len(allo)):
            self.capital_allocations[i] = (allo[i] * cap)
        return self.capital_allocations


class Stock:

    market_cap = -1
    pe_ratio = -1
    prices = -1
    volality = -1
    ROI = -1
    weighted_ROI = -1
    weighted_vol = -1

    def __init__(self, company, stock_symbol):
        self.company = company
        self.stock_symbol = stock_symbol
