def equivalence(tup):   #   A <=> B -> (!A V B) ^ (!B V A)

    A = tup[1]
    B = tup[2]

    return ('and', implication(('=>', A, B)), implication(('=>', B, A)))

def implication(tup):   #   A => B -> (!A V B)

    A = tup[1]
    B = tup[2]

    return ('or', ('not', A), B)

def negation(tup):
    if tup[0] == 'not':
            return tup[1]
    return ('not', tup)

def RL_dist(tup):   #   (A^B) V C  -> (C V A) ^ (C V B)

    A = tup[1][1]
    B = tup[1][2]
    C = tup[2]

    return ('and',('or', C, A), ('or', C, B))

def LR_dist(tup):   #   C V (A^B) -> (C V A) ^ (C V B)

    A = tup[1]
    B = tup[2][1]
    C = tup[2][2]

    return ('and',('or', A, B), ('or', A, C))

def deMorgan_or_and(tup):   #   !(A V B) -> (!A ^ !B)

    A = tup[1][1]
    B = tup[1][2]

    return ('and', negation(A), negation(B))


def deMorgan_and_or(tup):  # !(A ^ B) -> (!A V !B)

    A = tup[1][1]
    B = tup[1][2]

    return ('or', negation(A), negation(B))

def negation2(tup):
    if isinstance(tup[1], tuple):
        if tup[1][0] == 'not':
            return tup[1][1]
    return ('not', tup)
