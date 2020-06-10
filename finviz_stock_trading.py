#!/usr/bin/python3

from finviz.helper_functions.save_data import export_to_db, export_to_csv
from finviz.screener import Screener
from finviz.main_func import *
from csv import reader
from twilio.rest import Client

ACCOUNT_SID = "------------------------------"
AUTH_TOKEN = "-------------------------------"

filters = ['exch_nasd']  # Shows companies in the S&P500

print("Filtering stocks..")

#stock_list = Screener(filters=filters,order='-volume,-change',signal='Most Volatile')
stock_list = Screener(filters=filters,order='-change',signal='Most Volatile')

stock_list.get_ticker_details()

# Export the screener results to CSV file
stock_list.to_csv('jimmy.csv')

result = []

def main():
	with open('jimmy.csv', 'r') as read_obj:
		head = [next(read_obj) for x in range(10)]
		csv_reader = reader(head)
		for row in csv_reader:
			result.append(row[1])
	#send_mess_twlio(result)
	print(result)
	return result
	
def send_mess_twlio(message):
	numbers = ['-----------------------------']
	client = Client(ACCOUNT_SID, AUTH_TOKEN)
	for number in numbers:
        	client.messages.create(
                	to=number,
                	from_="-----",
                	body=message,
            )
if __name__ == "__main__":
	main()
	if len(result)!=0:
		send_mess_twlio("\n".join(result))
