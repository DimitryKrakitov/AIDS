def printer(alameda):
    surprise = "["
    for Quenga in alameda:
        surprise += " " + str(Quenga) + ";"
    return surprise + "]"


def sendhelp(b):
    if "[" in b:
        return b
    return "'" + b + "'"
