class Employee:
    _STANDARD_DEDUCTIONS = [0, 1625000, 1800000, 3600000, 6600000, 8500000]
    _PERSONAL_EXPEMPTIONS = [0, 24000000, 24500000, 25000000]
    _TAX_RATE = [0, 1950000, 3300000, 6950000, 9000000, 18000000, 40000000]

    def __init__(self, gross_income: int, dependants: int):
        self._gross_income = gross_income
        self._exclusion = self.exclusion
        self._personal_expemtions = self.personal_expemtion
        self._dependants = dependants
        self._taxable_income = self.taxable_income

    @property
    def exclusion(self) -> int:
        if self._gross_income in range(
            Employee._STANDARD_DEDUCTIONS[0], Employee._STANDARD_DEDUCTIONS[1]
        ):
            exclusion = 550000
        elif self._gross_income in range(
            Employee._STANDARD_DEDUCTIONS[1], Employee._STANDARD_DEDUCTIONS[2]
        ):
            exclusion = 0.4 * self._gross_income - 100000
        elif self._gross_income in range(
            Employee._STANDARD_DEDUCTIONS[2], Employee._STANDARD_DEDUCTIONS[3]
        ):
            exclusion = 0.3 * self._gross_income + 80000
        elif self._gross_income in range(
            Employee._STANDARD_DEDUCTIONS[3], Employee._STANDARD_DEDUCTIONS[4]
        ):
            exclusion = 0.2 * self._gross_income + 440000
        elif self._gross_income in range(
            Employee._STANDARD_DEDUCTIONS[4], Employee._STANDARD_DEDUCTIONS[5]
        ):
            exclusion = 0.1 * self._gross_income + 1100000
        else:
            exclusion = 1950000

        return exclusion

    @property
    def personal_expemtion(self) -> int:
        if self._gross_income in range(
            Employee._PERSONAL_EXPEMPTIONS[0], Employee._PERSONAL_EXPEMPTIONS[1]
        ):
            personal_expemtion = 480000
        elif self._gross_income in range(
            Employee._PERSONAL_EXPEMPTIONS[1], Employee._PERSONAL_EXPEMPTIONS[2]
        ):
            personal_expemtion = 320000
        elif self._gross_income in range(
            Employee._PERSONAL_EXPEMPTIONS[2], Employee._PERSONAL_EXPEMPTIONS[3]
        ):
            personal_expemtion = 160000
        else:
            personal_expemtion = 0

        return personal_expemtion

    @property
    def taxable_income(self):
        taxable_income = (
            self._gross_income
            - self._exclusion
            - self._personal_expemtions
            - self._dependants * 380000
        )

        return taxable_income

    @property
    def income_tax(self):
        if self._taxable_income in range(Employee._TAX_RATE[0], Employee._TAX_RATE[1]):
            income_tax = 0.05 * self._taxable_income - 0
        elif self._taxable_income in range(
            Employee._TAX_RATE[1], Employee._TAX_RATE[2]
        ):
            income_tax = 0.1 * self._taxable_income - 97500
        elif self._taxable_income in range(
            Employee._TAX_RATE[2], Employee._TAX_RATE[3]
        ):
            income_tax = 0.2 * self._taxable_income - 427500
        elif self._taxable_income in range(
            Employee._TAX_RATE[3], Employee._TAX_RATE[4]
        ):
            income_tax = 0.23 * self._taxable_income - 636000
        elif self._taxable_income in range(
            Employee._TAX_RATE[4], Employee._TAX_RATE[5]
        ):
            income_tax = 0.33 * self._taxable_income - 1536000
        elif self._taxable_income in range(
            Employee._TAX_RATE[5], Employee._TAX_RATE[6]
        ):
            income_tax = 0.4 * self._taxable_income - 2796000
        else:
            income_tax = 0.45 * self._taxable_income - 4796000

        return income_tax
