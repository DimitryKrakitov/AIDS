import copy

'''

'''


def simplify_4(cnf):
    cnf_4 = []
    for i in range(len(cnf)):
        cnf_4.append(list(set(cnf[i])))
    return cnf_4


'''

'''


def simplify_2(cnf, literals):
    cnf_2 = copy.copy(cnf)

    for i in cnf:
        for l in literals:
            if (l in i) and (("-" + l) in i):
                cnf_2.remove(i)
                break
    return cnf_2


'''

'''


def simplify_3(cnf):
    cnf_3 = copy.copy(cnf)
    remove = []
    for i in range(len(cnf_3)):
        for j in range(len(cnf_3)):
            # print(str(i) + " - " + str(j) )
            if (i != j) and (set(cnf_3[i]) <= set(cnf_3[j])) and (cnf_3[j] not in remove):
                remove.append(cnf_3[j])
    for j in remove:
        cnf_3.remove(j)
    return cnf_3


'''

'''


def simplify_1(cnf, literals, not_literals):
    remove = []

    for l in literals[:]:
        nl = ("-" + l)
        if nl not in not_literals:
            remove.append(l)
    for n in not_literals[:]:
        ns = str(n)
        if ns[1:] not in literals:
            remove.append(n)

    for r in remove:
        for c in cnf:
            if r in c:
                cnf.remove(c)
    return cnf


'''

'''


def get_literals(cnf):
    all_literals = []
    not_literals = []
    literals = []
    for i in cnf:
        for j in i:
            if j in all_literals:
                continue
            else:
                if j.find("-") == -1:
                    literals.append(j)
                else:
                    not_literals.append(j)
                all_literals.append(j)

    return all_literals, literals, not_literals


'''

'''


def simplify(cnf):
    all_literals, literals, not_literals = get_literals(cnf)

    cnf_4 = simplify_4(cnf)
    cnf_2 = simplify_2(cnf_4, literals)
    cnf_3 = simplify_3(cnf_2)

    all_literals, literals, not_literals = get_literals(cnf_3)

    cnf_1 = simplify_1(cnf_3, literals, not_literals)

    return cnf_1


'''

'''



def contained(list1, list2):
    # if not list1:
    #   return False
    for i in range(len(list1)):
        for j in range(len(list2)):
            if not (set(list1[i]) <= set(list2[j])):
                # If a value of list1 is not on list2 then list1 is not contained in list2
                return False

    return True


'''

'''


def remove_duplicates(l):
    l.sort()
    l = [l[i] for i in range(len(l)) if i == 0 or l[i] != l[i - 1]]
    return l


'''

'''


def resolve(clause_i, clause_j):
    ci = copy.copy(clause_i)
    cj = copy.copy(clause_j)
    resolved = False
    for i in clause_i:
        for j in clause_j:
            neg = str(i)
            if (neg[0] == "-") and (neg[1:] == j):
                resolved = True
            elif (neg[0] != "-") and (("-" + neg) == j):
                resolved = True
            if resolved:
                ci.remove(i)
                cj.remove(j)
                if not ci:
                    return cj, True
                else:
                    ci.extend(cj)
                    return ci, True

    return [], False  # It will return [ ] without resolving
