def printer(x):
    p = "["
    for y in x:
        p += " " + str(y) + ";"
    return p + "]"


def sendhelp(b):
    if "[" in b:
        return b
    return "'" + b + "'"
