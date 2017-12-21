def equivalence(tup):   #   A <=> B -> (!A V B) ^ (!B V A)

    A = tup[1]
    B = tup[2]

    return ('and', implication(('=>', A, B)), implication(('=>', B, A)))

def implication(tup):   #   A => B -> (!A V B)

    A = tup[1]
    B = tup[2]

    return ('or', ('not', A), B)

#def negation(tup):

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




