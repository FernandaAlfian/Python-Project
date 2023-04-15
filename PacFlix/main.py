from plan import Plan
from plan import basic_plan, standard_plan, premium_plan
from plan import list_plan
from user import *
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
import random
import string
from dataclasses import dataclass
from tabulate import tabulate




number_user = int(input("Input number of user want to create: "))

list_user = []

for i in range(number_user):
    user_name = input("Input New Username: ")
    user_plan = input("Choose a Plan (Basic, Standard, Premium) ").lower()
    ref_code  = input("Input Referral Code: ")

    temp_plan = None
    try:
        if user_plan == "basic":
            temp_plan = basic_plan
        elif user_plan == "standard":
            temp_plan = standard_plan
        elif user_plan == "premium":
            temp_plan = premium_plan
        else:
            raise Exception("Input Correct Plan")

    except Exception as e:
        print(e)

    else:
        user = User(user_name, temp_plan, date.today())
        list_user.append(user)
        if ref_code != '':
            valid, message = user.redeem(ref_code)
            if valid:
                print(f"Anda berhasil melakukan reedem, tagihan anda sebesar {message}")
            else:
                print(message)
        print(user)
list_user