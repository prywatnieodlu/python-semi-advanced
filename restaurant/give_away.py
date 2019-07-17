from time import time,sleep

class GiveAway:

    @staticmethod
    def log(message):
        with open('GiveAway.log', 'a', encoding='utf-8')as f:
            f.write(message +'\n')

    def __init__(self, manager):
        self.manager = manager

    def call_customer(self, order):
        self.log('Give away: zaczynam wydawać zamówienie')
        sleep(3)
        self.log('Give away mówi: gotowe')
        self.customer_collected_order(order)

    def customer_collected_order(self, order):
        order.collected_at = time()
        self.manager.customer_collected_order(order)