#!/usr/bin/python3

from finviz.helper_functions.save_data import export_to_db, export_to_csv
from finviz.screener import Screener
from finviz.main_func import *
from csv import reader
from twilio.rest import Client

ACCOUNT_SID = "AC2494707f1daaaf22ff9d002e00458c29"
AUTH_TOKEN = "faaae49027ebf2ba212d85785544dcfd"

#filters = ['exch_nasd','ta_change_u' ]  # Shows companies in the S&P500
filters = ['ta_change_u' ]  # Shows companies in the S&P500

print("Filtering stocks..")

#stock_list = Screener(filters=filters,order='-volume,-change',signal='Most Volatile')
stock_list = Screener(filters=filters,order='-volume',signal='ta_mostvolatile')

stock_list.get_ticker_details()

# Export the screener results to CSV file
stock_list.to_csv('jimmy.csv')

result = ['These are stocks based on highest % change since this morning, GREEN stocks only']
d = {}

def main():
	with open('jimmy.csv', 'r') as read_obj:
		head = [next(read_obj) for x in range(10)]
		csv_reader = reader(head)
		for row in csv_reader:
                    print (row[1],row[8],row[9],row[10])
                    result.append(row[1])

def send_mess_twlio(message):
	numbers = ['+15108629817','+14087574675','+14088066239','+14087996321','+15103632391','+19728380311','+15104023623']
	#numbers = ['+15108629817']
	client = Client(ACCOUNT_SID, AUTH_TOKEN)
	for number in numbers:
        	client.messages.create(
                	to=number,
                	from_="426366",
                	body=message,
            )
if __name__ == "__main__":
	main()
	if len(result)!=0:
		send_mess_twlio("\n".join(result))
