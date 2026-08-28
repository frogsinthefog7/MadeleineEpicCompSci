
def Temp():
    HighTemp = input("What is the high tempurature for today(In Farenheit)? ")

    try:
        HighTemp = int(HighTemp)
        if HighTemp < 60:
            print("You need to bring a sweater.")
        elif HighTemp > 140:
            print("invalid temperature")
            start()
        else:
            print("You do not need to bring a sweater.")
    except ValueError:
        print("invalid temperature")
        start()


def start():
    Temp()

start()