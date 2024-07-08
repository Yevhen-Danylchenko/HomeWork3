elem = int(input('Задайте довільний аргумент: \t'))

def My_Func_Arg (list, elem) :
    list1 = list.append(elem), list.copy()

    print(list1)

list = [1,5,4,7,9,3,4,-3,3.9]

My_Func_Arg(list, elem)