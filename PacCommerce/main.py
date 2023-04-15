from tabulate import tabulate
from math import sqrt


class Membership:

    # Defines and stores membership information in three dictionaries

    user_data = {
        'Sumbul': 'Platinum', 
        'Ana': 'Gold', 
        'Cahya': 'Platinum'
        }


    table_memberships = {
        "Platinum" : ["Platinum", 15, "Voucher Makanan, Voucher Ojek Online, Voucher Liburan, Cashback Max. 30%"],
        "Gold" : ["Gold", 10, "Voucher Makanan, Voucher Ojek Online"],
        "Silver" : ["Silver", 8, "Voucher Makanan"]
        }
    

    table_requirements = {
        "Platinum" : ["Platinum", 8, 15],
        "Gold" : ["Gold", 6, 10],
        "Silver" : ["Silver", 5, 7]
        }

    
    def __init__(self, username):
        """
        Constructor method for the Membership class.
        Initializes the username and user_data dictionary with the provided username.
        """

        self.username = username
        self.user_data[username] = ""


    def check_all_memberhsip(self):
        """
        Method to display all membership details in a tabulated format.
        Prints the membership details, including membership name, discount percentage, and benefits,
        using the table_memberships dictionary and the tabulate library.
        """

        headers = ["Membership", "Discount %", "Benefits"]
        table = [value for key, value in self.table_memberships.items()]
        print(tabulate(table, headers, tablefmt="pretty"))


    def check_requirements(self):
        """
        Method to display all membership requirements in a tabulated format.
        Prints the membership requirements, including membership name, monthly expense, and monthly income,
        using the table_requirements dictionary and the tabulate library.
        """
            
        headers = ["Membership", "Monthly Expence", "Monthly Income"]
        table = [value for key, value in self.table_requirements.items()]
        print(tabulate(table, headers, tablefmt="pretty"))


    def predict_membership(self, username, monthly_expense, monthly_income):
        """
        Method to predict the membership type for a given user based on their monthly expense and monthly income.
        Calculates the Euclidean Distance between the given monthly expense and income with the requirements
        in the table_requirements dictionary to determine the closest membership type.
        Updates the user_data dictionary with the predicted membership type for the given user.
        Returns the predicted membership type.
        """

        distance = {}

        for key, value in self.table_requirements.items():
            pred =  round(sqrt((monthly_expense - value[1])**2 + (monthly_income - value[2])**2), 2)
            distance[key] = pred

        print(f"Hasil perhitungan Euclidean Distance dari {username} adalah {distance}")
        

        for key, value in distance.items():
            if value == min(distance.values()):
                self.user_data[username] = key
                return key
            

    def calculate_bill(self, username, list_transaction):
        """
        Method to calculate the bill for a given user based on their list of transactions.
        Calculates the total amount from the list of transactions.
        Applies discount based on the membership type retrieved from the user_data dictionary.
        Returns the calculated bill amount after applying the discount.
        Raises exceptions for cases where the username is not found in the user_data dictionary
        or the membership type is not predicted for the given user.
        """

        total = sum(list_transaction)

        try:
            if username in self.user_data.keys():
                membership_type = self.user_data[username]
                if membership_type != '':
                    discount = self.table_memberships[membership_type][1] / 100
                    return total * (1 - discount)
                else:
                    raise Exception("Lakukan prediksi membership pada user {username}")
            
            else:
                raise Exception(f"User {username} tidak ditemukan")

        except Exception as e:
            print(e)


    def check_membership(self, username):
        if username in self.user_data.keys():
            return self.user_data[username]
    


        
