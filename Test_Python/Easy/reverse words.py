__author__ = 'tito'
colections=open('test_words','r')
for i in colections.readlines():
    dev=i.split()
    if dev:
        dev.reverse()
        StrOut=' '.join(dev)
        print(StrOut)