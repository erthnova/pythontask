def main():
    usage = '''Аргументы переданы некорректно!
В функцию нужно передать число, систему исчисления, которую хотите получить, систему исчисления передаваемого числа(по умолчанию десятичная).
Все аргументы должны быть в формате string.'''
    try:
        numer, baseto, *base = input().split()
        base = base[0] if base else '0123456789'
        for i in numer:
            if i not in base:
                print(usage)
            break
        print(itoBase(numer, baseto, base))
    except Exception:
        print(usage)

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


main()
