def output_file(sol):
    F = open("cnf.txt",'w')
    #print("OUTPUT FILE:")

    print("CNF form: ")
    for elem in sol:

        print(elem)
        F.write(elem + "\n")

    #print(F) # printing the file in the console too
    return
