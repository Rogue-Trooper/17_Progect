class Account:

    # def __init__(self):
    #     self.id = 0
    #     self.balance = 0
    #     self.name = "no name"
    #     self.cofficient = 0.001

    # constructor with params
    def __init__(self, id, balance, name, cofficient=0.01):
        self.id = id
        self.balance = balance
        self.name = name
        self.cofficient = cofficient

    # destructor
    def __del__(self):
        pass

    def get_info(self):
        return (f"{self.id}: "
                f"balance = {self.balance}, "
                f"name = {self.name}, "
                f"cofficient = {self.cofficient}")
