"""
### Simple Program PacFlix

Features:
1. Check all plans in PacFlix
2. Check Plan for Existing User
3. Upgrade Plan for existing user
4. New user can use referral to get discount

User data:
User Name: String
Active Plan: Plan
Duration Plan: Integer
Referral Code: int

Note:
- Users in Pacflix can only choose one plan.
- Users can only upgrade and cannot downgrade.
- If a user has a plan duration of over 12 months and upgrades, they get a 5% discount:
  Total = New Plan Price - (New Plan Price * 0.05)
- If a user is new and has a referral code, they get a 4% discount:
  Total = Price - (Price * 0.04)

"""

from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from plan import *
import random
import string
from plan import basic_plan, standard_plan, premium_plan
from plan import list_plan
from tabulate import tabulate

class User:
    
    # Just for example the list of referral codes and list users that have been filled in
    __list_referral_code = {'John Doe': 'JohnzHDPi6D2', 
                            'Alice Smith': 'AliceH7JVzoH0', 
                            'bubu': 'bubuMjO3SZuf'}
    
    list_user = {'John Doe': ['Basic Plan', date(2021, 10, 17), 120000, Plan(plan_name='Basic Plan', can_stream=True, can_download=True, has_SD=True, has_HD=False, has_UHD=False, num_of_device=1, content=['3rd Party Movie'], price=120000)], 
                 'Alice Smith': ['Standard Plan', date(2022, 10, 17), 160000, Plan(plan_name='Standard Plan', can_stream=True, can_download=True, has_SD=True, has_HD=True, has_UHD=False, num_of_device=2, content=['3rd Party Movie ', 'Sports (F1, Football, Basketball)'], price=160000)], 
                 'bubu': ['Basic Plan', date(2023, 10, 17), 120000, Plan(plan_name='Basic Plan', can_stream=True, can_download=True, has_SD=True, has_HD=False, has_UHD=False, num_of_device=1, content=['3rd Party Movie'], price=120000)]
                 }


    def __init__(self, username, current_plan, register_date):
        self.username = username
        self.current_plan = current_plan
        self.plan_name = self.current_plan.plan_name
        self.register_date = register_date
        self.bill = self.current_plan.price
        self.referral_code = self.username.split()[0] + self.generate_referral_code()
        self.__list_referral_code[self.username] = self.referral_code
        self.list_user[self.username] = [
                self.current_plan.plan_name,
                self.register_date,
                self.bill,
                self.current_plan
                ]
                

    def upgrade_plan(self, new_plan):
        # (Code for upgrading the plan and calculating the discount)
        if new_plan not in list_plan:
            print("Plan tidak terdaftar")
            return

        discount = 0
        today = date.today()
        difference_in_years = relativedelta(today, self.list_user[self.username][1]).years
        
        if  new_plan.price <=  self.list_user[self.username][2]:
            print("Anda tidak bisa melakukan upgrade, pilih plan yang lebih tinggi")
            return
        
        if difference_in_years >= 1:
            discount = 0.05

        new_price = new_plan.price - (new_plan.price * discount)

        self.list_user[self.username][0] = new_plan.plan_name
        self.list_user[self.username][2] = new_price
        self.list_user[self.username][3] = new_plan
        self.bill = new_price
        self.current_plan = new_plan

        return self.bill


    def generate_referral_code(self):
         # Generate a referral code for the user
         length = 8
         characters = string.ascii_letters + string.digits
         referral_code = ''.join(random.choice(characters) for i in range(length))

         return referral_code
    


    def referral(self, referral_code):
         # Check and apply referral discount
        if referral_code in self._User__list_referral_code.values():
            discount = 0.04
            new_price = self.current_plan.price - (self.current_plan.price * discount)
            
            self.list_user[self.username][2] = new_price
            self.bill = new_price
            return True, self.bill
        
        else:
            return False, "Referral code Anda tidak valid"
        

    def __str__(self):
        # Return a string representation of the user
        return tabulate([
            ['Username', self.username],
            ['Plan', self.current_plan.plan_name],
            ['Register Date', self.register_date],
            ['Last Bill', self.bill],
            ['Referral Code', self.referral_code]
        ])
    







# Example usage
# user1 = User("Bebek", basic_plan, date.today())
# # user2 = User("Alice Smith", standard_plan, date.today())
# # user3 = User("bubu", basic_plan, date.today())

# print(user1._User__list_referral_code)
# print("=====================")
# # print(user1.list_user)
# print(user1.list_user['John Doe'])
