import copy


def negation(p, c):
    str_p = str(p)
    str_c = str(c)
    if (str_p == '(\'not\', \'' + str_c + '\')'):
        # print("TRUE FIRST")
        return True
    if (str_c == '(\'not\', \'' + str_p + '\')'):
        # print("TRUE SECOND")
        return True
    # print("FALSE")
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
    # print("FUSED")
    # print(fusion)
    return fusion


def negation_in(prove, clause):
    # print(prove + " FUSION WITH " + clause)
    # prove_ = eval(prove)
    # clause_ = eval(clause)

    # print(str(prove_) + str(len(prove_)))
    # print(str(clause_) + str(len(clause_)))

    add_kb = []

    if (len(prove) == 1 & len(clause) == 1 & negation(prove, clause)):
        return 1  # ITS OVER; WE PROVED THE THEOREM!!!

    for elem_c in clause:
        # print("ELEMC " + str(elem_c))
        for elem_p in prove:
            # print("ELEMP " + str(elem_p))
            if (negation(elem_p, elem_c)):
                add_kb.append(fusion(prove, clause, elem_c, elem_p))
                # print(add_kb)

    return add_kb


def simplify_4(cnf):
    cnf_4 = []
    for i in range(len(cnf)):
        cnf_4.append(list(set(cnf[i])))
    print("4")
    print(cnf_4)
    return cnf_4


def simplify_2(cnf, literals):
    cnf_2 = copy.copy(cnf)

    for i in cnf:
        for l in literals:
            if ((l in i) & (("-" + l) in i)):
                cnf_2.remove(i)
    print("2")
    print(cnf_2)
    return cnf_2


def simplify_3(cnf):
    cnf_3 = copy.copy(cnf)
    remove = []
    for i in range(len(cnf_3)):
        for j in range(len(cnf_3)):
            # print(str(i) + " - " + str(j) )
            if (i != j) and (set(cnf_3[i]) < set(cnf_3[j])) and (cnf_3[j] not in remove):
                remove.append(cnf_3[j])
    for j in remove:
        cnf_3.remove(j)
    print("3")
    print(cnf_3)
    return cnf_3


def simplify_1(cnf, all_literals, literals, not_literals):
    remove = []
    print("LITERALS")
    print(literals)
    print("NOT LITERALS")
    print(not_literals)
    for l in literals[:]:
        nl = ("-" + l)
        if (nl not in not_literals):
            remove.append(l)
            # print(l)
    for n in not_literals[:]:
        ns = str(n)
        if (ns[1:] not in literals):
            # print(n)
            remove.append(n)

    # print(remove)
    # remove = set(literals) ^ set(not_literals)

    for c in cnf[:]:
        for r in remove:
            if (r in c):
                cnf.remove(c)
    print("1")
    print(cnf)

    return cnf


def get_literals(cnf):
    all_literals = []
    not_literals = []
    literals = []
    for i in cnf:
        for j in i:
            if (j in all_literals):
                continue
            else:
                if (j.find("-") == -1):
                    literals.append(j)
                else:
                    not_literals.append(j)
                all_literals.append(j)

    return all_literals, literals, not_literals


def simplify(cnf):
    all_literals, literals, not_literals = get_literals(cnf)

    print("LITERALS")
    print(literals)
    print("ALL")
    print(all_literals)
    cnf_4 = simplify_4(cnf)
    cnf_2 = simplify_2(cnf_4, literals)
    cnf_3 = simplify_3(cnf_2)

    all_literals, literals, not_literals = get_literals(cnf_3)

    cnf_1 = simplify_1(cnf_3, all_literals, literals, not_literals)

    return cnf_1


def contained(list1, list2):
    for i in range(len(list1)):
        for j in range(len(list2)):
            if not set(list1[i]) >= set(
                    list2[j]):  # If a value of list1 is not on list2 then list1 is not contained in list2
                return False

    return True


def resolve(clause_i, clause_j):
    resolvent = []
    ci = copy.copy(clause_i)
    cj = copy.copy(clause_j)
    resolved = False
    for i in clause_i:
        for j in clause_j:
            neg = str(i)
            if ((neg[0] == "-") and (neg[1:] in j)):
                resolved = True
            elif ((neg[0] != "-") and (("-" + neg) in j)):
                resolved = True
            if (resolved):
                ci.remove(i)
                cj.remove(j)
                resolvent = ci.extend(cj)
                return resolvent, True

    return resolvent, False  # It will return [ ] without resolving
