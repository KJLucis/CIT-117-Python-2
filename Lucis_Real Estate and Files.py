#Name: Katlyn Lucis    3/16/2026
#CIT-117-D02 Python Programming 2
#Assignment: Real Estate and Files
#Reflection: Share what you liked about this assignment?    I enjoyed that this assignment built off of the real estate anaylzer we had last semester.  I also like that it had a really practical
#                                                           usage of the .csv file since those are used so often.
#            Share what you struggled with?    Getting the sum() to work on the value portion of the dictionary.  The initial attempts to convert the inputs to float kept throwing errors, so I took a break from
#                                               that part for a bit to work on other parts.  I looked at it later and it seemed so much simpler.
#            Which approach did you use to import the data and why did you choose it?   I used the csv.reader since it is specifically designed to read csv files and helps with conformity.
#            How many dictionaries did you use for this assignment?     3 dictionaries (for each requested sort type) and 1 list (for the overall price summary)
#            Share exactly 2 things you learned on this assignment:    
#            1. I learned that the csv.reader iterates over the rows of a .csv file and returns them as strings.
#            2. I wrote a dictionary with the values as a list from a .csv file.  It was different to read from a provided file rather than write one as we did in the last assignment.


#Import the csv module for later use.
import csv
def main():

    sIMPORT_TARGET = 'RealEstateData.csv'
    #getDataInput is called to obtain the necissary dictionaries and list for the summaries.
    (dictCityKJL, dictZipKJL, dictTypeKJL, priceListKJL) = getDataInput(sIMPORT_TARGET)
    
    #The price list is sorted in ascending order so the median can be found.
    list.sort(priceListKJL)

    #getMedian function is called and returns the value for fMedian.
    fMedian = getMedian(priceListKJL)

    #All values are calculated and displayed with proper formatting based on the assignment example.
    print(f"Data summaries from {sIMPORT_TARGET}")
    print(f"Minimum: \t {(min(priceListKJL)):25,.2f}")
    print(f"Maximum: \t {(max(priceListKJL)):25,.2f}")
    print(f"Sum: \t \t {(sum(priceListKJL)):25,.2f}")
    #The average of the list is printed using the sum() divided by the length of the list.
    print(f"Average: \t {((sum(priceListKJL)/len(priceListKJL))):25,.2f}")
    #The fMedian formatted and printed to display the median.
    print(f"Median: \t {fMedian:25,.2f}")


    #The requested summaries are given by property type, city, and zip code, with formatting to keep them in line per the example.
    print('\n'"Summary by Property Type:")
    for sType, fpriceList in dictTypeKJL.items():
        print(f"{sType:<12} \t {sum(fpriceList):25,.2f}")

    print('\n'"Summary by City:")
    for sCity, fpriceList in dictCityKJL.items():
        print(f"{sCity:<16} {sum(fpriceList):25,.2f}")

    print('\n'"Summary by Zip code:")
    for iZip, fpriceList in dictZipKJL.items():
        print(f"{iZip:<16} {sum(fpriceList):25,.2f}")      

def getDataInput (sIMPORT_TARGET):

    #RealEstate.csv opened "with" so it will close when the block finishes.
    try:
        with open(sIMPORT_TARGET, 'r') as dataInKJL:

            #dataInKJL is assigned the strings from the csv.reader iterations.
            dataInKJL = csv.reader(dataInKJL)
        
            #The first column of the file is passed over with .__next__() so it is not added to the dictionaries.
            passHeadingsKJL = dataInKJL.__next__()
        
            #Dictionaries and list created for data extraction.
            dictCityKJL = {}
            dictZipKJL = {}
            dictTypeKJL = {}
            priceListKJL = []
        
            #The strings taken from the .csv file are iterated over and the relevant data is extracted into dictionaries.
            for (sStreet, sCity, iZip, sState, iBeds, iBaths, iSqft, sType, fPrice, iLatitude, iLongitude) in dataInKJL:
            
                #The City column is seperated out.  If the city doesnt exist, it created a key with the price as the value.
                #If the city does exist, the price is appended to the value list.
                #This is repeated for the relevent data.
                if sCity not in dictCityKJL:
                    dictCityKJL[sCity] = [float(fPrice)]
                else:
                    dictCityKJL[sCity].append(float(fPrice))
        
                if iZip not in dictZipKJL:
                    dictZipKJL[iZip] = [float(fPrice)]
                else:
                    dictZipKJL[iZip].append(float(fPrice))
        
                if sType not in dictTypeKJL:
                    dictTypeKJL[sType] = [float(fPrice)]
                else:
                    dictTypeKJL[sType].append(float(fPrice))
    
                #The prices are placed in a list to use for the overall summary.
                priceListKJL.append(float(fPrice))
    except FileNotFoundError:
        print(f"{sIMPORT_TARGET} not found. Please relocate {sIMPORT_TARGET} to the current working directory and restart the program.")
        input("Press ENTER to quit.")
        quit()
        
    #The dictionaries and list are returned to the main function.
    return(dictCityKJL, dictZipKJL, dictTypeKJL, priceListKJL)

#Define getMedian function.
#priceListKJL is passed to the function.
def getMedian (priceListKJL):
    #The function tests if the length of the list is even or odd.
    #If the list is divisible by 2 with no remainder, it is deemed even.
    #An even number will require both of the middle most indices be found.
    if (len(priceListKJL) % 2) == 0:
        #The index of the second middle value is found with integer division.
        #The index of the first middle value is found by subtracting one from the integer division result.
        #fMedianKJL is determined by adding the values at each index in the list and dividing the total by 2.
        fMedianKJL = ((priceListKJL[(len(priceListKJL)//2-1)]+priceListKJL[(len(priceListKJL)//2)])/2)
    #If the list is found to be odd, the follow else executes.
    else:
        #The index of the middle number is found using integer division.
        iIndexKJL = len(priceListKJL)//2
        #The property value at fIndex is assigned to fMedian.
        fMedianKJL = priceListKJL[iIndexKJL]
    #fMedian is returned to the main function.
    return fMedianKJL
        
#Call the main function.
main()
