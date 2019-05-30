import sys
import csv

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
	
	return id

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
			time=i[5]		
	
	cID=input("Enter the customer Id (If not registered type 'No') ")
	if(cID.lower()=='no'):
		cID=customerDetails()
	for i in csv.reader(open('customers.csv')):
		if(i[2]==cID):
			Name=i[0]
			Address=i[1]
	book=[flightId,cID,Name,Address,frm,to,date,time]
	print(book)
	for data in book:
		bookFile.write(data)
		bookFile.write(',')
	bookFile.write('\n')

def summary_info():
	flag = 0
	cID = input("Enter customer ID: ")
	customer_info = csv.reader(open('customers.csv'))
	customer_flight_info = csv.reader(open('bookedFile.csv'))
	print(f"Information of Customer ID : {cID}")
	for data in customer_info:
		if data[2] == cID:
			print(f"Name: {data[0]} \nAddress: {data[1]} \nCustomer ID: {data[2]}")
			print(f"Customer eat halal meat: {data[3]}")				
			
			for flight_info in customer_flight_info:
				if cID in flight_info:
					print(f"Flight ID: {flight_info[0]} \nDate: {flight_info[6]} \nBooked Time: {flight_info[7]}")
					break
		else:
			flag = flag + 1
	
	if flag !=0:
		print(f"Sorry! there is no deatils on Customer ID : {cID}")

				
summary_info()				
#flightOrder()
#customerDetails()
#test reading files 
# csv_file= open('customers.csv','r') 
# csv_reader=csv.reader(csv_file)
# for i in csv_reader:
# 	print(i)