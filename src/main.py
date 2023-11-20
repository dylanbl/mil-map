from dataProcessor.parse import *
from classes.Country import Country
from dataProcessor.create_json import *
from dataProcessor.gloablCountryList import globalCountryList

def main(): 
    parseGeoJson()

    """
    countries = []

    for country in globalCountryList: 
        countries.append(Country(country))

    for country in countries: 
        print("Country Obj. for: " + country.id)

        countryNames = country.names
        print("    Common name:                " + countryNames.commonName)
        print("    Official name:              " + countryNames.officialName)
        print("    ISO-3611 3-letter code:     " + countryNames.threeLetterCode)
        print("    ISO-3611 numeric code:      " + countryNames.numericCode)
        print("\n")
    """

if __name__ == "__main__": 
    main()