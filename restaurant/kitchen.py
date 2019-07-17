from time import time, sleep


class Kitchen:

    @staticmethod
    def log(message):
        with open('kitchen.log', 'a', encoding='utf-8')as f:
            f.write(message +'\n')

    def __init__(self, manager):
        self.manager = manager

    def prepare_meal(self, order):
        self.log('Kuchnia: rozpoczynam przygotowanie')
        sleep(5)
        self.log('z Kuchnia gotowe!')
        self.meal_ready(order)

    def meal_ready(self, order):
        order.ready_at = time()
        self.manager.meal_ready(order)

