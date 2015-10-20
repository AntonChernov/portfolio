""" Проверка пароля. Должна быть 1 буква в нижнем регистре 1 в верхнем и 1 цифра длинна пароля не менее 10 символов"""
def das(data):
    __d=len(data)>=10 # проверка длинны
    __a=False
    __b=False
    __c=False
    #проверка условий
    for i in data:
        if i.isupper()==True:
            __c=True
        elif i.isdigit()==True:
            __a=True
    for i in data:
        if i.islower()==True:
            __b=True
        else:
            __b=False
    """print (__d)
    print(__a)
    print(__c)
    print('Result is : ')"""
    #проверка выполнения условий
    if (__a and __d and __c)==True:
        return True
    else:
        return False
