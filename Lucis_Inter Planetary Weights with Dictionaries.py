#Name: Katlyn Lucis    2/27/2026
#CIT-117-D02 Python Programming 2
#Assignment: Planetary Weights Dictionaries
#Reflection: Share what you liked about this assignment?    Just like the other assignments, it is always satisfying figuring it all out, like pieces of a puzzle coming together and IDLE stops screaming at me about syntax errors.
#                                                           When beginning this project, I opened the previous planet conversion assignment as a base.  It amused me to be able to turn that whole program into about 6 lines or so.
#            Share what you struggled with?    Getting the dictionary within a dictionary to work with the pickling and reloading
#            How did you like working with dictionaries and pickling concepts?    It was very different and rather dynamic.  I can see how these could have much broader applications.
#            Share exactly 2 things you learned on this assignment:    I learned far more than just 2 things, but here are some of them-
#            1. I learned how to write, iterate over, and access a dictionary inside a dictionary
#            2. I also learned writing a file is a relatively heavy task and should be done at the end of the program, not at the end of every loop.


import pickle
def main():
    
    #dictionary created with all conversion rates.
    dictPLANET_CONVERSIONS = {'Mercury' : .38 , 'Venus' : .91 , 'our Moon' : .165, 'Mars' : .38 , 'Jupiter' : 2.34, 'Saturn' : .93, 'Uranus' : .92, 'Neptune' : 1.12, 'Pluto' : .066}
    #constant created to hold the file name.
    sPLANET_HISTORY = 'klPlanetaryWeights.db'
    #dictionary created to hold the name/planet/weight history
    dictPlanetHistoryKJL = {}

    #File Reading or Creation
    #program checks if the klPlanetaryWeights database file is already created.  If so, it is loaded and converted from binary, and changes the IsHistory variable to true.
    bIsHistory = False
    try:
        with open (sPLANET_HISTORY, 'rb') as inputfile:
            dictPlanetHistoryKJL = pickle.load(inputfile)
            bIsHistory = True
    #if not, the exception is handled and dictionary is created.
    except FileNotFoundError:
        dictPlanetHistoryKJL = {}

    #History Check
    #a loop is started to request if the user would like to see the history.
    if bIsHistory:
        sQueryKJL = input(f"Would you like to see the history y/n: ")
        #if the user enters y or Y, and the dictionary isnt empty, the dictionary keys and inner key/values are iterated over and printed.
        if sQueryKJL.lower() == 'y':
            for sOldName, dictOldPlanetWeights in dictPlanetHistoryKJL.items():
                print(f"{sOldName} here are your weights on our Solar System's planets:")
                #the nested dictionary is iterated over and printed to format.
                for sPlanets,sPlanetWeights in dictOldPlanetWeights.items():
                     print(f"Weight on {sPlanets}: \t {sPlanetWeights}")
                print('\n')

    #Name Loop
    #This loop continues until a valid name is entered
    while True:
        sNameKJL = input("What is your name (enter key to quit): ").title()
        if sNameKJL == "":
            break
        #the input name is tested against all (if any) previously entered names.
        if sNameKJL in dictPlanetHistoryKJL:
            print(f"{sNameKJL} is already in the history file.  Enter a unique name.")
            continue            
    
        #dictionary is created to hold planet and weight values.
        #fWeightKJL created to activate the next loop.
        dictPersonWeightsKJL = {}

        #Weight Loop
        #fWeightKJL created to activate the next loop.
        #this will continue until the user enters a valid numeric value.
        fWeightKJL = 0
        while fWeightKJL <=0:
            try:
                fWeightKJL = float(input("What is your weight: "))
                if fWeightKJL <= 0:
                        print("Input must be a positive numeric value")
            #exception handled if a non float value is entered.
            except ValueError:
                print("Input must be a positive numeric value")
        
        #Output & Pickling
        print(f"{sNameKJL} here are your weights on our Solar System's planets:")
        #the conversion constants are iterated over and the input weight is multiplied by the conversion rate.
        #the output is formated with a tab space, 10 characters wide, and 2 decimal places.
        for sPlanetKJL in dictPLANET_CONVERSIONS:
            print(f"Weight on {sPlanetKJL}: \t {(fWeightKJL*dictPLANET_CONVERSIONS[sPlanetKJL]):10.2f}")
            #dictionary filled with the planet name becoming the key for the values of the weights.
            #formatting carried over for simplifaction in recalling the history.
            dictPersonWeightsKJL[sPlanetKJL] = (f"{fWeightKJL*dictPLANET_CONVERSIONS[sPlanetKJL]:10.2f}")
        #the new elements are added to the planet history dictionary
        dictPlanetHistoryKJL[sNameKJL] = dictPersonWeightsKJL
        print('\n')
        
    #the klPlanetaryWeights database file is opened an the previously created list is serialized into binary.
    with open (sPLANET_HISTORY, 'wb') as outputfile:
        pickle.dump(dictPlanetHistoryKJL, outputfile)

main()
