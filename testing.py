from jnos import *
from functions import *

def renai_circulation_teste(tup, full_counter):

    output = []
    print("Sentence:" + str(tup))

    jno = No(tup, 0)

    print("Sentence ID:")
    jno.id()

    jno = evaluator(jno)

    print("Sentence:" + str(jno.say_my_jnos()))



    return output

def evaluator(jno):

    for elem in jno.sons:

        if jno.t == "<=>":

            print("Detected equivalence")
            jno = equivalence3(jno)

        elif jno.t == "=>":

            print("Detected implication")
            jno = implication3(jno)

        elif jno.t == "=>":

            print("Detected Niggation")
            jno = negation3(jno)

        elif jno.t == "or":

            if jno.denied & (jno.t == "or" or jno.t == "and"):

                print("Detected deMorgan")
                jno = senorMorgan(jno)

            elif jno.t == "or" & (jno.sons[0].t == "and"):

                print("Detected distributiva Right to Left")
                jno = distributiva_RL_or(jno)

            elif jno.t == "or" & (jno.sons[1].t == "and"):

                print("Detected distributiva Left to Right")
                jno = distributiva_LR_or(jno)

    return jno
