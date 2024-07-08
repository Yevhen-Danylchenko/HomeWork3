userInput = input('Введіть рядок: \t')

ind = 0

def My_Func_String (userInput, ind) :

    for index in range(len(userInput)) :
        ind += 1

    print(f'Рядок має {ind} символів')

My_Func_String(userInput, ind)