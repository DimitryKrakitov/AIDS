from convFunctions import negration
def output_file(sol):
    F = open("cnf.txt",'w')
    #print("OUTPUT FILE:")

    print("CNF form: ")
    for elem in sol[0:-1]:

        print(elem)
        F.write(elem + "\n")

    #print(F) # printing the file in the console too
    print("Point we're trying to prove:")
    print(sol[-1])
    F.write(negration(sol[-1]))#isto vai causar negações de negações,resolver isso mesmo na função negation
    #  (apagar as negações em duplas negações)
    return
