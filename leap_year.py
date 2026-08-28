
def leapYear():
    
    theYear = input("what is the year? ")

    try:
        theYear = int(theYear)
        NotAString(theYear)
    except ValueError:
        print("This is not Leap Year.")
        print("")
        Start()


def NotAString(theYear):

    theYearOverFour = theYear % 4
    theYearOverFourHundred = theYear % 400
    theYearOverOneHundred =theYear % 100
        
    
    if theYearOverFour == 0 and theYearOverOneHundred != 0:
        print("This is a Leap Year!")
    elif theYearOverOneHundred == 0 and theYearOverFourHundred == 0:
        print("This is a Leap Year!")
    else:
        print("This is not a Leap Year.")
    
    print("")
    
    Start()

def Start():
    leapYear()

Start()