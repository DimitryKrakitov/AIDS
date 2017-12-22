'''Functions for reading the input files with the logic statements'''


def filereader(file):
    try:
        with open(file, 'r') as f:  # Open the file to retrieve the text lines
            data = f.readlines()
    except EnvironmentError:  # Is the name of the file correct?
        print("Invalid File")
        exit(-2)
    return data


def cnfreader(file):
    try:
        with open(file, 'r') as f:  # Open the file to retrieve the text lines
            data = f.readlines()
    except EnvironmentError:  # Is the name of the file correct?
        print("Invalid CNF File")
        exit(-2)
    return data
