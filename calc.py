
def getEquation():
    equation = input("What is the math equation? ")

    try:
        a, operation, b = equation.split()
        a = int(a)
        b = int(b)
    except ValueError:
        print("invalid input")
        return start()

    if operation == "/":
        calc(a,b,1)
    elif operation == "*":
        calc(a,b,2)
    elif operation == "+":
        calc(a,b,3)
    elif operation == "-":
        calc(a,b,4)
    else:
        print("This Calculator can't do that.")
        return start()

def calc(a,b,operation):

    if operation == 1:
        if b == 0:
            print("invalid input")
            return start()
        print(a/b)
        
    if operation == 2:
        print(a*b)

    if operation == 3:
        print(a+b)

    if operation == 4:
        print(a-b)


def start():
    getEquation()

start()