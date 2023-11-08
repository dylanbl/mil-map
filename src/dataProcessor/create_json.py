import json 
from dataProcessor.gloablCountryList import globalCountryList

def writeOfficalNameJson(): 
    data = open("data/officialNames/refined.csv", "r")

    jsonDict = {}

    for row in data: 
        reg, official = row.split(",")

        jsonDict[reg] = {}
        jsonDict[reg]["official_name"] = official.replace("\n", "")

    k = list(jsonDict.keys())
    k.sort()
    jsonDict = {i: jsonDict[i] for i in k}
 
    f_out = open("data/officialNames/officialNames.json", "w")
    json.dump(jsonDict, f_out)

    data.close()
    f_out.close()

def writeCodesJson(): 
    data = open("data/codes/codes.csv", "r")

    jsonDict = {}

    for row in data: 
        name, twoLetter, threeLetter, numeric = row.split(",")

        jsonDict[name] = {}
        jsonDict[name]["twoLetter"]   = twoLetter
        jsonDict[name]["threeLetter"] = threeLetter
        jsonDict[name]["numeric"]     = numeric.replace("\n", "")

        
    k = list(jsonDict.keys())
    k.sort()
    jsonDict = {i: jsonDict[i] for i in k}
 
    f_out = open("data/codes/codes.json", "w")
    json.dump(jsonDict, f_out)

    data.close()
    f_out.close()

def writeMasterJson(): 
    f_in = open("data/codes/codes.json")
    codesData = json.load(f_in)
    f_in.close()

    f_in = open("data/officialNames/officialNames.json")
    officialNamesData = json.load(f_in)
    f_in.close()

    masterJson = {"metadata": {}, "countries": {}}

    for country in globalCountryList: 
        codes = codesData[country]
        officalName = officialNamesData[country]

        masterName = codes["twoLetter"]

        masterJson["countries"][masterName] = {"names": {}}
        masterJson["countries"][masterName]["names"]["name"]            = country
        masterJson["countries"][masterName]["names"]["numericCode"]     = codes["numeric"]
        masterJson["countries"][masterName]["names"]["officialName"]    = officalName["official_name"]
        masterJson["countries"][masterName]["names"]["threeLetterCode"] = codes["threeLetter"]

    masterJson["metadata"]["num_countries"] = len(globalCountryList)

    f_out = open("data/masterCountryData.json", "w")
    json.dump(masterJson, f_out)
    f_out.close()