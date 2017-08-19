from yahoo_finance import Share 	#https://pypi.python.org/pypi/yahoo-finance
import urllib2
import time
from datetime import datetime, date
import calendar
import pytz



def stockChecking():
	stcokSym = raw_input("\nPlease enter a symbol:\n")
	stock=Share(stcokSym)
	#handle error, #input the correct name
	if stock.get_name() is None:
		print("wrong stock symbol!")
		stockChecking()
	#Current local time;
	strd=calendar.day_name[date.today().weekday()] #Monday
	tz = pytz.timezone('PST8PDT')	
	pacific_now = datetime.now(tz)
	#print(pytz.all_timezones) CHECK THE TIME ZONE NAMES
	#tz = pytz.timezone('Asia/Shanghai')	#convert to local time zone
	#d1x = tz.localize(datetime.fromtimestamp(int(time.time())))
	#print(d1x)	#"2017-05-01 00:24:30+08:00"
	#print(d1x.tzinfo) #'Asia/Shanghai'
	#print(d1x.tzname()) # "CST"
	print("\n" + strd[0:3] + time.strftime(" %b %d %H:%M:%S ", pacific_now.timetuple() ) 
							+ pacific_now.tzname() + time.strftime(" %Y", pacific_now.timetuple()) + " (Current Local Time)\n")  #Mon Oct 10 17:23:48 PDT 2016
	#print("Current Time: " + strd[0:3] + " " + time.strftime("%Y %b %d %H:%M:%S : %Z ", time.localtime() ) + " ")  
 	
 	#stock symbol to company name
 	print(stock.get_name() + " (" + stcokSym +")\n") #Full name of the company $ Adobe Systems Incorporated (ADBE)
	print(stock.get_price() + " " + stock.get_change() + " " +  stock.get_percent_change() +"\n")# Stock price
	stockChecking()

 
#handle error, #check network
def internet_on():
    try:
        urllib2.urlopen('http://172.217.5.110', timeout=1)	#One of the IP of google.com
        return True
    except urllib2.URLError as err: 
        return False


if __name__ == '__main__':
	internet = internet_on()
	if internet:
		stockChecking()
	else:
		print("no network connection")


# import requests
# def get_symbol(symbol):
#     url = "http://d.yimg.com/autoc.finance.yahoo.com/autoc?query={}&region=1&lang=en".format(symbol)

#     result = requests.get(url).json()

#     for x in result['ResultSet']['Result']:
#         if x['symbol'] == symbol:
#             return x['name']


# company = get_symbol("MSFT")

# print(company)