def filereader(file):
    try:
        with open(file, 'r') as f: # Open the file to retrieve the text lines
            data = f.readlines()
    except EnvironmentError:  # Is the name of the file correct?
        print("Nigga pls")
        exit(-2)
    return data






