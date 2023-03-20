# public access modifier

class Employee:
    def __init__(self, first_name, last_name,):
        self.first_name = first_name
        self.last_name = last_name
        self.__base_annual_salary = 0
        self.__bonus_percentage = 0


    def get_monthly_gross(self):
        return self.__base_annual_salary /12


    def get_standard_annual_bonus_ammount(self):
        return self.__base_annual_salary * (self.__bonus_percentage/100)

    #getters
    @property
    def base_annual_salary(self):
        return self.__base_annual_salary
    @property
    def bonus_percentage(self):
        return self.__bonus_percentage

    #setters
    @base_annual_salary.setter
    def base_annual_salary(self, base_annual_salary):
        if 45000.00 <= base_annual_salary <= 120000.00:
            self.__base_annual_salary = base_annual_salary
        else:
            print("must be between 45k and 120K")

    @bonus_percentage.setter
    def bonus_percentage(self, bonus_percentage):
        if 0.05 <= bonus_percentage <= .21:
            self.__bonus_percentage = bonus_percentage
        else:
            print("must be between 5% and 21%")




def main():
    print("hola desde Main")

    employee1 = Employee("JP","Solano")
    employee1.bonus_percentage = 0.1
    employee1.base_annual_salary = 130000.00

    pago_mensual = employee1.get_monthly_gross()
    bono_anual = employee1.get_standard_annual_bonus_ammount()

    print("Salario Anual: {:.2f}".format(employee1.base_annual_salary))
    print("Salario Mensual: {:.2f}".format(pago_mensual))
    print("Bono Anual: {:.2f}".format(bono_anual))


if __name__ == '__main__':
    main()

