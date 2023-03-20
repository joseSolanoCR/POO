class Car:
    # atributos y variables de clase
    no_of_tires = 4

    # constructor / inicializador de clase
    def __int__(self):
        self.make = "Ford"
        self.model = "Mustang"
        self.year = 2010
        self.color = "Blue"
        self.moon_roof = True
        self.engine_running = False


    # atributos y variables de objeto
    # metodos
    def start_the_engine(self):
        self.engine_running = True



    def stop_the_engine(self):
        self.engine_running = False

    pass
