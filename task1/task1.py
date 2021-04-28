import sys

def itoBase(nb, baseSrc, baseDst):
    if baseDst == '0123456789': #если число подано в десятичной системе
        numb = int(nb)
    else: #если число в не десятичной системе, то переводим в десятичную, работает даже с котиками
        baselen = len(baseDst)
        basedict = {baseDst[a]: a for a in range(len(baseDst))} #словарь из baseDst
        numb = 0
        count = len(nb) - 1
        for i in nb:
            numb += basedict[i] * baselen ** (count)
            count -= 1

    basenumb = len(str(baseSrc))
    res = ''
    while numb != 0: #переводим число в искомую систему
        res += (baseSrc[numb % basenumb])
        numb = numb // basenumb
    return res[::-1]

if __name__ == "__main__":
    usage = '''Аргументы переданы некорректно!
    В функцию нужно передать число, систему исчисления, которую хотите получить, систему исчисления передаваемого числа(по умолчанию десятичная).
    Все аргументы должны быть в формате string.'''
    if len (sys.argv) == 3:
        numer = sys.argv[1]
        baseto = sys.argv[2]
        base = '0123456789'
        for i in numer:
            if i not in base:
                print(usage)
                sys.exit(1)
        print(itoBase(numer, baseto, base))
    elif len (sys.argv) == 4:
        numer = sys.argv[1]
        baseto = sys.argv[2]
        base = sys.argv[3]
        for i in numer:
            if i not in base:
                print(usage)
                sys.exit(1)
        print(itoBase(numer, baseto, base))
    else:
        print(usage)
        sys.exit (1)
