from functions import *

'''tup_to_cnf: function that receives a line in the form
of a tuple and keeps calling the function (searcher) that transforms this
sentence into CNF form until said form is reached'''


def tup_to_cnf(tup):
    # print("Is tup a tuple? ", isinstance(tup,tuple))

    # new_line = []
    # print("\0")

    new_tup = searcher(tup)
    while isinstance(new_tup, tuple) and (new_tup[0] is not 'and') and ('and' in str(new_tup[1:])):
        new_tup = searcher(new_tup)

    # print("     CNF form of line:", new_tup)
    # new_line.append(new_tup)
    return new_tup


'''CNFer: checks if the operator of the sentence is an "and". If it is,
it breaks said sentence into 2'''


def CNFer(tup):
    new_line = []
    new_tup = tup_to_cnf(tup)

    '''print("function:", )
    print("Is funcion an 'and'?", tup[0] == 'and')'''
    if isinstance(new_tup, tuple) and new_tup[0] == 'and':
        # print("Line broken in 2")
        new_line.extend(CNFer(new_tup[1]))
        new_line.extend(CNFer(new_tup[2]))
    else:
        # print("CNF line to print")
        new_line.append(new_tup)

    return new_line


'''searcher: function that searches the tuple recursively (in tree-form)
looking for any situations that defy the CNF form. When such situation
is arrived upon, it calls the right function to deal with that specific situation,
 to turn that portion of the sentence into something that follows the CNF norm'''


def searcher(tup):  # searches for equivalences and implications

    aux = tup  # ('f', A, B)
    # print("Tuple we're at: ", tup)
    # print("Negation of tuple is: ", negation(tup))
    if isinstance(tup, tuple):
        # print("Length: ", len(tup))
        if len(tup) == 3:
            if aux[0] == '<=>':  # search for equivalences
                # print("tup is equivalence")
                new_tup = equivalence(tup)
            elif aux[0] == '=>':  # search for implications
                # print("tup is implication")
                new_tup = implication(tup)
            elif aux[0] == 'or':  # search for distributive
                if isinstance(aux[1], tuple) and aux[1][0] == 'and':
                    # print("tup is to be distributed from right to left")
                    new_tup = RL_dist(tup)
                elif isinstance(aux[2], tuple) and aux[2][0] == 'and':
                    # print("tup is to be distributed from left to right")
                    new_tup = LR_dist(tup)
                else:
                    # print("tup is regular 'or' sentence")
                    new_tup = tup
            elif aux[0] == 'and':
                # print("tup is regular 'and' sentence")
                new_tup = tup

            else:
                print("Unknown sentence of size 3")
                exit(-3)
        elif len(tup) == 2:
            if tup[0] == 'not':
                if isinstance(tup[1], tuple):
                    if tup[1][0] == 'or':
                        # print("tup is deMorgan or to and")
                        new_tup = deMorgan_or_and(tup)
                    elif tup[1][0] == 'and':
                        # print("tup is deMorgan and to or")
                        new_tup = deMorgan_and_or(tup)
                    elif tup[1][0] == 'not':
                        new_tup = tup[1][1]
                    else:
                        print("Unexpected negated sentence")
                        new_tup = searcher(negation(searcher(negation(tup))))

                        # print("Unexpected error in negated sentence")
                        # exit(-2)
                else:
                    # print("Negated literal")
                    return tup

            else:
                print("Unknown sentence of size 2")
                exit(-2)
        else:
            print(tup + "is of invalid size")
            exit(-4)
    else:
        # print(tup + " is a literal")
        return tup
    if len(new_tup) == 3:
        new_tup = (new_tup[0], searcher(new_tup[1]), searcher(new_tup[2]))
        '''if isinstance(new_tup[1], tuple):
            new_tup = (new_tup[0], searcher(new_tup[1]), new_tup[2])
        if isinstance(new_tup[2], tuple):
            new_tup = (new_tup[0], new_tup[1], searcher(new_tup[2]))'''

    return (new_tup)
