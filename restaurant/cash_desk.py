class CashDesk:

    def __init__(self, manager):
        self.manager = manager

    def new_order(self, order):
        self.manager.new_order(order) #cash_desk przekazuje order do menagera