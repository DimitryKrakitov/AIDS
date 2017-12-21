from convFunctions import *
from recursivetuppling import *

def line_processor_easy(tup, full_counter):
    linha = []
    exp = tup[0]
    if len(tup) == 3:
        if exp == "<=>":
            linha.extend(equivalence(tup[1],tup[2]))
            #output.extend(linha)

        elif exp == "=>":
            linha.extend(implication(tup[1], tup[2]))
            #output.append(linha)
        elif exp == "or":
            linha.extend(disjunction(tup[1], tup[2]))
            #output.append(linha)
        elif exp == "and":
            linha.extend(conjunction(tup[1],tup[2]))
            #output.extend(linha)
        else:
            print("Invalid expression  at line: ", full_counter)
    elif len(tup) == 2:
        if exp == "not":
            linha.extend(negation(str(tup[1])))
            #output.append(linha)
        else:
            print("Invalid expression  at line: ", full_counter)
    elif len(tup) == 1:
        linha.append("'" + exp + "'")
    else:
        print("Invalid expression  at line: ", full_counter)

    return linha

def renai_circulation(tup, full_counter):

    output = []
    for elemelon in tup:
        if "(" in str(elemelon):
            #output.extend(line_processor_hard(tup, output, full_counter))
            output.extend(ponderingSuicide(tup, output, full_counter))
    output.extend(line_processor_easy(tup, full_counter))

    return output


def line_processor_hard(tup, output, full_counter):
    linha = []
    exp = tup[0]
    if len(tup) == 3:
        if exp == "<=>":
            linha.extend(equivalence(tup[1],tup[2]))
            #output.extend(linha)

        elif exp == "=>":
            linha.extend(implication(tup[1], tup[2]))
            #output.append(linha)
        elif exp == "or":
            linha.extend(disjunction(tup[1], tup[2]))
            #output.append(linha)
        elif exp == "and":
            linha.extend(conjunction(tup[1],tup[2]))
            #output.extend(linha)
        else:
            print("Invalid expression  at line: ", full_counter)
    elif len(tup) == 2:
        if exp == "not":
            linha.extend(negration(str(tup[1])))
            #output.append(linha)
        else:
            print("Invalid expression  at line: ", full_counter)
    elif len(tup) == 1:
        output.append("'" + exp + "'")
    else:
        print("Invalid expression  at line: ", full_counter)

    #print(linha)

    return output