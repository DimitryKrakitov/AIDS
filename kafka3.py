from functions import negation

def metamorfose(lines):
    cnf = []

    for elem in lines:
        l = []
        if isinstance(elem, tuple) and len(elem) == 3:
            #line = list(elem)
            a = aztec_magic(elem, l)
            b = trimming(a[1])
            if b:
                cnf.append(b)
        else:
            cnf.append(elem)

    return cnf

def trimming(l):

    l = list(set(l))
    for elem in l:
        if negation(elem) in set(l):
            return []

    return l



def aztec_magic(line, l):

    if isinstance(line, tuple) and len(line) == 3:
        line = ('or', aztec_magic(line[1], l), aztec_magic(line[2], l))

    if not isinstance(line, tuple):
        #return "'" + line + "'"
        l.append(line)
        return (line, l)

    if len(line) == 3:
        lista = list(line)
        lista.remove('or')
        '''l.append(line[1])
        l.append(line[2])'''
        return (lista, l)

    #print("Elem in Kafka", line)
    l.append(line)
    return (line, l)
