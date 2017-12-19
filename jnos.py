from convFunctions import negation

class no:

    def __init__(self, tup, denied = False, dad=[]):

        self.denied = denied
        temp_tup = tup
        if temp_tup[0] == "not":
            self.denied = not denied
            tup = eval(str(negation(str(tup))))

        self.f = tup[0]
        self.sons = []

        if dad:
            self.d = dad

        if len(tup) > 1:
            for elem in tup[1:-1]:
                self.sons.append(elem)

