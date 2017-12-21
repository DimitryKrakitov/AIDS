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

    if "[" not in b:
        #b = "'" + b + "'"
        return ("['not', '" + b + "']")

    tup = eval(b)
    #if "(" not in b:
    print("tup length:", len(tup))
    if len(tup) == 3:
        #b = "'" + b + "'"
        return ("['not', " + b + "]")
    elif "not" in tup[0]:
        return str("'" + tup[1] + "'")#testar ver se isto faz sentido

    print("Implausible Deniability")
    exit(-2)
    #return ("('not', '" + b + "')")

def negration(a):
    b = str(a)
    if "(" not in b:
        return ("['not', " + b + "]")

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
