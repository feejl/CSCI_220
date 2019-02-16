# Name: Jayton Fee
# mean.py
# Problem: Calculate the Root Mean Square (RMS) average,
#          The Harmonic Mean,
#          and the Geometric Mean using a single user input for each
#          formula
# Certification of Authenticity:
# I certify that this lab is my own work, but I discussed it with:
# Kendall Dunn at the CSL to pass the lists from function to function.
# Inputs: How many numbers and the list of numbers; from user
# Outputs: RMS, Harmonic Mean, and Geometric Mean
#          of the user inputs; to monitor

import math


# Define Root Mean Squared with a parameter
def rootMeanSquared(numList):
    # Initialize total
    totalNumbers = 0
    # Loop each input in the RMS formula
    for num in numList:
        total = num **2
        totalNumbers = total + totalNumbers
    average = totalNumbers/len(numList)
    rootMeanSq = math.sqrt(average)
    # Print the RMS Average rounded to the third decimal
    print("The Root Mean Squared Average of", *numList, "is",round(
        rootMeanSq,3))


# Define Harmonic Mean with a parameter
def harmonicMean(numList):
    # Initalize total
    totalNumbers = 0
    # Loop each input into the HM formula
    for num in numList:
        total = 1/num
        totalNumbers = total + totalNumbers
    harMean = len(numList)/totalNumbers
    # print Harmonic Mean rounded to the third decimal place
    print("The Harmonic Mean of", *numList, "is", round(harMean, 3))

# Define Geometric Mean with a parameter
def geometricMean(numList):
    # Initialize total
    totalNumbers = 1
    # Loop each input through the GM formula
    for num in numList:
        totalNumbers = num * totalNumbers
    geoMean = totalNumbers ** (1/len(numList))

    # Print the Geometric Mean rounded to the third decimal place
    print("The Geometric Mean of", *numList, "" "is", round(geoMean,3))


def main():
    print("This program calculates the Root Mean Squared Average, "
          "the Harmonic Mean, and the Geometric Mean of your numbers")

    numImputs = int(input("How many numbers do you want to calculate? "))
    print()

    # initialize empty list
    numList = []
    # Loop to get numbers based on the number of inputs
    for i in range(numImputs):
        number = eval(input("Enter your number: "))
        # Add to list using append: listname.append(item)
        numList.append(number)
    print()
    # Call each function with the list as the parameter
    rootMeanSquared(numList)
    harmonicMean(numList)
    geometricMean(numList)

main()




