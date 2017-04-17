class Fraction(object):
    ''' Makes a fraction object '''

    def __init__(self, num = 0, denom = 1):
        ''' runs when object instantiated '''
        self.num = num
        self.denom = denom

    def __repr__(self):
        ''' tells python how to represent the object '''
        return "{0}/{1}".format(self.num,self.denom)

    def add(self, other):
        ''' defines the add function '''
        if self.denom == other.denom:
            return Fraction(self.num + other.num, self.denom)
        else:
            print ("The denominators don't match.  Impossible!")
            return None

    def __add__(self, other):
        new_num = (self.num * other.denom) + (other.num * self.denom)
        new_denom = (self.denom * other.denom)
        return Fraction(new_num,new_denom)

if __name__ == '__main__':
    f1 = Fraction(num = 5, denom = 8)
    f2 = Fraction(num = 1, denom = 3)
    print (f1 + f2)

    # What attributes will a Fraction object have?

    # Can I display a Fraction object?  Why or why not?

    # If I uncomment all the code, what methods will a Fraction object have?

    # What could be done to allow adding fractions with different denominators?
