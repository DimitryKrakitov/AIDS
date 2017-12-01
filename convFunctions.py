def equivalence(a, b):
    data = []
    data.append(implication(a,b))
    data.append(implication(b,a))
    return data

def implication(a, b):
    return "[('not', '" + a + "'), '" + b + "']"

def negation(a):
    return ("('not', '" + a + "')")

def conjunction(a, b):
    data = []
    data.append(a)
    data.append(b)
    return data

def disjunction(a, b):
    return("['" + a + "', '" + b + "']")
