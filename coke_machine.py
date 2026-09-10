
def coin_inserted(coin, amount_due):
    amount_due = amount_due - coin
    return amount_due
    

def paid_in_full(change):

    print("One Coke coming up!")

    if change != 0:
        print(f"Here's your change: {change}")
    elif change == 0:
        print("You don't have any change!")

    print("Don't forget to have your Coke and smile.")

def main():

    amount_due = 50
    print("That Coke will be $0.50")

    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        inserted_coin = int(input("Coin: "))
        amount_due = coin_inserted(inserted_coin, amount_due)

    if amount_due < 0:
        amount_due = abs(amount_due)
        print(f"Change Owed: {amount_due}")
        paid_in_full(amount_due)
    elif amount_due == 0:
        paid_in_full(amount_due)

main()