class Car:
    # atributos y variables de clase
    no_of_tires = 4

    # constructor / inicializador de clase
    def __init__(self):
        self.make = ""
        self.model = ""
        self.year = ""
        self.color = ""
        self.moon_roof = ""
        self.engine_running = ""

        # atributos y variables de objeto
        # metodos

        def start_the_engine(self):
            self.engine_running = True

        def stop_the_engine(self):
            self.engine_running = False


def main():
    print("hola desde main()")
    car1 = Car()
    car2 = Car()

    #Values
    car1.make = "Tesla"
    car1.model = "Model 3"
    car1.color = "Red"
    car1.year = 2020
    car1.moon_roof =True

    print("Printing Car details".center(50,"-"))
    print("Make : {}".format(car1.make))
    print("Model : {}".format(car1.model))
    print("Year : {}".format(car1.year))
    print("Color : {}".format(car1.color))
    print("Moon Roof : {}".format(car1.moon_roof))

    print("Printing Car details".center(50,"-"))
    print("Make : {}".format(car2.make))
    print("Model : {}".format(car2.model))
    print("Year : {}".format(car2.year))
    print("Color : {}".format(car2.color))
    print("Moon Roof : {}".format(car2.moon_roof))

    print("Printing Car tires".center(50, "-"))
    car1.no_of_tires = 25
    Car.no_of_tires = 30
    print("car 1" ,car1.no_of_tires)
    print("car 2", car2.no_of_tires)
    print("Car", Car.no_of_tires)


if __name__ == '__main__':
    main()
