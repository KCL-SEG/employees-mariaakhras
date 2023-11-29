"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name):
        self.name = name
        self.contract_type = None
        self.hourly_wage = None
        self.hours_worked = None
        self.monthly_salary = None
        self.commission_type = None
        self.commission_value = 0
        self.num_contracts = 0

    def set_salary_contract(self, salary):
        self.contract_type = "Salary"
        self.monthly_salary = salary

    def set_hourly_contract(self, wage, hours):
        self.contract_type = "Hourly"
        self.hourly_wage = wage
        self.hours_worked = hours

    def set_bonus_commission(self, bonus):
        self.commission_type = "Bonus"
        self.commission_value = bonus

    def set_contract_commission(self, contracts, commission_per_contract):
        self.commission_type = "Contract"
        self.num_contracts = contracts
        self.commission_value = commission_per_contract

    def calculate_pay(self):
        total_pay = 0

        # Salary or hourly pay calculation
        if self.contract_type == "Salary":
            total_pay += self.monthly_salary
        elif self.contract_type == "Hourly":
            total_pay += self.hourly_wage * self.hours_worked
        # Commission calculation
        if self.commission_type == "Bonus":
            total_pay += self.commission_value
        elif self.commission_type == "Contract":
            total_pay += self.num_contracts * self.commission_value

        return total_pay

    def __str__(self):
        # Initialize pay_details with an empty string
        pay_details = ""

        # Salary or hourly description
        if self.contract_type == "Salary":
            pay_details += f"{self.name} works on a monthly salary of {self.monthly_salary}."
        elif self.contract_type == "Hourly":
            pay_details += f"{self.name} works on a contract of {self.hours_worked} hours at {self.hourly_wage}/hour."
        # Commission description
        if self.commission_type == "Bonus":
            pay_details += f" and receives a bonus commission of {self.commission_value}."
        elif self.commission_type == "Contract":
            pay_details += f" and receives a commission for {self.num_contracts} contract(s) at {self.commission_value}/contract."
        # Append total pay
        pay_details += f" Their total pay is {self.calculate_pay()}."
        return pay_details

    def get_pay(self):
        return self.calculate_pay()

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
