"""определение мидианы т.е среднего эл-та в строке. Если строка  четная то средний эл-т это {3, 5, 7, 9} is (5 + 7) / 2 = 6""" 
def checkio(data):
    data.sort()# сортировка списка
    b=0
    #определение медианны в строке с четным кол-вом символов
    if len(data)%2==0:
        a=len(data)/2
        _n=int(a-1)
        _nn=int(a)
        b=((data[_n])+(data[_nn]))/2
        """print (a)
        print(data[_n])
        print(data[_nn])"""
        return b
    #определение медианны в строке с не четным кол-вом символов
    else:
        _z=len(data)/2
        b=int(_z)
        return data[b]
