import sys
import csv
import time as t
def idVal(id):
	if((id[0]==0) or (int(id)<100) or (int(id)>999)):
		return False
	else:
		return True
#input the customer details q no 1
def customerDetails():
	customerFile=open('customers.csv','a')
	cDetails=[]
	cName=input("Enter customers name::")
	cAddress=input("Enter customers Address::")
	i=1
	while(1):
		if(i==1):
			id=input("Enter the customer ID::")
		else:
			id=input("Your ID is invalid. Please Try Again.(Type 'abort' to exit)::")
		if(id.lower()=='abort'):
			sys.exit()
		elif(idVal(id)==True):
			break
		i=i+1
	eatOnlyHalal=input("Do you eat halal meat only(Yes/No)::").lower()
	cDetails=[cName,cAddress,id,eatOnlyHalal]
	for data in cDetails:
		customerFile.write(data)
		customerFile.write(',')
	customerFile.write('\n')
	customerFile.close()
	return id
#gets the fileOrder and save it in the book file 
def flightOrder():
	book=[]
	bookFile=open('bookedFile.csv','a')
	for i in csv.reader(open('flightInfo.csv')):
		print(i[0]+'\t'+i[1])
	flightId=input('Enter the flight ID to be booked::')
	for i in csv.reader(open('flightInfo.csv')):
		if(i[0]==flightId):
			frm=i[1]
			to=i[2]
			date=i[4]
			times=i[5]		
	
	cID=input("Enter the customer Id (If not registered type no) ")
	if(cID=='no'):
		cID=customerDetails()
	
	for i in csv.reader(open('customers.csv')):
		if(i[2]==cID):
			Name=i[0]
			Address=i[1]
	book=[flightId,cID,Name,Address,frm,to,date,times]
	print(book)
	#writing in a file in csv file so that i can be traced in a list per line use csv.reader function to retrive data
	for data in book:
		bookFile.write(data)
		bookFile.write(',')
	bookFile.write('\n')
#give summary infromation 
def summaryinfo():
	print('********************************************************************')
	print("Summary Info of flight from to the destination")
	print('....................................................................')
	for i in csv.reader(open('flightInfo.csv')):
		print(i[1]+' to '+i[2])
	print('********************************************************************')
#summaryinfo()
flightOrder()
#customerDetails()


#test reading files 
# csv_file= open('customers.csv','r') 
# csv_reader=csv.reader(csv_file)
# for i in csv_reader:
# 	print(i)