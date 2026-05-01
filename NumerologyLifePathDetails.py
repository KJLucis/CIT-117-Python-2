import numerology

#Create the NumerologyLifePathDetails class to inherit the Numerology class.
class NumerologyLifePathDetails(numerology.Numerology):
    def __init__(self, sName, sDOB):
        self.__name = sName
        self.__DOB = sDOB
        numerology.Numerology.__init__(self, sName, sDOB)
        #A dictionary is created to store the values of what each life path number means.
        #The life path number is used as the key to return the corresponding value.
        dictLPD = {1:"The Idependent: Wants to work/think for themselves.",
                   2:"The Mediator: Avoids conflict and wants love and harmony.",
                   3:"The Performer: Likes music, art and to perform or get attention.",
                   4:"The Teacher/ Truth Seeker: Is meant to be a teacher or mentor and is truthful.",
                   5:"The Adventurer: Likes to travle and meet others, often an extrovert.",
                   6:"The Inner Child: Is meant to be a parent and/or one that is young at heart.",
                   7:"The Naturalist: Enjoy nature and water and alternative life paths, open to spirituality.",
                   8:"The Executive: Gravitates to money and power.",
                   9:"The Humanitarian: Helps others and/or experiences pain and learns the hard way."}
        self.__LifePathDescription = (dictLPD[self.LifePath])        
    
    @property
    def LifePathDescription(self):
        return self.__LifePathDescription
