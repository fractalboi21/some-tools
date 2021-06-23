#file -> list


def file_to_list(path):
    lst = []
    with open(path,"r") as f:
        f = f.read().split("\n")
        
        
        for i in f:
            if i != '':
                lst.append(i)
        return lst

