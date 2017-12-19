import copy

def negation(p,c):
    str_p = str(p)
    str_c = str(c)
    if(str_p == '(\'not\', \''+ str_c + '\')'):
        #print("TRUE FIRST")
        return True
    if(str_c == '(\'not\', \''+ str_p + '\')'):
        #print("TRUE SECOND")
        return True
    #print("FALSE")
    return False

def fusion(prove_, clause_, elem_c, elem_p):
    prov = list(prove_)
    claus = list(clause_)

    print("JOIN")
    print(prov)
    print("AND")

    print("ANTES")
    print(claus)

    prov.remove(elem_p)
    claus.remove(elem_c)

    print("DEPOIS")
    print(claus)

    prov.extend(claus)
    fused = copy.deepcopy(prov)

    fusion = str(fused)
    #print("FUSED")
    #print(fusion)
    return fusion


def negation_in(prove, clause):
    #print(prove + " FUSION WITH " + clause)
    #prove_ = eval(prove)
    #clause_ = eval(clause)

    #print(str(prove_) + str(len(prove_)))
    #print(str(clause_) + str(len(clause_)))

    add_kb = []

    if(len(prove) == 1 & len(clause) == 1 & negation(prove, clause)):
        return 1 # ITS OVER; WE PROVED THE THEOREM!!!

    for elem_c in clause:
        #print("ELEMC " + str(elem_c))
        for elem_p in prove:
            #print("ELEMP " + str(elem_p))
            if(negation(elem_p,elem_c)):
                add_kb.append(fusion(prove, clause, elem_c, elem_p))
                #print(add_kb)

    return add_kb