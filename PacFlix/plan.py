from dataclasses import dataclass
from tabulate import tabulate


@dataclass
class Plan:
    name: str
    can_stream: bool
    can_download: bool
    has_SD: bool
    has_HD: bool
    has_UHD: bool
    num_of_devices: int
    content: list
    price: int

    def check_plan(self):
        all_plan = [
                ["Services", "Detail"],
                ["Plan Name", self.name],
                ["Streaming", 'v' if self.can_stream else '-'],
                ["Download", 'v' if self.can_download else '-'],
                ["SD Quality", 'v' if self.has_SD else '-'],
                ["HD Quality", 'v' if self.has_HD else '-'],
                ["UHD Quality", 'v' if self.has_UHD else '-'],
                ["Number of Devices", self.num_of_devices],
                ["Content", self.content],
                ["Price", self.price]
        ]
        print(tabulate(all_plan, headers="firstrow", tablefmt="pretty"))



basic_plan = Plan(
        name = 'Basic Plan',
        can_stream = True,
        can_download = True,
        has_SD = True,
        has_HD = False,
        has_UHD = False,
        num_of_devices = 1,
        content = ['3rd Party Movie Only'],
        price = 120_000
)

standard_plan = Plan(
        name = 'Standard Plan',
        can_stream = True,
        can_download = True,
        has_SD = True,
        has_HD = True,
        has_UHD = False,
        num_of_devices = 1,
        content = ['3rd Party Movie Only', 'Sports(F1, Football, Basketball)'],
        price = 160_000
)

premium_plan = Plan(
        name= 'Premium Plan',
        can_stream= True,
        can_download= True,
        has_SD= True,
        has_HD= True,
        has_UHD= True,
        num_of_devices= 5,
        content= ['3rd Party Movie Only', 'Sports (F1, Football, Basketball)', 'PacFlix Original Series of Movie'],
        price= 200_000
)

list_plan = [basic_plan, standard_plan, premium_plan]

