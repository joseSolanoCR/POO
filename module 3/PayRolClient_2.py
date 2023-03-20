from EmployeeTypes import *
from PayRollProcessor import *

management_employee_1 = Employee('JP', 'Solano', 1001, 5 , 120000.000)
salaried_employee_1 = Employee('Mamorin', 'Zamora', 2001, 1 , 60000.000)
sales_employee_1 = Employee('Pelon', 'Salazar', 1004, 1 , 80000.000, 1)

list_of_employees = [management_employee_1,salaried_employee_1, sales_employee_1]

payroll = PayRollProcessor('17/03/2023')
payroll.print_payroll_report(list_of_employees)


