class Calculo:

    def __init__(self, name, lastname, salary,bonus,years, retirem):
        self.name = name
        self.lastname = lastname
        self.salary = salary
        self.bonus = bonus
        self.years = years
        self.retirem = retirem

    def bonification(self):
        plus = (self.salary/100)*self.bonus
        return self.salary + plus

def main():
    print("hola desde main")
    reporte = Calculo("hola", "mundo",100, 10,2,10)
    test = reporte.bonification()
    print(test)

if __name__ == '__main__':
    main()
