from jnos import *
from literalyPrinters import sendhelp

def rec(linha2):
    for elemelon in linha2:
        if "(" in str(elemelon):
            return True
    return False

def renai_circulation(tup, full_counter):

    output = []
    for elemelon in tup:
        if "(" in str(elemelon):
            #output.extend(line_processor_hard(tup, output, full_counter))
            output.extend(ponderingSuicide(tup, output, full_counter))
    #output.extend(line_processor_easy(tup, full_counter))

    return output


def ponderingSuicide(tup):
    pai = no(tup)

    genos = pai
    level = 0
    node_list = []
    while True:  # criar a arvore

        level += level

        if genos.f == "<=>":

            node_list.extend(equivalence2(genos.sons[0], genos.sons[1]))  # adicionar filhos como novos nos

        elif genos.f == "=>":

            node_list.extend(implication2(genos.sons[0], genos.sons[1]))  # adicionar filhos como novos nos

        '''for elem in genos:
            if elem'''