import random
from datetime import date
CN= input("Enter the Name of the customer: ")
SN= int(input("Enter the Service Number: "))
MN= int(input("Enter the Mobile Number: "))
P= int(input("Enter the Previous Month Reading: "))
C= int(input("Enter the Current Month Reading: "))
payment= input("Enter the Payment type (Cash/Card): ")
num= random.randint(1000000000, 9999999999)
date= date.today()


print("\t\t\t\tTAMILNADU ELECTRICITY BOARD")
print("\t\t\t\t\t\t\t\t ELECTRICITY BILL")
print("********************************************************************************************************************")
print("NAME:", CN,"","","\t\t\t\t\t\t\t\tPAYMENT TYPE:", payment)
print("SERVICE NUMBER:", SN,"","","\t\t\t\t\t\t\tMOBILE NUMBER:", MN)
print("PREVIOUS MONTH READING:", P,"","","\t\t\t\t\t\tCURRENT MONTH READING:", C)
print("BILL NUMBER:", num,"","","\t\t\t\t\t\t\t\tDATE:", date)
print("*********************************************************************************************************************")
print("TOTAL UNITS CONSUMED:", C-P,"","","TOTAL AMOUNT TO BE PAID:", (C-P)*4.5)
print("*********************************************************************************************************************")
print("THANK YOU FOR USING TAMILNADU ELECTRICITY BOARD")