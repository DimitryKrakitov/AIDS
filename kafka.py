

def metamorfose(lines):
    cnf = []

    for elem in lines:
        cnf.append(aztec_magic(elem))

    return cnf

def aztec_magic(line):

    if isinstance(line, tuple) and len(line) == 3:
        line = ('or', aztec_magic(line[1]), aztec_magic(line[2]))

    if not isinstance(line, tuple):
        #return "'" + line + "'"
        return line

    if len(line) == 3:
        lista = list(line)
        lista.remove('or')
        return lista

    #print("Elem in Kafka", line)
    return line
