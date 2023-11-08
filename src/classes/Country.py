import json
from classes.Name import Name 

class Country():   
    def __getAllCountryData(self, country: str) -> {}: 
        data = {}
        with open("data/masterCountryData.json") as f: 
            data = json.load(f)
        
        return data["countries"][country]

    def __init__(self, country: str) -> None:
        countryData = self.__getAllCountryData(country)

        self.id = country
        self.names = Name(countryData["names"])

        