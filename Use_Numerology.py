#Name: Katlyn Lucis
#Assignment: Numerology Classes
#Reflection:  Share what you liked about this assignment:  The idea of Numerology is fun, sort of like Astrology. I went to
#             look up what each number was to add it to the assignment, but saw that it was part of the next assignment anyway.

#             Share what you struggled with:  The date validation was interesting to wrap my head around but the example
#             shared with the class was very helpful in presenting a module I wasnt familiar with.

#             Think back on a previous assignment. How could it be rewritten to use Python classes?  The real estate analyzer
#             could create a Real_Estate_Group class.  The __init__ would receive the csv file and assign all of the attributes
#             such as minimum, maximum, sum, and so on.  The class would accept (self, csv_file_name) so multiple groups
#             could be easily analyzed by simply entering the file to be processed.

#             Share exactly 2 things you learned on this assignment:
#             1. I learned how to use the @property decorator to easily assign attributes to variables of an object and help hide their
#                content while making them simpler to access from the program importing the class.
#             2. I learned more about the __init__ portion of when an object is created.  When first reading about it,
#                I only thought about it as the initilizing variables, but did not think to add more than just the passed values,
#                such as calculations for other variables that would be crucial for the object.
import numerology
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
            
    new_client = numerology.Numerology(sName,sDOB)

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
