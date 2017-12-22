import copy

'''
Simplification 4: Resolves clauses with repeated literals,  removing  the  duplicates.  
This  is  implemented, by making a "set" out of the clauses which eliminate duplicates
and then returning back to a list type.
'''


def simplify_4(cnf):
    cnf_4 = []
    for i in range(len(cnf)):
        cnf_4.append(list(set(cnf[i])))
    return cnf_4


'''
Simplification 2: Discards tautologies which are clauses with both a literal and it's negation. These do not add any
information to the solver since they are always true.
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
Simplification 3: Clauses implied by other clauses are removed. In other words, if a clause is contained in another, the
larger one is removed. Each  clause  is converted to a ”set” in python and compared with the all others in search of a 
another clause containing every element of the first one,if this happens the latter one is removed.
'''


def simplify_3(cnf):
    cnf_3 = copy.copy(cnf)
    remove = []
    for i in range(len(cnf_3)):
        for j in range(len(cnf_3)):
            if (i != j) and (set(cnf_3[i]) <= set(cnf_3[j])) and (cnf_3[j] not in remove):
                remove.append(cnf_3[j])  # Remove the largest clause
    for j in remove:
        cnf_3.remove(j)
    return cnf_3


'''
Simplification 1: Clauses that contain literals which cannot be resolved are removed. This is done by previoulsy storing
all the "positive" literal instances in a list and the "negative" literal instances in another. If a literal is in a 
list but not the other, than that literal cannot be resolved. Every clause containing that literal is thus removed.
Arguments:
cnf - list of clauses
literals - list of non-negated literal instances of the list of clauses
not_literals - list of negated literal instances of the list of clauses
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
get_literals(): A function which receives a list of clauses and returns two lists. One with all instances of non-negated
literals (list "literals") and another with all instances of negated literals (list "not_literals").
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

    return literals, not_literals


'''
simplify(): Receives a list of clauses and preforms all the 4 simplifications explained in the report.
'''


def simplify(cnf):
    literals, not_literals = get_literals(cnf)

    cnf_4 = simplify_4(cnf)
    cnf_2 = simplify_2(cnf_4, literals)
    cnf_3 = simplify_3(cnf_2)

    literals, not_literals = get_literals(cnf_3)

    cnf_1 = simplify_1(cnf_3, literals, not_literals)

    return cnf_1


'''
contained(): Returns True if "list1" is contained in "list2". This is done by turning each clause of both lists in sets
and checking if all elements of a set are contained in the other set. Every pair is checked. If a clause from list1 is
not in list2, the function returns False, otherwise it returns True.
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
remove_duplicates(): Removes duplicate clauses from a list of clauses.
This is implemented, by first sorting the clauses and then removing consecutive elements that are equal.
'''


def remove_duplicates(l):
    l.sort()
    l = [l[i] for i in range(len(l)) if i == 0 or l[i] != l[i - 1]]
    return l


'''
resolve(): Preforms a resolution between clauses i and j, returning the resolvent if the resolution is preformed.
A boolean is also returned to determine if a resolution is preformed, since a resolution can be preformed and be equal
to an empty clause (theorem is proven) but when two clauses cannot be resolved an empty clause is also returned (nothing 
is appended to the resolvent list). When a resolvent is generated, the function returns it immediately since if several
resolutions can be preformed between the same two clauses these are certainly tautologies.
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
