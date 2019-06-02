import sys
import csv
from datetime import datetime


def idVal(id):
	if((id[0] == 0) or (int(id) < 100) or (int(id) > 999)):
		return False
	else:
		return True

# input the customer details q no 1


def customerDetails():
	customerFile = open('customers.csv', 'a')
	cDetails = []
	cName = input("Enter customers name::")
	cAddress = input("Enter customers Address::")
	i = 1
	while(1):
		if(i == 1):
			id = input("Enter the customer ID::")
		else:
			id = input(
				"Your ID is invalid. Please Try Again.(Type 'abort' to exit)::")
		if(id.lower() == 'abort'):
			sys.exit()
		elif(idVal(id) == True):
			break
		i = i+1
	eatOnlyHalal = input("Do you eat halal meat only(Yes/No)::").lower()
	cDetails = [cName, cAddress, id, eatOnlyHalal]
	print("Your data was recorded")
	print("**************************************************")
	for data in cDetails:
		customerFile.write(data)
		customerFile.write(',')
	customerFile.write('\n')
	customerFile.close()
	return id

# gets the fileOrder and save it in the book file



	
#gets the fileOrder and save it in the book file 

def flightOrder():
	book = []
	bookFile = open('bookedFile.csv', 'a')
	for i in csv.reader(open('flightInfo.csv')):
		print(i[0]+'\t'+i[1]+' to '+i[2])
	flightId = input('Enter the flight ID to be booked::')
	for i in csv.reader(open('flightInfo.csv')):
		if(i[0] == flightId):
			frm = i[1]
			to = i[2]
			date = i[4]
			times = i[5]

	cID = input("Enter the customer Id (If not registered type no) ")
	if(cID == 'no'):
		cID = customerDetails()

	for i in csv.reader(open('customers.csv')):
		if(i[2] == cID):
			Name = i[0]
			Address = i[1]
	book = [flightId, cID, Name, Address, frm, to, date, times]
	# writing in a file in csv file so that i can be traced in a list per line use csv.reader function to retrive data
	print("Your order was placed")
	#writing in a file in csv file so that i can be traced in a list per line use csv.reader function to retrive data
	for data in book:
		bookFile.write(data)
		bookFile.write(',')
	bookFile.write('\n')
# give summary infromation
	print("*******************************************************************************")
#give summary infromation 

def summaryinfo():
	print('********************************************************************')
	print("Summary Info of flight from to the destination")
	print('....................................................................')
	for i in csv.reader(open('flightInfo.csv')):
		print(i[1]+' to '+i[2])
	print('********************************************************************')
	print("Info about the no of flights and ")
	# for no of booked flights
	noInBookedFile=0
	flights=[]
	totalseats=[]
	for i in csv.reader(open('bookedFile.csv')):
		noInBookedFile=noInBookedFile+1
	for i in csv.reader(open('flightInfo.csv')):
		flights.append(i[0])
		totalseats.append(int(i[3]))
	for i in range(len(flights)):
		count=0
		for j in csv.reader(open('bookedFile.csv')):
			if(flights[i]==j[0]):
				count=count+1
		print('There are '+str(count)+' seats booked in the flight '+ flights[i] +' and remaining seats are '+str(totalseats[i]-count))
	print('****************************************************************************')
	print("TOTAL NO OF PEOPLE WHO EAT HALAL")
	for i in range(len(flights)):
		counts=0
		for j in csv.reader(open('bookedFile.csv')):
			if(flights[i]==j[0] and j[8]=='yes'):
				counts=counts+1
			
		print("The no of people who eat halal in flight "+flights[i]+' is '+str(counts))
	print("*******************************************************************************\n*****************************************")
	
def fIDVal(x):
	temp=x[:3]
	temp1=x[3:]
	if not (temp.isdigit()):
		return False
	if(temp1.isdigit()):
		return False
	else:
		return True
	
def createNewFlight():
	flightInfo=[]
	flightFile=open('flightInfo.csv','a')
	i=0;
	while(True):
		if(i==0):
			fID=input("Enter the flight Id (It must be of 3 letter following with a character) ")
			i=i+1
		else:
			fID=input("Invalid flight Id ( Enter valid ID It must be of 3 letter with a character")
		if(fIDVal(fID)):
			break
	frm=input("Where does the flight fly from::")
	to=input("Where does the flight fly to::")
	noofSeats=input("How seats are there in the flight::")
	date=input("Input the date of flight (YYYY/MM/DD)::")
	time=input("Input the time of flight (HH:MM:SS PM/AM)::")
	flightInfo=[fID,frm,to,noofSeats,date,time]
	
	for data in flightInfo:
		flightFile.write(data)
		flightFile.write(',')
	flightFile.write('\n')
	flightFile.close()
	print("Your Flight Was Created")
	print("*******************************************************************************\n*****************************************")

def customer_details():
	flag = 0
	cID = input("Enter customer ID: ")
	customer_info = csv.reader(open('customers.csv'))
	customer_flight_info = csv.reader(open('bookedFile.csv'))
	print(f"Information of Customer ID : {cID}")
	for data in customer_info:
		if data[2] == cID:

			print(
				f"Name: {data[0]} \nAddress: {data[1]} \nCustomer ID: {data[2]}")
			print(f"Customer eat halal meat: {data[3]}")

			for flight_info in customer_flight_info:
				if cID in flight_info:
					print(
						f"Flight ID: {flight_info[0]} \nDate: {flight_info[6]} \nBooked Time: {flight_info[7]}")
					break
		else:
			flag = flag + 1

	if flag != 0:
		print(f"Sorry! there is no deatils on Customer ID : {cID}")

# summary_info()
# flightOrder()
def cancel_booking():
	flight_info = csv.reader(open('flightInfo.csv'))
	booked_info = csv.reader(open('bookedFile.csv'))
	cID = input('Enter the customer ID: ')
	for flight_booked in booked_info:
		if cID in flight_booked:
			date = flight_booked[6]
			time = flight_booked[7]
			current_time = datetime.now().strftime('%H:%M')
			current_date = datetime.now().strftime("%Y/%m/%d")
			if date >= current_date:
				if int(time[0:2]) - int(current_time[0:2]) >= 2:
				# remove the line matching the cID in file 'bookedFile.csv' 
				# and increment the number of flight seat in file 'flightInfo.csv'
				# remove the key word pass after you add the logic to overwrite the csv file.
					pass

				elif int(time[0:2]) - int(current_time[0:2]) == 1:
					if time[3:] == current_time[3:]:
						# remove the line matching the cID in file 'bookedFile.csv' 
						# and increment the number of flight seat in file 'flightInfo.csv'
						# remove the key word pass after you add the logic to overwrite the csv file.
						pass
			else:
				print("Sorry, you can't cancel the flight now. Its too late for cancellation")

	# test reading files
# csv_file= open('customers.csv','r')

flag=1        
while(flag==1):
        choice=int(input("1.Add Customer Details\n2.Order a flight\n3.Summary Info\n4.Create New Flight\n5.Exit\nEnter your choice::"))
        if(choice==1):
                customerDetails()
        elif(choice==2):
                flightOrder()
        elif(choice==3):
                summaryinfo()
        elif(choice==4):
                createNewFlight()
        elif(choice==5):
                sys.exit()
        else:
                print("INVALID INPUT")
#summaryinfo()				
#summary_info()				

#flightOrder()


#customerDetails()


#test reading files 
# csv_file= open('customers.csv','r') 
# csv_reader=csv.reader(csv_file)
# for i in csv_reader:
# 	print(i)
