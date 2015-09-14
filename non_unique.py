def checkio(data):
    b=[]
    for i in data:
        if data.count(i)>1:
            b.append(i)
    
    return b
