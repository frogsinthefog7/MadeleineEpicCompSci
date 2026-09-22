
class Car:
    def __init__(self, make, model, mpg):
        self.make = make
        self.model = model
        self.mpg = mpg

def main():
    car1 = Car("Toyota", "Prius", 35)
    car2 = Car("Subaru", "Outback", 32)
    car3 = Car("Ford", "F150", 25)

    parking_lot = [car1, car2, car3]

    total_car_mpg = 0

    for car in parking_lot:
        total_car_mpg += car.mpg

    print(f"The sum of all the car's mpg is {total_car_mpg}")

if __name__ == '__main__':
    main()