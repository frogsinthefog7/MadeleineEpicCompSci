from time import sleep

time = 0.0

def main():

    global time

    time = input("What time is it(Military Time)? ")
    time = convert(time)

def convert(time):
    try:
        a, b = time.split(":")

        a = int(a)

        b = int(b)
        b = b / 60

        time = a + b
    except ValueError:
        print("That's not a good time...")
        sleep(2)
        print("Do you need to go back to kindergarten...?")
        sleep(1)
        print("Why don't your try again sweetie.")
        sleep(2)
        return main()

    int(time)

    return time
    
main()

if time <= 8 and time >= 7:
    print("It's breakfeast time!")
    sleep(1)
    print("I vote you make pancakes!")
    sleep(2)
elif time <= 13 and time >= 12:
    print("I'ts time for lunch.")
    sleep(1)
    print("Yeah, it's time for lunch!")
    sleep(1)
    print("Bubble, bubble, bubble, guppie, guppie, guppi....")
    sleep(2)
elif time <= 19 and time >= 18:
    print("It's dinner time, you know what that means.")
    sleep(1)
    print("Your stomach is screaming \"Feed me Semor!\" \"FEED ME!\"")
    sleep(2)
else:
    print("It's not time for a meal")
    print("...okay, and...")
    sleep(2)
    print("Why are you still here?, it's not time for a meal.")
    sleep(3)
    print("Please leave now.")
    sleep(5)
    print("OKAY!")
    sleep(1)
    print("THAT'S IT!!")
    sleep(.5)
    print("I'M KICKING YOU OUT!!!!!!")
    sleep(.5)