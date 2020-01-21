from sys import version_info,argv
#Just trying to make sure we are on the right version of python
if version_info[0] < 3:
    exit("This script is intended for Python 3")
#Getting some input from the user that will at least resemble a date in the form that we want and ignore any potentially accidental typos
#First check if it was given from the start
con = 1
try:
    cc = [int(inpt) for inpt in list(argv[1]) if inpt.isdigit()][::-1]
    if not len(cc)==16:
        raise ValueError("Input not in correct form")
    con = 0
except: print("Also correct usage: 'python3 ex12.py XXXXXXXXXXXXXXXX' (X are digits)")
#If not then just ask for it
while(con):
    try:
        #getting a reverse list of the 16 digits we want, ignoring everything else
        cc = [int(inpt) for inpt in list(input("Your 16 digit Credit Card nember : ")) if inpt.isdigit()][::-1]
        if not len(cc)==16: continue
    except ValueError: continue
    break
del con
# Now we:
# 1) Double the value of every second digit
# 2) Replace every second digit with the sum of their integer division and modulo with 10
#    (pretty much geting the 2 digits of the maximum 2 digit number)
#    (it is only done once since a digit can be up to 9, so their double can be up to 18 -> 1+8=9 )
# 3) Take the total of all the first digits and the sum of of all the first digits added together
# 4) If the total modulo 10 is equal to 0, then the number is valid,otherwise it is not valid
# All in one line
# (I know this ain't lisp,but this looks better to me because it conveys more in a fast and digestable way,
#  without clutter,at least for me, but i wrote these comments just in case.)
cc = ((sum(sum(divmod(2*x,10)) for x in cc[1::2]) + (sum(cc[0::2]))) % 10 == 0)
#Telling the user if the credit card number is valid or not.
if cc:
    exit("Valid")
exit("Invalid")
