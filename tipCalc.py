
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip: .2f}")

def dollars_to_float(dollars):
    dollars = dollars.strip("$")
    dollars = float(dollars)
    return dollars

def percent_to_float(percentage):
    percentage = percentage.strip("%")
    percentage = float(percentage)
    percentage = percentage / 100
    return percentage

main()