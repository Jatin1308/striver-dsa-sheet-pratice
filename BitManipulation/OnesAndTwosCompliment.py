class Compliments:
    def __init__(self):
        pass

    def find1sCompliment(self,b):
        res = ""
        for ele in b:
            if ele == "1":
                res+="0"
            else:
                res+="1"
        return res.lstrip("0")

    print(find1sCompliment("1101"))


    def find2sCompliment(self,b):
        onesCompliment = self.find1sCompliment(b)

        def add1ToGet2sComplement(onesComp):
            pass

        return add1ToGet2sComplement(onesCompliment)