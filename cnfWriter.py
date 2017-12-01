from convFunctions import negation
def output_file(sol):
    F = open("cnf.txt",'w')
    #print("OUTPUT FILE:")

    print("CNF form: ")
    for elem in sol[0:-1]:

        print(elem)
        F.write(elem + "\n")

    #print(F) # printing the file in the console too
    F.write(negation(sol[-1]))#isto vai causar negações de negações,reolver isso mesmo na função negation
    #  (apagar as negações em duplas negações)
    return
