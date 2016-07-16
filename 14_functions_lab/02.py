def type_check(number=1, string=None):
    if type(number) != int or type(string) != str:
        raise TypeError("you insert wrong type")

type_check(2,"f")