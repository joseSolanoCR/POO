class Car:
    # atributos y variables de clase
    no_of_tires = 4

    # constructor / inicializador de clase
    def __int__(self, make, model, year, color, moon_roof=False):
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

if __name__ == '__main__':
    main()


