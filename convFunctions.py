def equivalence(a, b):
    data = []
    data.append(implication(a,b))
    data.append(implication(b,a))
    return data

def implication(a, b):
    return "[('not', '" + a + "'), '" + b + "']"

def negation(b):
    '''print('Tuple to be negated:')
    print(b)'''

    if "(" not in b:
        #b = "'" + b + "'"
        return ("('not', '" + b + "')")

    tup = eval(b)
    #if "(" not in b:
    print("tup length:", len(tup))
    if len(tup) == 3:
        #b = "'" + b + "'"
        return ("('not', " + b + ")")
    elif "not" in tup[0]:
        return str("'" + tup[1] + "'")#testar ver se isto faz sentido

    print("Implausible Deniability")
    exit(-2)
    #return ("('not', '" + b + "')")

def negration(a):
    b = str(a)
    if "(" not in b:
        return ("('not', " + b + ")")

    tup = eval(b)
    if "not" in tup[0]:
        return str("'" + tup[1] + "'")

def conjunction(a, b):
    data = []
    data.append("'" + a + "'")
    data.append("'" + b + "'")
    return data

def disjunction(a, b):
    return("['" + a + "', '" + b + "']")


def line_processor(tup, exp, full_counter):
    output = []
    if len(tup) == 3:
        if exp == "<=>":
            linha = equivalence(tup[1],tup[2])
            #output.extend(linha)

        elif exp == "=>":
            linha = implication(tup[1], tup[2])
            #output.append(linha)
        elif exp == "or":
            pass
            #output.append(disjunction(tup[1],tup[2]))
        elif exp == "and":
            pass
            #output.extend(conjunction(tup[1],tup[2]))
        else:
            print("Invalid expression  at line: ", full_counter)
    elif len(tup) == 2:
        if exp == "not":
            output.append(negation(str(tup[1])))
        else:
            print("Invalid expression  at line: ", full_counter)
    elif len(tup) == 1:
        output.append("'" + exp + "'")
    else:
        print("Invalid expression  at line: ", full_counter)

    callback(linha)


    print(linha)
    #if linha ==
    exit(-2)

    return output

def callback(linha):
    tup=eval(linha)
    exp=tup[0]
    print(tup)

    for elem in tup:
        pass