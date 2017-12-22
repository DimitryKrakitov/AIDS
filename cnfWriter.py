from functions import negation

'''Function that receives a list of sentences in their final form to be printed
and lays them out onto the console, to be picked up by the prover'''


def output_file(sol):
    # F = open("cnf.txt",'w')
    # print("OUTPUT FILE:")

    # print("CNF form: ")
    for elem in sol:

        if not isinstance(elem, tuple) and not isinstance(elem, list):
            elem = "'" + elem + "'"
        print(elem)
        # F.write(str(elem) + "\n")

    # print(F) # printing the file in the console too
    '''print("Points we're trying to prove:")
    for elem in ans:

        if not isinstance(elem, tuple) and not isinstance(elem, list):
            elem = "'" + elem + "'"
        print(elem)
        F.write(str(elem) + "\n")'''

    # F.write(str(negation(sol[-1])))#isto vai causar negações de negações,resolver isso mesmo na função negation
    #  (apagar as negações em duplas negações)
    return
