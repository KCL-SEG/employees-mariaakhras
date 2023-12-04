"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name):
        self.name = name
        self.salary_pay = 0
        self.hourly_pay = 0
        self.hours_worked = 0
        self.comm_pay = 0
        self.no_of_contracts = 0
        self.bonus_pay = 0
    def set_salary(self, salary_pay):
        self.salary_pay = salary_pay

    def set_hourly(self, hourly_pay, hours_worked):
        self.hourly_pay = hourly_pay
        self.hours_worked = hours_worked
        
    def set_comm(self, comm_pay, no_of_contracts=0):
        self.comm_pay = comm_pay
        self.no_of_contracts = no_of_contracts

        def set_bonus(self, bonus_pay):
         self.bonus_pay = bonus_pay

    def get_salary(self):
         return self.salary_pay + self.comm_pay * self.hourly_pay

    def get_comm(self):
         return self.comm_pay * self.no_of_contracts + self.bonus_pay

    def get_pay(self):
         salary_total = self.salary_pay
         hourly_total = self.hourly_pay * self.hours_worked
         comm_total = self.comm_pay * self.no_of_contracts
         bonus_total = self.bonus_pay

         return salary_total + hourly_total + comm_total + bonus_total

    def __str__(self):
        employee = f"{self.name} works on a "
        employee = f"{self.name} works on "

        if self.salary_pay > 0:
             employee += f"monthly salary of {self.salary_pay} "
             employee += f"a monthly salary of {self.salary_pay}"
        elif self.hourly_pay > 0 and self.hours_worked > 0:
             employee += f"contract of {self.hours_worked} hours at {self.hourly_pay}/hour "
             employee += f"a contract of {self.hours_worked} hours at {self.hourly_pay}/hour"

        if self.comm_pay > 0:
             employee += "and receives a commission for "
             if self.no_of_contracts > 0:
                 employee += f"{self.no_of_contracts} contract(s) at {self.comm_pay}/contract "
             else:
                 employee += f"a bonus commission of {self.comm_pay} "
                 if self.salary_pay > 0 or (self.hourly_pay > 0 and self.hours_worked > 0):
                     employee += " and "
                 employee += f"receives a commission for {self.no_of_contracts} contract(s) at {self.comm_pay}/contract"

        if self.bonus_pay > 0:
             if self.salary_pay > 0 or (self.hourly_pay > 0 and self.hours_worked > 0) or self.no_of_contracts > 0:
                 employee += " and "
             employee += f"receives a bonus commission of {self.bonus_pay}"

        employee += f". Their total pay is {self.get_pay()}."
        return employee.strip()
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
