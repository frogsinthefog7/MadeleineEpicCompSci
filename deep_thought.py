
def WhatIsTheAnswer():
    theAnswer = input("What is the answer to life, the universe, and everything? ").lower()
    if theAnswer == "42" or theAnswer == "fourty-two" or theAnswer == "fourty two":
        print("YES")
        quit()
    else:
        print("no...")
        print("maybe try again...")
        start()

def start():
    WhatIsTheAnswer()

start()