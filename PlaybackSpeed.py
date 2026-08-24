
def SlowDown(userInput):
    
    global slow

    slow = userInput.split()
    print(slow)
    seperator = "..."
    slow = seperator.join(slow)


userInput = str(input("What would you like to say? \n"))
SlowDown(userInput)
print(slow)