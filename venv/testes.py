class funcs():
    @staticmethod
    def equi():
        print("equi")

    @staticmethod
    def impli():
        print("impli")


    @staticmethod
    def noti():
        print("noti")


cases = {
    "<=>": funcs.equi(),
    "=>": funcs.impli(),
    "not": funcs.noti()

}


#cases["not"]