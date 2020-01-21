from sys import argv, version_info
from re import sub
#Just trying to make sure we are on the right version of python
if version_info[0] < 3:
    exit("This script is intended for Python 3")
#Creating a function to get the txt that will be given
def opentxt(text):
    try:
        with open(text, "r") as file:
            text = file.read() + "69"
    except FileNotFoundError:
        return("")
    except IOError:
        return("")
    return (text)
#Making a function so we won't repeat the same message
told=1
def tell(told):
    if told:
        print("Also correct usage: 'python3 ex1.py .../whatever.txt Q1 Q2' Q1,Q2=(Yes/No/True/False)")
        return 0
    return told
#Checking if a txt was given
con=1
try:
    txt = argv[1]
    if not txt.endswith(".txt"):
        raise ValueError("Input not in correct form")
    txt = opentxt(txt)
    if not txt:
        raise ValueError("Input not in correct form")
    con=0
except:told=tell(told)
#Checking if our questions for later were answered beforehand
Y=""
try:
    Y = argv[2]
except:told=tell(told)
G=""
try:
    G = argv[3]
except:told=tell(told)
del told
#If not then just ask for it
while(con):
    try:
        txt = input("Enter a valid .txt (and the correct directory to it if needed): ")
        if not txt.endswith(".txt"):
            continue
        txt = opentxt(txt)
        if not txt:
            continue
    except ValueError: continue
    break
del con
#Transforming the text into a clean list
txt = sub("[\s\W\d]", "_", txt).split("_")
txt = list(filter(None, txt))
vowels = ["a","e","i","o","u"]
#Getting some inputs from the user that will at least resemble something of an agreement or disagreement to our question and ignore any accidental typos
def checkin(qstn,add,vowels,aargv):
    check = ["true","yes","false","no"]
    if any(x in aargv.casefold() for x in check):
        answer=aargv
    else:
        while(1):
            what=input(qstn+" Yes or No? True or False?")
            if not(any(x in what.casefold() for x in check)): continue
            break
        answer=what
    if any(x in answer.casefold() for x in check[:2]):
        vowels += add
checkin("Is 'Y' a vowel?",["y"],vowels,Y)
#Asking if greek is also to be considered in this because I wasn't sure
greek = ["α","ε","η","ι","ο","ω","υ","ά","έ","ή","ί","ό","ώ","ύ","ϊ","ΐ","ϋ","ΰ"]
checkin("Should greek be taken into consideration?",greek,vowels,G)
del greek,G,Y
#Find the score of every word
bad = ["f","c","k","r"]
def words(text):
    score=0
    for x in vowels:
        text = sub(x, "", text.casefold())
    for x in text:
        if any(x in y for y in bad):
            score-=1
        else:
            score+=1
    if score<0:
        return("κακή")
    return("καλή")
#Present every word and it's score in dicttionary form, so the user can understand, read, change and use it, all with ease
print ({i : words(i) for i in txt})
