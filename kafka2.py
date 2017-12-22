

def metamorfose(lines):
    cnf = []

    for elem in lines:
        line = []
        if isinstance(elem, tuple) and len(elem) == 3:
            #line = list(elem)
            cnf.append(aztec_magic(elem, line))
        else:
            cnf.append(aztec_magic(elem))

    return cnf

def aztec_magic(line):

    if isinstance(line[1], tuple) and len(line) == 3:
        line.append(aztec_magic(line[1]))
    if isinstance(line[2], tuple) and len(line) == 3:
        line.append(aztec_magic(line[2]))
    line.remove()

        #line = ('or', aztec_magic(line[1]), aztec_magic(line[2]))

    if not isinstance(line, tuple):
        #return "'" + line + "'"
        line.append(line)
        return line
    else:
        if len(line) == 2:
            line.append(line)
            return line

    if len(line) == 3:
        lista = list(line)
        lista.remove('or')
        return line

    #print("Elem in Kafka", line)
    return line
