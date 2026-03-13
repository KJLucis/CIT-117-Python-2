#Name: Katlyn Lucis    02/05/2026
#CIT-117-D02 Python Programming 2
#Assignment:  Password Validator
#Reflection:  Share what you Liked about this assignment:  I enjoyed that this assignment felt like pieces of a puzzle to figure out.
#               I felt very accomplished after getting each function to work properly.
#             Share what you struggled with: The most difficult function for me to figure out was repeatCheck. Never having used
#               dictionaries before, it was a big learning experience.
#             How did you write your code to be efficient and reduce redundancy? I try to reduce redundancy by trying to minimize steps as much as possible.
#               When doing the functions, I would approach with an idea, and then prune down the lines.  Where could this be converted inside of the print line?
#               Are there any of these steps that aren't quite needed?  I get the code to work first and then modify it from there.
#             Share exactly 2 things you learned on this assignment: 
#             1. I learned the various methods for manipulating a dictionary.
#             2. I had never used the any() function before.  I changed the specialCheck function to make it more concise using any().
#   2/15/2026 - edited standard checks to be in one function. Lower, upper, number, and special now found under the charCheck function.
#             - removed all unnecissary variable assignments.
#             - simplified error validation check to a single equation containing all functions.(removed 2/16)
#   2/16/2026 - coverted logic to boolean, simplifying more code.
#   2/18/2026 - incorporated all functions into charCheck.

#defining main function
def main():

    #receive input for user name and passwords.
    sNameKJL = input("Enter full name such as John Smith: ")

    #Initiate the loop.
    while True:
        sPasswordKJL = input("Enter new password: ")
        #Each validation function run.  If a false is returned the loop repeats.
        if charCheck(sNameKJL,sPasswordKJL):
            #If true is returned, the while loop will break and the code will validate.
            break
        print(" ")    
        
    #If the all values are "True", the loop will break and the password will validate.    
    print("Password is valid and OK to use.")

#charCheck function defined.  Boolean variables created to validate checks. 
def charCheck (sNameKJL,sPasswordKJL):
    dictPasswordKJL = {}
    bIsUpperKJL = bIsLowerKJL = bIsNumberKJL = bIsSpecialKJL = False
    #The password is iterated over to search for upper case, lower case, numeric, and special characters.
    for sLetter in sPasswordKJL:
        if sLetter.isupper():
            bIsUpperKJL = True
        elif sLetter.islower():
            bIsLowerKJL = True
        elif sLetter.isnumeric():
            bIsNumberKJL = True
        elif sLetter in ["!","@","#","$","%","^"]:
            bIsSpecialKJL = True
        #Dictionary filled with the letter as the key, and the number of times the letter is used as the value.
        if sLetter.lower() not in dictPasswordKJL:
            dictPasswordKJL[sLetter.lower()] = 1
        else:
            #If the key of the letter already exists in the dictionary, its value is increased by 1.
            dictPasswordKJL[sLetter.lower()] += 1
    #error message printed for any checks that did not pass (returned false)
    if not (bool(len(sPasswordKJL) >= 8 and len(sPasswordKJL) <= 12)):
        print("Password must be between 8 and 12 characters.")
    if (sPasswordKJL.lower().startswith("pass")):
        print("Password can't start with Pass.")
    if not bIsUpperKJL:
        print("Password must contain at least 1 uppercase letter.")
    if not bIsLowerKJL:
        print("Password must contain at least 1 lowercase letter.")
    if not bIsNumberKJL:
        print("Password must contain at least 1 number.")
    if not bIsSpecialKJL:
        print("Password must contain 1 of these special characters: ! @ # $ % ^")
    if (sNameKJL[0].lower()+sNameKJL[sNameKJL.find(" ")+1].lower()) in sPasswordKJL.lower():
        print("Password must not contain user initials.")
    #Created a variable to control the error heading through iterations as well as the return value.
    bHeadingKJL = True
    #The previously created dictionary is iterated over to identify duplicates, which are then printed.
    for sLetter,iTimes in dictPasswordKJL.items():
        if iTimes > 1:
            if bHeadingKJL == True:
                print("These characters appear more than once:")
                #The heading variable is changed to false to prevent printing more than once during iterations.
                bHeadingKJL = False
            print(sLetter,": ",iTimes," times")
     #Boolean value returned to main function.  Will only return true if all values return true.
    return ((bool(len(sPasswordKJL) >= 8 and len(sPasswordKJL)) <= 12) and (not(sPasswordKJL.lower().startswith("pass")))
            and (not (sNameKJL[0].lower()+sNameKJL[sNameKJL.find(" ")+1].lower()) in sPasswordKJL.lower())
            and bIsUpperKJL and bIsLowerKJL and bIsNumberKJL and bIsSpecialKJL and bHeadingKJL == True)
        
#Calls the main function to run.
main()
