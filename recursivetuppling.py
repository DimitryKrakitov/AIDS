from jnos import *
from literalyPrinters import * sendhelp

'''def psycho_pass(tup, output):

    #linha = str(tup)
    exp = tup[0]

    linha2 = list(tup)
    #while rec(linha2):
    while "(" in str(linha2):
        for elemelon in linha2[1:-1]:
            l = list(elemelon)
            if l[0] == '<=>':


    return'''

def rec(linha2):
    for elemelon in linha2:
        if "(" in str(elemelon):
            return True
    return False

def ponderingSuicide(tup):

    pai = no(tup)

    genos = pai
    level = 0
    node_list = []
    while True:#criar a arvore

        level += level

        if genos.f == "<=>":

            node_list.extend(equivalence2(genos.sons[0], genos.sons[1])) #adicionar filhos como novos nos

        elif genos.f == "=>":

            node_list.extend(implication2(genos.sons[0], genos.sons[1]))#adicionar filhos como novos nos 

        '''for elem in genos:
            if elem'''

def equivalence2(a, b):
    data = []
    data.append(implication2(a, b))
    data.append(implication2(b, a))
    return data

def implication2(a, b):
    return "('or', " + str(negation(a)) + ", " + sendhelp(str(b)) + ")"






