# this file is a toy controller for csv offline db

import time
from Historic_Crypto import HistoricalData
import pandas as pd


def getFrame(coin, grain, date):
    return HistoricalData(coin,grain,date).retrieve_data()

def date2timestamp(date):
    strp = time.mktime(time.strptime(date, "%Y-%m-%d %H-%M-%S"))
    return strp

def timestamp2date(ts):
    return time.strftime("%Y-%m-%d %H-%M-%S", ts)

def getFromCsv(csvname):
    return pd.read_csv(csvname)

####################
#
# DB PARAMS -
# SHOULD ADD AN ARG PARSER 
# to automate the procedure
#
####################
coin1 = "BTC-USD"
grain = 86400
date = "2018-01-01-00-00"
end = "2021-05-07-00-00"

# a very ugly local path
# db name
# based on param values
csvname = "../data/"+coin1+"/"+str(grain)+"/from_"+int(date2timestamp(date))+"_to_"+int(date2timestamp(end))+".csv"

###################
#
# FUNCTIONS AVAILABLE
#
###################

######################################
# downloads a requested db to csv file
get_db = True

######################################
# checks if db has missing data
check_db = False




# saves coinmarketcap to local db
if get_db:
    dataFrame = getFrame(coin1, grain, date, end)
    dataFrame.to_csv(csvname)


# not finished, checks if db has "holes"
# using dates is a mess, using timestamps is easy
# [TO DO]
if check_db:
        dataFrame = getFromCsv(csvname)
        times = dataFrame["time"].values
        for idx, time in enumerate(times[1 :]):

            print(time)
            print(date2timestamp(time))
            raise NotImplementedError


# this class can incorporate some db functionalities
# it is currently unused
class coinContainer:

    def __init__(self, coin = None,
                        grain = 86400,
                        start = '2020-04-23-00-00',
                        end = None):
    
        if coin != None:
            self.dataFrame = getFrame(coin, grain, start, end)

    def frame2csv(self, csvName):
        self.dataFrame.to_csv(csvName)

    def csv2frame(self, csvName):
        self.dataFrame = getFromCsv(csvName)    
    
    # indexed series as numpy array
    # now these get functions should have time windows enabled
    def getLow(self):
        return self.dataFrame["low"].values
        
    def getHigh(self):
        return self.dataFrame["high"].values

    def getOpen(self):
        return self.dataFrame["open"].values

    def getClose(self):
        return self.dataFrame["close"].values

    def getTime(self):
        return self.dataFrame["time"].values

    def getIndex(self):
        return self.dataFrame.index.values

    def getFrame(self):
        return self.dataFrame