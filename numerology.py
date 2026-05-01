#Name: Katlyn Lucis
#Assignment: Numerology Classes
#See accompanying Use_Numerology.py for reflections.
#Define the Numerology class.  All the calculations are done during initialization and assigned
#to private variables to be called later by the properties of the class.
class Numerology:
    #The name and date of birth are received from the input
    def __init__(self, sName, sDOB):
        self.__name = sName
        self.__DOB = sDOB

        #DOB input removes spaces or dashes, and is turned to a list.
        #The string list is converted to int for computation purposes.
        #LifePath is found finding the sum of the DOB integers, until the result is less than 9 (simplify function).
        sDOBList = list(self.__DOB.replace("/","").replace("-",""))
        iDOBList = [int(number) for number in sDOBList]
        self.__LifePath = self.simplify(iDOBList)
        
        #BirthDay is found by passing the days from the input to simplify().
        sBDList = list(sDOBList[2:4])
        iBDList = [int(number) for number in sBDList]
        self.__BirthDay = self.simplify(iBDList)
        
        #Attitude is found by passing the month and days to simplify().
        sANList = list(sDOBList[0:4])
        iANList = [int(number) for number in sANList]
        self.__Attitude = self.simplify(iANList)        

        #List are created to be appended to separate vowels and consonants.
        sConsList=[]
        sVowelList=[]
        #Dictionary Constants are created with corresponding letter/number values sort out the name input.
        CONS_DICT = {"B":2,"C":3,"D":4,"F":6,"G":7,"H":8,"J":1,"K":2,"L":3,"M":4,"N":5,"P":7,"Q":8,"R":9,"S":1,"T":2,"V":4,"W":5,"X":6,"Y":7,"Z":8}
        VOWEL_DICT= {"A":1,"E":5,"I":9,"O":6,"U":3}
        
        #Consonants are seperated, assigned a value that is added to a list, and simplified.
        #Personality number found through this process.
        for letter,number in CONS_DICT.items():
            if letter in self.__name.upper():
                sConsList.append(number)
        iConsList = [int(number) for number in sConsList]
        self.__Personality = self.simplify(iConsList)
        
        #Vowels are seperated, assigned a value that is added to a list, and simplified.
        #Soul number found through this process.
        for letter,number in VOWEL_DICT.items():
            if letter in self.__name.upper():
                sVowelList.append(number)
        iVowelList = [int(number) for number in sVowelList]
        self.__Soul = self.simplify(iVowelList)
        
        #The PowerName is found by adding the Personality and Soul together, and using a portion of the simplify function.
        iPN = self.__Personality + self.__Soul
        while iPN > 9:
            iPN = int((str(iPN))[0])+int(((str(iPN))[1]))
        self.__PowerName = iPN


    #Attribute retrieval defined.
    @property
    def Name(self):
        return self.__name

    @property
    def Birthdate(self):
        return self.__DOB

    @property
    def LifePath(self):
        return self.__LifePath
          
    @property
    def BirthDay(self):
        return self.__BirthDay

    @property           
    def Attitude(self):
        return self.__Attitude

    @property        
    def Personality(self):
        return self.__Personality

    @property    
    def PowerName(self):
        return self.__PowerName

    @property    
    def Soul(self):
        return self.__Soul

    #Was about to turn in assignment when I saw this note on the upload screen, "CHANGE: add __str__ to return a string representation of the object."
    #Used this to replace the first "test" sample on the output.
    def __str__(self):
        return (f"Test Name: {self.__name}\nTest DOB: {self.__DOB}\nLife Path Number: {self.__LifePath}\n"
               f"Birth Day Number: {self.__BirthDay}\nAttitude Number: {self.__Attitude}\nSoul Number: {self.__Soul}\n"
               f"Personality Number: {self.__Personality}\nPower Name Number: {self.__PowerName}")
        
    #The simplify function used to find the sum of the numerology factors until the value is less than 10.
    def simplify(self, iList):
        iNumber = (sum(iList))
        while iNumber > 9:
            iNumber = int((str(iNumber))[0])+int(((str(iNumber))[1]))
        return iNumber
