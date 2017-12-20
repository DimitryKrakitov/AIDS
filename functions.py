from convFunctions import negation
from jnos import *
from literalyPrinters import sendhelp

# no.t[0] == "<=>"
def equivalence3(jno):  #   A <=> B -> (!A V B) ^ (!B V A)

    '''temp_jno = No()

    temp_jno.sons[0] = No.sons[1]
    temp_jno.sons[1] = No.sons[0]'''
    return No(["and", implication3(jno), implication4(jno)], jno.denied, jno.d)


def implication3(jno): #   A => B -> (!A V B)
    #return eval("['or', " + str(negation(a)) + ", " + sendhelp(str(b)) + "]")

    return No(['or', negation3(jno.sons[0]), jno.sons[1]], jno.denied, jno.d)

def implication4(jno): #   A <= B -> (!B V A)
    #return eval("['or', " + str(negation(b)) + ", " + sendhelp(str(a)) + "]")

    return No(['or', negation3(jno.sons[1]), jno.sons[0]], jno.denied, jno.d)

def negation3(jno):

    jno.denied = not jno.denied
    return jno

#if no.denied & (no.t[0] == "or" or no.t[0] == "and"

def senorMorgan(jno):

    jno.denied = not jno.denied

    if jno.t[0] == "or":
        jno.t[0] = "and"
    else:
        jno.f = "or"

    jno.sons[0] = negation3(jno.sons[0])
    jno.sons[1] = negation3(jno.sons[1])


#if no.t[0] == "or" & no.sons[0].t[0] == "and"
def distributiva_RL_or(jno):    #   (A^B) V C -> (C V A) ^ (C V B)

    temp_jnos = []

    temp_jnos[0] == "and"
    temp_jnos[1] == ["or", jno.t[2], jno.sons[0].t[1]]
    temp_jnos[2] == ["or", jno.t[2], jno.sons[0].t[2]]

    return No(temp_jnos, jno.denied, jno.dad)


def distributiva_LR_or(jno):    #   C V (A^B) -> (C V A) ^ (C V B)
    temp_jnos = []

    temp_jnos[0] == "and"
    temp_jnos[1] == ["or", jno.t[1], jno.sons[1].t[1]]
    temp_jnos[2] == ["or", jno.t[1], jno.sons[1].t[2]]

    return No(temp_jnos, jno.denied, jno.dad)


def distributiva_RL_AND(jno):  # (A V B) ^ C -> (C^A) V (C^B)

    temp_jnos = []

    temp_jnos[0] == "or"
    temp_jnos[1] == ["and", jno.t[2], jno.sons[0].t[1]]
    temp_jnos[2] == ["and", jno.t[2], jno.sons[0].t[2]]

    return No(temp_jnos, jno.denied, jno.dad)


def distributiva_LR_AND(jno):  # C ^(A V B) -> (C^A) V (C^B)

    temp_jnos = []

    temp_jnos[0] == "or"
    temp_jnos[1] == ["and", jno.t[1], jno.sons[1].t[1]]
    temp_jnos[2] == ["and", jno.t[1], jno.sons[1].t[2]]

    return No(temp_jnos, jno.denied, jno.dad)
