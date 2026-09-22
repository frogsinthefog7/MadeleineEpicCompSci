
class MenuItem:

    def __init__(self, name, price):
        self.name = name
        self.price = price

class Order:

    def __init__(self, receipt):
        self.receipt = receipt

    def add_item(self, item):
        self.receipt.append(item)

    def calculate_taxes(self):

        global with_taxes_price
        global tax_total

        tax_total = 0

        with_taxes_price = []

        for i in self.receipt:
            with_taxes_price.append(i.price + (i.price * 0.07))
            tax_total += i.price * 0.07

    def calculate_total(self, total):

        global with_taxes_price

        self.calculate_taxes()
        
        for i in with_taxes_price:
            total += i

        return total


    def print_receipt(self, total):

        print("MONTY PYTHON'S GREAT CAFE")
        print("---------------")

        for i in self.receipt:
            print(f"{i.name}: ${i.price}0")

        print("---------------")
        print(f"Taxes: ${str(round(tax_total, 2))}")

        print("---------------")
        print(f"Your total is: ${round(total,2)}\n")


def main():

    menu = [

        MenuItem("bagel", 3.00),
        MenuItem("burrito", 5.00),
        MenuItem("ramen", 1.50),
        MenuItem("gum", 0.50)
    ]

    order1 = Order([])
    order1.add_item(menu[1])
    order1.add_item(menu[1])
    order1.add_item(menu[3])

    total = 0

    total = order1.calculate_total(total)
    print("")
    print(f"The total due is ${str(round(total,2))}")

    order1.print_receipt(total)

if __name__ == '__main__':
    main()