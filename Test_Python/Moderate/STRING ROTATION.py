__author__ = 'tito'
collection = open('STRING ROTATION', 'r')
for i in collection.readlines():
    # print(i)
    dev = i.rstrip().split(',')
    # print(type(dev))
    # a = ['True','False']
    if len(dev[0])==len(dev[1]):
        a = []
        for i in dev[0]:
            if i in dev[1]:
                a.append(i)
        if len(a) == len(dev[0]):
            print(True)
        else:
            print(False)
    else:
        print(False)