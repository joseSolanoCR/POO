# public access modifier

class Employee:
    def __init__(self, first_name, last_name, base_annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.base_annual_salary = base_annual_salary
        self.__bonus_percentage = 10

    def get_monthly_gross(self):
        return self.base_annual_salary /12


    def get_standard_annual_bonus_ammount(self):
        return self.base_annual_salary * (self.__bonus_percentage/100)


def main():
    print("hola desde Main")

    employee1 = Employee("JP","Solano",50000)
    pago_mensual = employee1.get_monthly_gross()
    bono_anual = employee1.get_standard_annual_bonus_ammount()

    print("Salario Anual: {:.2f}".format(employee1.base_annual_salary))
    print("Salario Mensual: {:.2f}".format(pago_mensual))
    print("Bono Anual: {:.2f}".format(bono_anual))


if __name__ == '__main__':
    main()

