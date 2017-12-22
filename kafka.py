from functions import negation

'''metamorfose: function that takes the sentences already in CNF 
form and turns them into the format asked, to be printed'''


def metamorfose(lines):
    cnf = []

    for elem in lines:
        l = []
        if isinstance(elem, tuple) and len(elem) == 3:
            # line = list(elem)
            a = cnf_maker(elem, l)
            b = trimming(a[1])
            if b:
                cnf.append(b)
        else:
            cnf.append(elem)

    return cnf


'''trimming: function that checks each line for possible optimizations.
Trims off repeated literals, and completely eliminates a sentence if it
contains both a literal and it's negation (sentence would always be True,
 wouldn't add any actual knowledge)'''


def trimming(l):
    l = list(set(l))
    for elem in l:
        if negation(elem) in set(l):
            return []

    return l


'''cnf_maker: function that recursively searches for tuples with disjunctions
 to turn the final sentence into a big list of all sentences in the disjunction
  (format asked for the information to be passed)'''


def cnf_maker(line, l):
    if isinstance(line, tuple) and len(line) == 3:
        line = ('or', cnf_maker(line[1], l), cnf_maker(line[2], l))

    if not isinstance(line, tuple):
        # return "'" + line + "'"
        l.append(line)
        return (line, l)

    if len(line) == 3:
        lista = list(line)
        lista.remove('or')
        '''l.append(line[1])
        l.append(line[2])'''
        return (lista, l)

    # print("Elem in Kafka", line)
    l.append(line)
    return (line, l)
