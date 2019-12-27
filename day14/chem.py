
def parseAmount(string):
    index = 0;
    while (string[index] in ['0','1','2','3','4','5','6','7','8','9']):
        index += 1
    return (int(string[:index]), string[index+1:])


with open("test", "r") as rxnfile:

    rxndata = rxnfile.read().split("\n")
    rxndata.pop()
    rxndata = list(map(lambda rxn: rxn.split(" => "), rxndata))
    
    rxnmap = dict()
    for rxn in rxndata:
        
        productAmount, productName = parseAmount(rxn[1])
        reactantEntry = dict()
        reactants = rxn[0].split(", ")
        for reactant in reactants:
            reactantAmount, reactantName = parseAmount(reactant)
            reactantEntry[reactantName] = reactantAmount
            
        rxnmap[productName] = {productAmount: reactantEntry}



def getOreAmount(elem, need=1):
    ore = 0
    multiplier = 1
    for productAmount, reactants in rxnmap[elem].items():
        while ((productAmount*multiplier) < need):
            multiplier += 1 # if yes then increase total amount
        # next see if any ORE is used as reactant if not asking for needed reactant
        for reactantName, reactantAmount in reactants.items():
            # if reactant is ORE
            if reactantName == 'ORE':
                return reactantAmount * multiplier
            else:
                # ask for needed reactant amount 
                ore += getOreAmount(reactantName, reactantAmount*multiplier)
    return ore

print(rxnmap['FUEL'])
print(getOreAmount("FUEL"))