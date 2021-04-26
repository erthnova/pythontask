def del_th(strsp): #выделяем в список все значения из второй строки, которые не *
    lists = list(strsp)
    listsp = []
    for i in lists:
        if i != '' and i != '*':
            listsp.append(i)
    return listsp

def compare_str(str1, str2):
    listexp = del_th(str2)
    # если вторая строка состоит только из *, она всегда будет равен любой строке(если при этом она не пустая)
    #или строки просто состоят из одинаковых символов
    if str2.replace('*','') == '' and str2 != '' and str1 !='' or str1 == str2:
        print('OK')
        return
    elif str2 == '' or str1.find(listexp[0]) == -1: #если элемент из второй строки не находится в первой, или втроая сторка пуста то они точно не равны
        print('KO')
        return
    elif listexp==[]: #если элементы в списке кончились, то строки равны
        print('OK')
    elif str1[0] == str2[0]: #удаляем оба символа, если они совпадают
        str1 = str1[1::]
        str2= str2[1::]
        compare_str(str1,str2) #рекурсим пока ничего не останется\не совпадет порядок
    elif str2[0] == '*':
        str1 = str1[1::] #обрезаем строки
        str2 = str2[1::]
        rema = str1.find(listexp[0])
        remb = str2.find(listexp[0])
        str1= str1[rema+1::] #обрезаем строки по элемент из списка
        str2= str2[remb+1::]
        while str1.find(listexp[0]) != 1 and str2.find('*') == -1:
            rema = str1.find(listexp[0])
            str1 = str1[rema + 1::]
        compare_str(str1, str2) #рекурсим пока ничего не останется\не совпадет порядок
    else:
        print('KO')
        return

string1, string2 = input().split(' ') #считываем переменные
compare_str(string1, string2)
