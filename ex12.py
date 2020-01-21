from sys import version_info,argv
from datetime import datetime
from calendar import monthrange
#Just trying to make sure we are on the right version of python
if version_info[0] < 3:
    exit("This script is intended for Python 3")
#Creating a function to check if the input we'll get is the way we want it
def checkif(day,month,year):
    if (0<day<32)and(0<month<13)and(0<year<10000):
        return (1)
    return(0)
#Getting some input from the user that will at least resemble a date in the form that we want and ignore any potentially accidental typos
#First check if it was given from the start
con = 1
try:
        day, month, year = [int(inpt) for inpt in argv[1].split("/")]
        if not(checkif(day, month, year)):
            raise ValueError("Input not in correct form")
        con = 0
except: print("Also correct usage: 'python3 ex12.py DD/MM/YYYY'")
#If not then just ask for it
while(con):
    try:
        day, month, year = [int(inpt) for inpt in input("Enter a valid date [1CE-9999CE] (DD/MM/YYYY) : ").split("/")]
        if checkif(day,month,year):
            break
        else: continue
    except ValueError: continue
    break
del con
#Get the two dates
dateinput = datetime(year, month, day)
datenow = datetime.today()
del day
#Finding the difference and showing it in DD/HH/SSSS
diffr = datenow - dateinput
print(abs(diffr.days),"/",diffr.seconds//3600,"/",diffr.seconds%3600)
#Showing the days in the month the user gave , at that year
print(monthrange(year, month)[1])
