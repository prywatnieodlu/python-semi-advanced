from time import time,ctime

class Order:
    def __init__(self, name):
        self.name = name
        self.created_at = time()
        self.ready_at = None
        self.collected_at = None

    def __str__(self)->str:
        return f'Order:{self.name}, {ctime(self.created_at)}, {self.ready_at}, {self.collected_at}'