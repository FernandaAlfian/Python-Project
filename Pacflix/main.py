from plan import *
from user import *



def new_user():
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


def check_all_plan():
    for plan in list_plan:
        print(f"Plan: {plan.plan_name}")
        print(plan.check_plan())
        print("\n")
    menu()

def check_current_plan():
    username = str(input("Enter your username: "))

    while True:
        if username in User.list_user:
def check_current_plan():
    username = str(input("Enter your username: "))

    while True:
        if username in User.list_user:
            user = User.list_user[username]
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


# for plan in list_plan:
#     print(plan.check_plan())

menu()
