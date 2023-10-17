
"""
### Class Plan
class plan is used to see all the plans in PacFlix

PacFlix Plans
1. Basic Plan
2. Standard Plan
3. Premium Plan

Benefit per Each Plan (Table)
Can call different .py

"""

from dataclasses import dataclass
import pandas as pd
from IPython.display import display, HTML


# Define a dataclass to represent a plan
@dataclass
class Plan:
    plan_name : str
    can_stream : bool
    can_download : bool
    has_SD : bool
    has_HD : bool
    has_UHD : bool
    num_of_device : int
    content : list
    price : int


    # Method to display plan details
    def check_plan(self):
        data = [
            ["Plan" , self.plan_name],
            ["Streaming" , 'v' if self.can_stream else '-'],
            ["Download" , 'v' if self.can_download else '-'],
            ["SD", 'v' if self.has_SD else '-'],
            ["HD" , 'v' if self.has_HD else '-'],
            ["UHD" , 'v' if self.has_UHD else '-'],
            ["Number of Devices" , self.num_of_device],
            ["Content" , self.content],
            ["price" , self.price],
        ]
        # Create a DataFrame
        df = pd.DataFrame(data, columns=["Service", "Detail"])
        return df


# Define various plans
basic_plan = Plan(
    plan_name = "Basic Plan",
    can_stream = True,
    can_download = True,
    has_SD = True,
    has_HD = False,
    has_UHD = False,
    num_of_device = 1,
    content = ["3rd Party Movie"],
    price = 120_000,
    )

standard_plan = Plan(
    plan_name = "Standard Plan",
    can_stream = True,
    can_download = True,
    has_SD = True,
    has_HD = True,
    has_UHD = False,
    num_of_device = 2,
    content = ["3rd Party Movie ", "Sports (F1, Football, Basketball)"],
    price = 160_000
    )

premium_plan = Plan(
    plan_name = "Premium Plan",
    can_stream = True,
    can_download = True,
    has_SD = True,
    has_HD = True,
    has_UHD = True,
    num_of_device = 4,
    content = ["3rd Party Movie ", "Sports (F1, Football, Basketball)", "PacFlix Original Series or Movie"],
    price = 200_000
    )

none = Plan(
    plan_name = "",
    can_stream = False,
    can_download = False,
    has_SD = False,
    has_HD = False,
    has_UHD = False,
    num_of_device = None,
    content = [None],
    price = None
    )



list_plan = [basic_plan, standard_plan, premium_plan]


# Checking the output
# x = none.check_plan()
# print(x)