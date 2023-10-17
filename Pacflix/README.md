
# PacFlix - Python Project

## Project Objective
- Membuat simple program dari PacFlix
- Membuat fitur yang terdapat pada feature Requirements


## PacFlix Description
PacFlix adalah layanan platform video streaming yang memiliki 3 plan dengan benefit yang berbeda-beda.

| Service | Basic Plan  | Standard Plan  | Premium Plan  |
| ------- | --- | --- | --- |
| Streaming | &check; | &check; | &check;  |
| Download | &check; | &check; | &check;  |
| SD | &check; | &check; | &check;  |
| HD | - | &check; | &check;  |
| UHD | - | - | &check;  |
| Number of Devices | 1 | 2 | 4  |
| Content | 3rd Party Movies Only | 3rd Party Movies + Sports (F1, Football, Basketball) | 3rd Party Movie + Sports (F1, Football, Basketball PacFlix Original Series or Movies |
| Price | Rp 120.000 | Rp 160.000 | Rp 200.000  |



## Case Description
- User hanya dapat memilih satu dari plan yang disediakan
- User hanya dapat upgrade plan
- User bisa upgrade dari plan yang ada di atasnya
- Jika user yang sudah mendaftar di atas 12 bulan dan ingin melakukan upgrade maka akan mendapatkan diskon 5%
- Jika user baru memiliki kode referral yang valid maka akan mendapat diskon 4%



## Feature Requirements
- Dapat melihat semua plan yang tersedia di PacFlix dalam fitur check all plans
- Dapat melihat plan yang sedang digunakan oleh existing user
- Dapat melakukan upgrade plan dari existing user dan jika existing user sudah mendaftar lebih dari 12 bulan maka akan mendaptkan diskon
- New User akan mendapatkan diskon jika memiliki kode referral yang valid


## Flowchart
![Flowchart](https://github.com/FernandaAlfian/Python-Project/assets/98755428/6dac5ee6-4e45-4db1-82c3-e2702320a13e)




# Program Functions

Project ini memiliki 3 file, `1`plan.py`, `user.py`, `main.py`.
1. `plan.py`
    File ini berisi plan yang tersedia dalam PacFlix
2. `uesr.py`
    File ini berisi fungsi dari class User untuk dapat dipilih consumer pada main menu dan fungsi lain yang diperlukan untuk menjalankan program.
3. `main.py`
    File ini adalah file untuk menjalankan main menu dari PacFlix.

Berikut adalah penjelasan dari file di atas.

## Modul `plan.py`

Library yang digunakan dalam `plan.py`
```py
from dataclasses import dataclass
import pandas as pd
from IPython.display import display, HTML
```

Class Plan
```py
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
```

Method in `plan.py`
```py
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
```
Membuat list untuk dapat dipanggil dalam file lain
```py 
list_plan = [basic_plan, standard_plan, premium_plan]
```



## Modul `user.py`
Library yang digunakan dalam `user.py`
```py 
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
from plan import *
import random
import string
from plan import basic_plan, standard_plan, premium_plan
from plan import list_plan
from tabulate import tabulate
```

Class User
```py 
class User:

    __list_referral_code = {}
    list_user = {}
```

Method `__init__()`
```py 
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

```


Method `upgrade_plan()`
```py 
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

```


Method `referral()`
```py 
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
  
```

Method `__str__()`
```py 
    def __str__(self):
        # Return a string representation of the user
        return tabulate([
            ['Username', self.username],
            ['Plan', self.current_plan.plan_name],
            ['Register Date', self.register_date],
            ['Last Bill', self.bill],
            ['Referral Code', self.referral_code]
        ])

```



## Modul `user.py`

Library dalam user.py
```py
from plan import *
from user import *
```

Method `new_user()`
```py 
    username = input("Enter your username: ")

    while True:
        temp_plan = input("Choose a plan (basic/standard/premium): ").lower()

        if temp_plan == 'basic':
            temp_plan = basic_plan
            temp_plan_name = basic_plan.plan_name
            break

        elif temp_plan == 'standard':
            temp_plan = standard_plan
            temp_plan_name = standard_plan.plan_name 
            break

        elif temp_plan == 'premium':
            temp_plan = premium_plan
            temp_plan_name = premium_plan.plan_name
            break

        else:
            print("Plan tidak terdaftar")



    ref_code = input("Referral code (if any): ")

    if ref_code == '':
        ref_code = None

    user = User(username, temp_plan, date.today())
    User.list_user[username] = [temp_plan_name, date.today(), temp_plan.price, temp_plan]

    if ref_code is not None:
        valid, new_bill = user.referral(ref_code)

        if valid:
            print(f"Berhasil melakukan redeem kode referral, harga baru anda menjadi {new_bill}")
        else:
            print(temp_plan.price)


    print(user.__str__())
    menu()

```

Method `upgrade_user()`
```py 
def upgrade_user():
    username = str(input("Enter your username: "))

    while True:
        if username in User.list_user:
            break
        else: 
            "User not found"
            return
        
    new_plan_name = input("Enter your new plan(basic/standard/premium):")

    while True:
        if new_plan_name == 'basic':
            new_plan = basic_plan
            break
        elif new_plan_name == 'standard':
            new_plan = standard_plan
            break
        elif new_plan_name == 'premium':
            new_plan = premium_plan
            break
        else:
            print("Plan tidak terdaftar")
            return

    user = User.list_user[username]
    # print(User.list_user)
    user = User(username, User.list_user[username][3], User.list_user[username][1])
    old_plan = User.list_user[username][0]

    # print(f'\n Old Plan {User.list_user[username][3]} \n')
    user.upgrade_plan(new_plan)
    # print(f'\n New Plan {User.list_user[username][3]}')
    print(f"Berhasil merubah plan dari {old_plan} menjadi {User.list_user[username][0]}")

    print(user.__str__())
    menu()
```

Method `check_all_plan()`
```py 
def check_all_plan():
    for plan in list_plan:
        print(f"Plan: {plan.plan_name}")
        print(plan.check_plan())
        print("\n")
    menu()
```

Method `check_current_plan()`
```py 
def check_current_plan():
    username = str(input("Enter your username: "))

    while True:
        if username in User.list_user:
            print("-------------  ----------------")
            print(f"Username       {username}")
            print(f"Plan           {user[0]}")
            print(f"Register Date  {user[1]}")
            print(f"Last Bill      {user[2]}")
            print("-------------  ----------------")
            break
        else: 
            print("User not found")
            username = str(input("Enter your username: "))
        

    
    menu()
```

Method `##()`
```py 
    def __str__(self):
        # Return a string representation of the user
        return tabulate([
            ['Username', self.username],
            ['Plan', self.current_plan.plan_name],
            ['Register Date', self.register_date],
            ['Last Bill', self.bill],
            ['Referral Code', self.referral_code]
        ])

```

Method `menu()`
```py 


def menu():
    print("\n------------ PacFlix -------------")
    print("\n------------ App Menu --------------")
    print("""
    1. Check All Plans & Benefit
    2. Upgrade Plan
    3. New User
    4. Check Current Plan
    5. Exit
    """)
    print("----------------------------------------\n")


    while True:
        fitur = int(input("Pilih menu yang ingin dipilih: "))
        if fitur <= 0 or fitur >= 6:
            print("Mohon agar dapat diisi angka pada menu")
            continue
        else:
            break
        

    if fitur == 1:
        check_all_plan()

    elif fitur == 2:
        upgrade_user()

    elif fitur == 3:
        new_user()

    elif fitur == 4: 
        check_current_plan()
        

    elif fitur == 5: 
        exit()
        return
```
# Test Case

Pada tahap ini akan dilakukan test code, untuk dapat melihat output yang dikeluarkan sudah sesuai dengan ekspektasi yang diinginkan.

Test

1. User ingin melihat plan apa saja yang tersedia di PacFlix.

    Expected Output:


    | Service | Basic Plan  | Standard Plan  | Premium Plan  |
    | ------- | --- | --- | --- |
    | Streaming | &check; | &check; | &check;  |
    | Download | &check; | &check; | &check;  |
    | SD | &check; | &check; | &check;  |
    | HD | - | &check; | &check;  |
    | UHD | - | - | &check;  |
    | Number of Devices | 1 | 2 | 4  |
    | Content | 3rd Party Movies Only | 3rd Party Movies + Sports (F1, Football, Basketball) | 3rd Party Movie + Sports (F1, Football, Basketball PacFlix Original Series or Movies |
    | Price | Rp 120.000 | Rp 160.000 | Rp 200.000  |

    
    Output Realization:
   
    ![Screenshot 2023-10-17 165649](https://github.com/FernandaAlfian/Python-Project/assets/98755428/cbd8e1a1-582f-442f-afa3-590f41d9920d)

3. User ingin mendaftar user di PacFlix dan memilih Basic Plan dengan menggunakan referral code


    Input:
    ```
    Username, plan, referral code
    ```

    Expected Output:

    ```
    Total yang harus dibayarkan
    ```

    Output Realization:
   
    ![Screenshot 2023-10-17 165739](https://github.com/FernandaAlfian/Python-Project/assets/98755428/d7f70429-6e12-4698-9965-64d57cdc945b)


4. User ingin melakukan upgrade plan dan sudah lebih dari 12 bulan.

    Input:
    ```
    Username, plan, new plan
    ```

    Expected Output:

    ```
    Total yang harus dibayarkan
    ```

    Output Realization:
   
    ![Screenshot 2023-10-17 165809](https://github.com/FernandaAlfian/Python-Project/assets/98755428/18ada3ba-45dd-411e-ab82-97fe9b0b0fa3)



5. User ingin melihat plan yang sedang user gunakan

    Input:
    ```
    Username
    ```

    Expected Output:

    ```
    Username, Plan yang sedang digunakan, Register Date, Bill
    ```

    Output Realization:
   
    ![Screenshot 2023-10-17 181340](https://github.com/FernandaAlfian/Python-Project/assets/98755428/474469fe-dbd6-43ce-9982-2b24274fe44d)



# Conclution
Berdasarkan requrements yang ada pada promblem case PacFlix ini, seluruh requremetns dapat dijalankan sesuai dengan ekspetkasi yang diinginkan, dan terdapat pernyesuaian dalam pengerjaannya untuk dapat lebih mempermudah consumer dalam menggunakan program PacFlix ini. Program sederhana ini dapat digunakan, dan masih dapat dilakukan pengembangan di kemudian hari.



# Future Development
1. Agar dapat juga menggunakan Graphic User Interface agar tampilan lebih interaktif
