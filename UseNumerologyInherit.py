#Name: Katlyn Lucis
#Assignment: Numerology Inheritance
#Reflection:  Share what you liked about this assignment:  I enjoyed that this built off of a previous assignment.  It was
#             nice to see something were learning applied to work we've already done, as it makes it easier to understand how it
#             enhances the previous code rather than just making something new.  I really liked how clean the LifePathDescription
#             turned out in the end.

#             Share what you struggled with:  Importing the class from a separate file instead of having it at the top of the code.

#             In your own words describe how deocration works and how does it help coders write better code: decorators automatically add more
#             functionality to a function passed to it by adding repeated sections to the start or end of the code.  They can simplify
#             and neaten up code by storing all of the repeated portions in one area.  This makes the code easier to change if there
#             is something in the wrapper that has to be altered, as it will change it on all subsequently decorated functions.
#             This also makes writing code faster since you don't have to rewrite the same lines over and over.  One other benefit is
#             minimizing errors that may occur when repetively typing the duplicate code instead of using the decorator over the function.

#             Share exactly 2 things you learned on this assignment:
#             1. How to import a class from a separate file!
#             2. Learning and implementing inheritence.  It is a relatively simple code line that does so much work automatically.

import NumerologyLifePathDetails
import re
from datetime import datetime

def main():
    sName = ("")
    #Name input ensures the field is not blank.
    while sName == (""):
        sName = input("Enter your full name: ")

    #Date passed to validating functions.  If both return true, the program will continue.
    while True:    
        sDOB = input("Enter your full date of birth (mm/dd/yyyy): ")
        if isValidDateFormat(sDOB) and isValidDate(sDOB):
            break
            
    new_client = NumerologyLifePathDetails.NumerologyLifePathDetails(sName,sDOB)

    #All values output to print.
    print(new_client)
    
    print('\n','\n')
    
    print(f"Client Name: {new_client.Name}")
    print(f"Client DOB: {new_client.Birthdate}")
    print(f"Life Path: {new_client.LifePath}")
    print(f"Attitude: {new_client.Attitude}")
    print(f"Birthday: {new_client.BirthDay}")
    print(f"Personality: {new_client.Personality}")
    print(f"Power Name: {new_client.PowerName}")
    print(f"Soul: {new_client.Soul}")
    print(f"Your life path number is {new_client.LifePath} which means you are~\n"
          f"{new_client.LifePathDescription}")
    

#Validates the date format is 2 numbers, a dash or slash, 2 numbers, a dash or slash, and 4 more numbers.
def isValidDateFormat(sDateToTest: str) -> bool:
        return bool(re.match(r'^\d{2}[-/]\d{2}[-/]\d{4}$', sDateToTest))

#Validates the date is an actual real day, including leap year days.
def isValidDate(sDateToTest: str) -> 'class datetime.datetime':
    sDateToTest = sDateToTest.replace("/","").replace("-","")
    try:
        datTest =  datetime.strptime(sDateToTest, '%m%d%Y') 
        return True
    except:
        return False

main()
