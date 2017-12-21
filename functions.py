from convFunctions import negation
from jnos import *
from literalyPrinters import sendhelp

# no.t[0] == "<=>"
def equivalence3(jno):  #   A <=> B -> (!A V B) ^ (!B V A)

    print("             Detected equivalence")
    print("             No detectado:", jno.say_my_jnos())

    '''temp_jno = No()

    temp_jno.sons[0] = No.sons[1]
    temp_jno.sons[1] = No.sons[0]'''
    print("jno: ", jno.say_my_jnos())
    jno.id()
    jnoa = No(["=>", jno.sons[0],  jno.sons[1]], jno.lvl, jno.denied, jno, debug = True)
    print("jnoa: ", jnoa.say_my_jnos())
    jnoa.id()
    jnoa2 = implication3(jnoa)
    print("jnoa2: ", jnoa2.say_my_jnos())
    #jnob = No(["=>", jno.sons[1],  jno.sons[0]], jno.lvl, jno.denied, jno, debug = True)
    #jno2 = No(["and", implication3(jnoa), implication3(jnob)], jno.lvl, jno.denied)
    print("             No processado na equivalencia:", jno2.say_my_jnos())

    return jno2

def implication3(jno): #   A => B -> (!A V B)
    #return eval("['or', " + str(negation(a)) + ", " + sendhelp(str(b)) + "]")
    '''print("Sentence ID (son in implication):")
    negation3(jno.sons[0]).id()'''

    print("         Detected implication")
    print("         No detectado:", jno.say_my_jnos())
    jno.id()

    print("         Filho 1 de jno na primeira implicação:", negation3(jno.sons[0]).say_my_jnos())

    jno2 = No(['or', negation3(jno.sons[0]), jno.sons[1]], jno.lvl, jno.denied, jno, True)
    print("         Filho 1 de jno2 na primeira implicação:", jno2.sons[0].say_my_jnos())
    print("         No processado na implicação:", jno2.say_my_jnos())
    jno2.id()
    return jno2

def implication4(jno): #   A <= B -> (!B V A)
    #return eval("['or', " + str(negation(b)) + ", " + sendhelp(str(a)) + "]")

    print("         Detected implication (from equivalence)")
    print("         No detectado:", jno.say_my_jnos())
    jno.id()

    jno2 = No(['or', negation3(jno.sons[1]), jno.sons[0]], jno.lvl, jno.denied, jno.d)
    print("         No processado na implicação2:", jno2.say_my_jnos())
    jno2.id()

    return jno2

def negation3(jno):

    '''print("Detected Niggation")
    print("No detectado:", jno.say_my_jnos())'''

    jno.denied = not jno.denied
    return jno

#if no.denied & (no.t[0] == "or" or no.t[0] == "and"

def senorMorgan(jno):

    print("     Detected deMorgan")
    print("     No detectado:", jno.say_my_jnos())
    jno.denied = not jno.denied

    if jno.t[0] == "or":
        jno.t[0] = "and"
    else:
        jno.f = "or"

    jno.sons[0] = negation3(jno.sons[0])
    jno.sons[1] = negation3(jno.sons[1])

    print("     No processado no morgan:", jno.say_my_jnos())


#if no.t[0] == "or" & no.sons[0].t[0] == "and"
def distributiva_RL_or(jno):    #   (A^B) V C -> (C V A) ^ (C V B)

    print(" Detected distributiva Right to Left")
    print(" No detectado:", jno.say_my_jnos())


    temp_jnos = []

    temp_jnos[0] == "and"
    temp_jnos[1] == ["or", jno.t[2], jno.sons[0].t[1]]
    temp_jnos[2] == ["or", jno.t[2], jno.sons[0].t[2]]

    jno2 = No(temp_jnos, jno.lvl, jno.denied, jno.dad)
    print(" No processado na dist RL:", jno2.say_my_jnos())
    return jno2


def distributiva_LR_or(jno):    #   C V (A^B) -> (C V A) ^ (C V B)
    temp_jnos = []

    print(" Detected distributiva Left to Right")
    print(" No detectado:", jno.say_my_jnos())

    temp_jnos[0] == "and"
    temp_jnos[1] == ["or", jno.t[1], jno.sons[1].t[1]]
    temp_jnos[2] == ["or", jno.t[1], jno.sons[1].t[2]]

    jno2 = No(temp_jnos, jno.lvl, jno.denied, jno.dad)
    print(" No processado na dist LR:", jno2.say_my_jnos())
    return jno2


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
