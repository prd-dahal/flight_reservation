import sys
import csv
def idVal(id):
	if((id[0]==0) or (int(id)<100) or (int(id)>999)):
		return False
	else:
		return True

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



csv_file= open('flightInfo.csv','r') 
csv_reader=csv.reader(csv_file)
for i in csv_reader:
 	if (i[0]=='kathmandu'):
 		i[2]='hello world'
 		print("hello")
for i in csv_reader:
	print(i)