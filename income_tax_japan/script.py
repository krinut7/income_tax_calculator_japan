from income_tax_japan.classes import Employee

if __name__ == "__main__":
    employee_x = Employee(5360810, 0)
    employee_x_old = Employee(5000000, 0)
    employee_x_dependant = Employee(5360810, 1)
    print(employee_x.income_tax / 12)
    print(employee_x_old.income_tax / 12)
    print(employee_x.income_tax - employee_x_dependant.income_tax)
