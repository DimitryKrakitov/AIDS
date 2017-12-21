from functions import *

def renai_circulation_teste(tup, full_counter):

    print("Is tup a tuple? ", isinstance(tup,tuple))
    print(searcher(tup))


def searcher(tup): #searches for equivalences and implications

    aux = tup   #   ('f', A, B)
    print("Tuple we're at: ", tup)
    if isinstance(tup, tuple):
        print("Length: ", len(tup))
        if len(tup) == 3:
            if aux[0] == '<=>': #   search for equivalences
                print("tup is equivalence")
                new_tup = equivalence(tup)
            elif aux[0] == '=>':    #   search for implications
                print("tup is implication")
                new_tup = implication(tup)
            elif aux[0] == 'or':    #   search for distributive
                if isinstance(aux[1], tuple) and aux[1][0] == 'and':
                    print("tup is to be distributed from right to left")
                    new_tup = RL_dist(tup)
                elif isinstance(aux[2], tuple) and aux[2][0] == 'and':
                    print("tup is to be distributed from left to right")
                    new_tup = LR_dist(tup)
            else:
                print("Unknown sentence of size 3")
                exit(-3)
        elif len(tup) == 2:
            if tup[0] == 'not':
                pass
            else:
                print("Unknown sentence of size 2")
                exit(-2)
        else:
            print(tup + "is of invalid size")
            exit(-4)


    return(new_tup)