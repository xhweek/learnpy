class Ticket:
    def __init__(self,ischild = False, weekend = False):
        self.tick = 100
        if ischild:
            self.discount = 0.5
        else:
            self.discount = 1

        if weekend:
            self.exp = 1.2
        else:
            self.exp = 1

    def cel_price(self,num):
        return self.tick * self.discount * self.exp * num

adult = Ticket()
child = Ticket(ischild=True)

print("money{}".format(adult.cel_price(2)+child.cel_price(1)))
