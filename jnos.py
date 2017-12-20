from convFunctions import negation
from literalyPrinters import sendhelp

class No:

    def __init__(self, lista, lvl, denied = False, dad = None):

        self.lvl = lvl + 1
        self.denied = denied
        temp_tup = lista
        if temp_tup[0] == "not":
            self.denied = not denied
            #lista = eval(negation(str(lista)))


        #self.t = sendhelp(str(lista[0]))
        self.t = lista[0]
        self.sons = []

        #if dad:
        self.d = dad


        if len(lista) == 2:

            #self.sons.append(No(list(eval(sendhelp(str(lista[1])))), not self.denied, self))
            self.sons.append(No(lista[1], self.lvl, not self.denied, self))

        if len(lista) > 2:
            for elem in lista[1:]:
                #self.sons.append(No(list(eval(sendhelp(str(elem)))), self.denied, self))
                self.sons.append(No(elem, self.lvl, self.denied, self))

        #self.id()

    def say_my_jnos(self):

        tony_wonder = []
        if self.sons:
            #print("River Song was here")
            tony_wonder.append(str(self.t))

            for elem in self.sons:
                '''a = []
                a.append(str(elem.t))'''
                tony_wonder.append(str(elem.say_my_jnos()))
            return tony_wonder

        #print("River Song was NOT here")

        #return "'" + str(self.t[0]) + "'"
        return str(self.t[0])

    def id(self):

        print(" Node: ",  str(self.say_my_jnos()))
        print(" Level: ", self.lvl)
        if self.d:
            print("     Parent:", str(self.d.say_my_jnos()))
        else:
            print("No Parent.")
        if self.sons:
            print("     Sons:")
            for elem in self.sons:
                print("Son:", str(elem.say_my_jnos()))
        else:
            print("No sons.")


