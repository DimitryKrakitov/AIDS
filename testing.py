from jnos import *
from functions import *

def renai_circulation_teste(tup, full_counter):

    output = []
    print("Sentence:" + str(tup))

    jno = No(tup, 0)

    print("Sentence ID:")
    jno.id()

    jno = evaluator(jno)

    print("     Sentence final po output:" + str(jno.say_my_jnos()))



    return output

def evaluator(jno):

    for elem in jno.sons:

        if jno.t == "<=>":

            jno = equivalence3(jno)

        elif jno.t == "=>":

            jno = implication3(jno)

        elif jno.t == "=>":

            jno = negation3(jno)

        elif jno.t == "or":

            if jno.denied & (jno.t == "or" or jno.t == "and"):

                jno = senorMorgan(jno)

            elif jno.t == "or" & (jno.sons[0].t == "and"):

                jno = distributiva_RL_or(jno)

            elif jno.t == "or" & (jno.sons[1].t == "and"):

                jno = distributiva_LR_or(jno)

    return jno
