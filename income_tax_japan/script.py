from income_tax_japan.classes import Employee

if __name__ == "__main__":
    krishna = Employee(5360810, 0)
    krishna_old = Employee(5000000, 0)
    krishna_dependant = Employee(5360810, 1)
    print(krishna.income_tax / 12)
    print(krishna_old.income_tax / 12)
    print(krishna.income_tax - krishna_dependant.income_tax)
