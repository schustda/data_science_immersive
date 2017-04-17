class PMF(object):

    def __init__(self, values):
        self.values = values

    def prob(self, value):
        print (self.values[value])

    def print_pmf(self):
        print ([(a,round(b,3)) for a,b in self.values.items()])

    def set(self,tuple):
        for a,b in self.values.items():
            self.values[a] = b*(1 - tuple[1])/(1 - self.values[tuple[0]])
        self.values[tuple[0]] = tuple[1]

if __name__ == '__main__':
    die = PMF({"1": 1./6, "2": 1./6, "3": 1./6, "4": 1./6, "5": 1./6, "6": 1./6 })
    die.prob("3")
    die.print_pmf()
    die.set(("2", 1/2))
    die.print_pmf()
