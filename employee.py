"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name):
        self.name = name

    def get_pay(self):
        raise NotImplementedError

    def __str__(self):
        raise NotImplementedError

class SalaryEmployee(Employee):
    def __init__(self, name, salary):
        super().__init__(name)
        self.salary = salary

    def get_pay(self):
        return self.salary

    def __str__(self):
        return f"{self.name} works on a monthly salary of {self.salary}. Their total pay is {self.get_pay()}."

class HourlyEmployee(Employee):
    def __init__(self, name, hourly_wage, hours_worked):
        super().__init__(name)
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked

    def get_pay(self):
        return self.hourly_wage * self.hours_worked

    def __str__(self):
        return f"{self.name} works on a contract of {self.hours_worked} hours at {self.hourly_wage}/hour. Their total pay is {self.get_pay()}."

# Example of a mixin for bonus commission
class BonusCommissionMixin:
    def __init__(self, bonus):
        self.bonus = bonus

    def get_bonus_pay(self):
        return self.bonus

    def __str__(self):
        return super().__str__() + f" and receives a bonus commission of {self.bonus}."

# Example of a mixin for contract commission
class ContractCommissionMixin:
    def __init__(self, num_contracts, commission_per_contract):
        self.num_contracts = num_contracts
        self.commission_per_contract = commission_per_contract

    def get_contract_commission_pay(self):
        return self.num_contracts * self.commission_per_contract

    def __str__(self):
        return super().__str__() + f" and receives a commission for {self.num_contracts} contract(s) at {self.commission_per_contract}/contract."

# Examples of combined classes
class SalaryEmployeeWithBonus(SalaryEmployee, BonusCommissionMixin):
    def __init__(self, name, salary, bonus):
        SalaryEmployee.__init__(self, name, salary)
        BonusCommissionMixin.__init__(self, bonus)

    def get_pay(self):
        return super().get_pay() + self.get_bonus_pay()

class SalaryEmployeeWithContractCommission(SalaryEmployee, ContractCommissionMixin):
    def __init__(self, name, salary, num_contracts, commission_per_contract):
        SalaryEmployee.__init__(self, name, salary)
        ContractCommissionMixin.__init__(self, num_contracts, commission_per_contract)

    def get_pay(self):
        return super().get_pay() + self.get_contract_commission_pay()

# Similarly, you can create classes for HourlyEmployee with bonus and contract commission


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie')
billie.set_salary_contract(4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie')
charlie.set_hourly_contract(25, 100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee')
renee.set_salary_contract(3000)
renee.set_contract_commission(4, 200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan')
jan.set_hourly_contract(25, 150)
jan.set_contract_commission(3, 220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie')
robbie.set_salary_contract(2000)
robbie.set_bonus_commission(1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel')
ariel.set_hourly_contract(30, 120)
ariel.set_bonus_commission(600)
