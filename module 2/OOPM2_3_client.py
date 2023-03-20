from OOPM2_3 import Employee

employee1 = Employee("JP", "Solano", 50000)
pago_mensual = employee1.get_monthly_gross()
bono_anual = employee1.get_standard_annual_bonus_ammount()

print("Salario Anual: {:.2f}".format(employee1.base_annual_salary))
print("Salario Mensual: {:.2f}".format(pago_mensual))
print("Bono Anual: {:.2f}".format(bono_anual))