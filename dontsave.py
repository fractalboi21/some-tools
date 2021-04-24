path = "/home/pi/Desktop/All Crypto Coins With Abbreviations[YamkiADX].txt"

def file_to_list(path):
    lst = []
    with open(path,"r") as f:
        f = f.read().split("\n")
        
        
        for i in f:
            if i != '':
                lst.append(i)
        return lst
    
lst = file_to_list(path)

crptos_dict = []

for i in lst:
    val = i.strip().replace("\t"," ").replace(" ",":").split(":")
    dct = {}
    dct[val[0]] = val[1]
    print(dct)
    crptos_dict.append(dct)
    print("done!")
    
    