from convFunctions import negation
from literalyPrinters import sendhelp

class No:

    def __init__(self, lista, lvl, denied = False, dad = None, debug = False):

        self.lvl = lvl + 1
        self.denied = denied
        temp_tup = lista

        self.sons = []
        self.d = dad

        self.lit = False

        #print("No(?) indexado é:", str(temp_tup))

        if isinstance(lista,No) & False:
            if debug:
                print("Cabeça do No (literal):", lista.t)
            self.t = lista.t
            self.lit = True

        else:

            if debug:
                print("Cabeça do No (sentence):", lista[0])
            if temp_tup[0] == "not":
                self.denied = not denied
                #lista = eval(negation(str(lista)))


            #self.t = sendhelp(str(lista[0]))
            self.t = lista[0]



            if len(lista) == 2:

                #self.sons.append(No(list(eval(sendhelp(str(lista[1])))), not self.denied, self))
                self.sons.append(No(lista[1], self.lvl, not self.denied, self))

            if len(lista) > 2:
                for elem in lista[1:]:

                    if debug:
                        s = elem.say_my_jnos()

                        #print("Is " + s + "a string? - " + str(isinstance(s, str)))
                        print("Filho do no:", s)

                    if isinstance(elem, No):
                        print("son is literal")
                        #self.sons.append(No(eval(s), self.lvl, self.denied, self))
                        self.sons.append(No(elem, self.lvl, self.denied, self))

                    else:
                        print("son is sentence")
                        #self.sons.append(No(list(eval(sendhelp(str(elem)))), self.denied, self))
                        self.sons.append(No(list(elem), self.lvl, self.denied, self))

            #self.id()

    def say_my_jnos(self):

        tony_wonder = []

        #if (not self.lit):# & (self.sons):
        if self.sons:
            #print("River Song was here")
            tony_wonder.append(str(self.t))
            for elem in self.sons:
                '''a = []
                a.append(str(elem.t))'''
                tony_wonder.append(str(elem.say_my_jnos()))
            return str(tony_wonder)

        #print("River Song was NOT here")

        #return "'" + str(self.t[0]) + "'"
        #return str(self.t[0])
        return str(str(self.t) + "(literal)")

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


