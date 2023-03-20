class Car:
    # atributos y variables de clase
    no_of_tires = 4

    # constructor / inicializador de clase
    def __init__(self, make, model, year, color, moon_roof=False):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.moon_roof = moon_roof
        self.engine_running = False

        # atributos y variables de objeto
        # metodos

        def start_the_engine(self):
            self.engine_running = True

        def stop_the_engine(self):
            self.engine_running = False


def main():
    print("hola desde main()")
    car1 = Car('Ford', 'Mustang', 2010, 'blue')
    car2 = Car('Tesla', 'Model 3', 2020, 'Red', True)

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
    print("car 1" ,car1.no_of_tires)
    print("car 2", car2.no_of_tires)
    print("Car", Car.no_of_tires)


if __name__ == '__main__':
    main()
