class Name(): 
    def __init__(self, names: dict): 
        self.commonName      = names["name"]
        self.officialName    = names["officialName"]
        self.numericCode     = names["numericCode"]
        self.threeLetterCode = names["threeLetterCode"]
