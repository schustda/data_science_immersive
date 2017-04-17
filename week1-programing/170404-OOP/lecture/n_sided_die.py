class Dice(object):


    def __init__(self,n_sides,side_up = 1):
        self.n_sides = n_sides
        self.side_up = side_up

    def roll(self):
        import random
        self.side_up = random.randint(1,self.n_sides)
        return self.side_up

    def compare(self,other):
        print (self.side_up, other.side_up)
        if self.side_up > other.side_up:
            return "Your dice is larger"
        elif self.side_up == other.side_up:
            return "Your dice is the same"
        elif self.side_up < other.side_up:
            return "Your dice is smaller"




if __name__ == '__main__':
    a = Dice(10)
    b = Dice(5)
    a.roll()
    b.roll()
    print (a.side_up)
    print (b.side_up)
    print (a.compare(b))
