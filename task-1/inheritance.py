class MobilePhone:
    def __init__(
        self,
        brand,
        screen_type,
        network_type,
        dual_sim,
        front_camera,
        rear_camera,
        ram,
        storage
    ):
        self.brand = brand
        self.screen_type = screen_type
        self.network_type = network_type
        self.dual_sim = dual_sim
        self.front_camera = front_camera
        self.rear_camera = rear_camera
        self.ram = ram
        self.storage = storage


    def make_call(self, number):
        print(f"{self.brand} calling {number}")


    def receive_call(self):
        print(f"{self.brand} receiving call")


    def take_picture(self):
        print(
            f"{self.brand} taking photo using {self.rear_camera} camera"
        )


    def show_details(self):
        print("\nMobile Details")
        print("----------------")
        print("Brand:", self.brand)
        print("Screen:", self.screen_type)
        print("Network:", self.network_type)
        print("Dual Sim:", self.dual_sim)
        print("Front Camera:", self.front_camera)
        print("Rear Camera:", self.rear_camera)
        print("RAM:", self.ram)
        print("Storage:", self.storage)



class Apple(MobilePhone):

    def __init__(
        self,
        front_camera,
        rear_camera,
        ram,
        storage
    ):

        super().__init__(
            "Apple",
            "Touch Screen",
            "5G",
            False,
            front_camera,
            rear_camera,
            ram,
            storage
        )


class Samsung(MobilePhone):

    def __init__(
        self,
        front_camera,
        rear_camera,
        ram,
        storage
    ):

        super().__init__(
            "Samsung",
            "Touch Screen",
            "4G/5G",
            True,
            front_camera,
            rear_camera,
            ram,
            storage
        )



iphone14 = Apple(
    "12MP",
    "48MP",
    "4GB",
    "64GB"
)


iphone12 = Apple(
    "8MP",
    "16MP",
    "3GB",
    "32GB"
)


samsung_s23 = Samsung(
    "16MP",
    "48MP",
    "4GB",
    "64GB"
)


samsung_a50 = Samsung(
    "8MP",
    "32MP",
    "3GB",
    "32GB"
)



phones = [
    iphone14,
    iphone12,
    samsung_s23,
    samsung_a50
]


for phone in phones:
    phone.show_details()
    phone.make_call("9876543210")
    phone.receive_call()
    phone.take_picture()