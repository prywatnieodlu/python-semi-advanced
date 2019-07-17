from restaurant.kitchen import Kitchen


class Manager:

    def __init__(self, cash_desk, kitchen, give_away):
        self.cash_desk = cash_desk
        self.kitchen = kitchen
        self.give_away = give_away

    def new_order(self, order):
        self.prepare_meal(order)

    def prepare_meal(self, order):
        self.kitchen.prepare_meal(order)

    def meal_ready(self, order):
        self.call_customer(order)

    def call_customer(self, order):
        self.give_away.call_customer(order)

    def customer_collected_order(self, order):
        print(f'Order delivered', order.name)
