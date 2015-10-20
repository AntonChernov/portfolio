__author__ = 'tito'
collections=open('REMOVE CHARACTERS', 'r')
for i in collections.readlines():
    dev=i.rstrip().split(',')
    a=[]
    a.append(list(dev[0]))
    a.append(list(dev[1].lstrip()))
    for i in a[0]:
        if i in a[1]:
            b=[]
            a[0].remove(i)
    StrDev=''.join(a[0])
    print(StrDev)