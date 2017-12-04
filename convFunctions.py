def equivalence(a, b):
    data = []
    data.append(implication(a,b))
    data.append(implication(b,a))
    return data

def implication(a, b):
    return "[('not', '" + a + "'), '" + b + "']"

def negation(a):
    '''print('Tuple to be negated:')
    print(a)'''
    tup = eval(a)
    if "not" in tup[0]:
        return str("'" + tup[1] + "'")#testar ver se isto faz sentido
    return ("[('not', " + a + ")]")


def conjunction(a, b):
    data = []
    data.append("'" + a + "'")
    data.append("'" + b + "'")
    return data

def disjunction(a, b):
    return("['" + a + "', '" + b + "']")
