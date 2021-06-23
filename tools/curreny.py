def removeCommaAndstr2num(strnum):
    return int(str(strnum).replace(",","").replace("$",""))
    
def usd2ind(dollar):
    val = dollar * 72
    return print(f"{val:,}")

def indian_place_value(num):
    length = len(str(num)) - 1
    if length == 5:
        return str(num)[0] + "L"
    elif length == 6:
        return str(num)[0:2] + "L"
    elif length == 7:
        return str(num)[0] + "Cr"
    elif length == 8:
        return str(num)[0:2] + "Cr"
    elif length == 9:
        return str(num)[0:3] + "Cr"
    else:
        return "idk"

def ind2usd(rupees):
    return "$" + str((removeCommaAndstr2num(rupees)/72))
