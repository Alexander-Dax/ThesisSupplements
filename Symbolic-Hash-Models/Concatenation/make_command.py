def get_params_from_keys(input_string):
    library_params = {
    "ACT" : ["AttackerDomain"],
    "ACN" : ["AttackerDomainFresh"],
    "RO" : ["FreshDomain"],
    "PI1" : ["PreImage"],
    "PI2" : ["SndPreImage"],
    "CP" : ["CPcol"],
    "IP" : ["IPcol"],
    "Adv" : ["LengthExtension"],
    "Clo" : ["LEcol"],
    "CloAdv" : ["LengthExtension", "LEcol"],
    "AllCol" : [],
    "CR" : ["CR"],
    "i" : ["iLeak"], # TODO in Library!
    "Ex" : ["ExCol"],
    "SingleHash" : ["SingleHash"],
    "FixedLength" : ["FixedLength"]
    }
    keys = input_string.split("_")
    values = []
    
    for key in keys:
        if key in library_params:
            values.extend(library_params[key])
        else:
            return f"Key '{key}' not found in the library parameters."
    

    output = ""
    for value in values:
        output += "-D=" + value + " "
    return output

istring = input("Enter short library flags: ")
print(get_params_from_keys(istring))