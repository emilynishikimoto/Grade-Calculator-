from statistics import mean
def findCategories():
    """Asks the user what categories their grade is split up into, returns a list of categories"""
    # create an empty list to accumulate the categories into 
    categoriesList = []
    #Ask the user how many categories there are and assign it the the variable categoryNumber
    categoryNumber = int(input("How many categories is your grade split up into? "))
    #create an empty string to store the category name in 
    categoryName = ""
    # for the amount categories, ask the user to name the category 
    for category in range(categoryNumber):
        #ask the user for input as to what the category name is 
        categoryName = str(input("Please enter the name for category: "))
        #add that category into the list 
        categoriesList.append(categoryName)
        #reset the category name
        categoryNumber = ""
    #return the categories list 
    return categoriesList

def findCategoriesWeight(categoryList):
    """Given a list of categories, asks the user for Input of weight of that category and maps the weight
    to the category in a dictionary"""
    #create an empty dictionary to store categories and their weights 
    categoryWeightDict = {}
    # create an empty string to store the category name 
    categoryName = ""
    #create and empty string to store the category weight
    categoryWeight = ""
    # iterate over every category in the list 
    for eachCategory in categoryList:
        #assign the category name to the variable categoryName
        categoryName = eachCategory
        # ask the user what the weight of that category is 
        categoryWeightInput = input(f"What is the weight of {categoryName} ")
        #make the category weight input into an int and assign it to categoryWeight
        categoryWeight = int(categoryWeightInput)
        #map the category Name to its weight in the dictionary as a percent 
        categoryWeightDict[categoryName]= categoryWeight/100
        #reset the variables category name and weight for next round 
        categoryName = ""
        categoryWeight = ""
    #return the dictionary 
    return categoryWeightDict

def assignmentGrades(categoriesList):
    """Given a list of categories that factor into a final grade, asks how many assignments there are
    and what they got on each assignment as an percent, then finds the average of those grades.
    Maps the category to the grade average for that category  as
    dictionary """
    #create an empty dictionary to hold the assignment scores and their categories 
    assignmentGradeDict = {}
    #create a variable to hold the category name
    catName = ""
    #create an empty list to hold the assignment scores 
    assignmentScores = []
    #iterate over every category 
    for cat in categoriesList:
        #assign the category name to the one we are on in the list 
        catName = cat
        #ask the user how many assignments are in that category as an int 
        numOfAssignments = int(input(f"How many assignments are there in the category {cat} "))
        # Get the grades for the number of assignments 
        for grade in range(numOfAssignments):
            #ask the user for the grade for each assignment and make it an int and a percentage 
            enterGrade = int(input("What was the grade for this assignment? "))/100
            # add that to the list of grades 
            assignmentScores.append(enterGrade)
        # find the average of the scores
        avg = mean(assignmentScores) 
        # using a dictionary map the average grade to the category 
        assignmentGradeDict[catName] = avg 
        #reset the list and the catName 
        catName = ""
        assignmentScores = []
    #return the dictionary 
    return assignmentGradeDict

def calculateFinalGrade(categoryList, weightsDictionary, averagesDictionary):
    """Given the list of categories, a dictionary mapping weights to the categories in that list, and a 
    dictionary that maps average grades to each category. For each category in the list, finds the weight
    for that category and the average grade of that category and multiplies them together to find the weight
    it is in the final grade. Then adds all of the weights together to get the final grade"""
    #create an empty list to put the scores into 
    scoresList = []
    #iterate over every category in the category list 
    for category in categoryList:
        #from the weights dictionary, find the weight of that category and assign it to weight 
        weight = weightsDictionary[category]
        #from the averages dictionary find the average of the category and assign it to average 
        average = averagesDictionary[category]
        #multiply the average by the weight and append it into the scores list 
        scoresList.append(average*weight)
    #sum all the numbers in the scores list and assign that to the variable final grade 
    finalGrade = sum(scoresList)
    #return the final grade
    return finalGrade

def main():
    """Runs the main code of the function"""
    #find the amount of categories the grade is broken into 
    listOfCategories = findCategories ()
    #find weights of Categories and put them into a dictionary 
    dictOfWeights = findCategoriesWeight(listOfCategories)
    # find the average grade for each category 
    dictOfAvg = assignmentGrades(listOfCategories)
    #calculate the final grade 
    finalGrade = calculateFinalGrade(listOfCategories,dictOfWeights,dictOfAvg)
    #turn the final grade into a whole number 
    finalGrade *= 100 
    #return what the final grade is with a print statement say your final grade is:
    return print(f"Your final grade is {finalGrade}%")
############## MAIN CODE ######################
run = main()
