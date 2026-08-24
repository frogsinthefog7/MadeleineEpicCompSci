def lowercase(userInput):

    global quiet

    quiet = userInput.lower()

userInput = str(input("What would you like to say? \n"))
lowercase(userInput)
print("I think you meant to say:" , quiet)