# Pflfxf 1.
# Задана натуральная степень k. Сформировать случайным образом 
# список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0


from random import randint

# функция создает список, состоящий из коэффициетов
def creat_list1(k):
    list = []
    for i in range(k + 1):
        list.append(randint(0, 100))    
    return list

def creat_list2(k):
    list = []
    for i in range(k + 1):
        list.append(randint(0, 100))    
    return list

# функция собирает строку в виде многочлена  
def comp_str(lst, int_k):
    if lst[int_k] != 0:
        lst[int_k] = f'{lst[int_k]}=0'
    else:
        lst[int_k] = f'=0'

    for i in range(int_k):
        if lst[i] != 0 and lst[i] != 1 and lst[i+1] != '=0': #
            lst[i] = f'{lst[i]}*x^{int_k}+'
            if lst[i+1] == '=0':
                lst[i] = f'{lst[i]}*x^{int_k}'
            int_k -= 1
        elif lst[i] == 1 and lst[i+1] != '=0': #
            lst[i] = f'x^{int_k}+'
            if lst[i+1] == '=0':
                lst[i] = f'x^{int_k}'
            int_k -= 1
        else:
            lst[i] = f''
            int_k -= 1
    
    return "".join(lst) 

# функция убирает лишнее
def correct_str(str):
    new_str = str.replace('x^1', 'x')
    new_str = new_str.replace('+=', '=')
    return new_str

# запись в файлы
def write_file1(str):
    with open('DZ_Task01-1.txt', 'w') as file:
        file.write(str)

def write_file2(str):
    with open('DZ_Task01-2.txt', 'w') as file:
        file.write(str)



print('Введите натуральную степень k:')
k = int(input())

list1 = creat_list1(k)
list2 = creat_list2(k)
print(list1)
print(list2)
new_str1 = comp_str(list1, k)
new_str2 = comp_str(list2, k)
print(new_str1)
print(new_str2)
print(correct_str(new_str1))
print(correct_str(new_str2))

write_file1(correct_str(new_str1))
write_file2(correct_str(new_str2))

