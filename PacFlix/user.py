from plan import Plan
from plan import basic_plan, standard_plan, premium_plan
from plan import list_plan
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
import random
import string
from dataclasses import dataclass
from tabulate import tabulate


class User:

    redeem_list = {}

    def generate_secret_code(self):
        # Generate a random 6-character secret code
        self.secret_code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        return self.secret_code
    
    def __init__(self, username, choosen_plan, register_date):
        self.username = username
        self.current_plan = choosen_plan
        self.register_date = register_date
        self.bill = self.current_plan.price
        self.referal_code = self.username + "_" + self.generate_secret_code()
        self.redeem_list[self.username] = self.referal_code


    def upgrade_plan(self, new_plan):
        if new_plan.price <= self.current_plan.price:
            print(f"Anda tidak bisa melakukan upgrade. Pilih plan di atas {new_plan}")
            return
        
        today = date.today()
        discount = 1

        difference_years = relativedelta(today, self.register_date).years

        if difference_years >= 1: 
            discount = 0.95

        self.bill = new_plan.price * discount
        self.current_plan = new_plan
        return self.bill
        
    
    def redeem(self, redeem_code):
        if redeem_code in self.redeem_list.values():
            self.bill = self.current_plan.price * 0.96
            return True, self.bill
        else:
            return False,  "Referral Code Anda Tidak Valid"


    def check_all_plan(self):
        for plan in list_plan:
            plan.check_plan()
            print("\n")

    def __str__(self):
        return tabulate([
            ["Username", self.username],
            ["Plan", self.current_plan.name],
            ["Register Date", self.register_date],
            ["Price", self.bill],
            ["Referral Code", self.referal_code]
        ])

