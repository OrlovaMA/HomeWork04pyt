# ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ:
# Расширить значение коэффициентов до [-100..100]

# Задача 1
from random import randint

# функция создает список, состоящий из коэффициетов
def creat_list1(k):
    list = []
    for i in range(k + 1):
        list.append(randint(-100, 100))    
    return list

def creat_list2(k):
    list = []
    for i in range(k + 1):
        list.append(randint(-100, 100))    
    return list

# функция собирает строку в виде многочлена  
def comp_str(lst, int_k):
    if lst[int_k] != 0:
        lst[int_k] = f'{lst[int_k]}=0'
    else:
        lst[int_k] = f'=0'

    for i in range(int_k):
        if lst[i] != 0 and lst[i] != 1 and lst[i] != -1: #
            lst[i] = f'{lst[i]}*x^{int_k}+'
            int_k -= 1
        elif lst[i] == 1: #
            lst[i] = f'x^{int_k}+'
            int_k -= 1
        elif lst[i] == -1: #
            lst[i] = f'-x^{int_k}+'
            int_k -= 1
        else:
            lst[i] = f''
            int_k -= 1
    
    return "".join(lst) 

# функция убирает лишнее
def correct_str(str):
    new_str = str.replace('x^1', 'x')
    new_str = new_str.replace('+=', '=')
    new_str = new_str.replace('+-', '-')
    new_str = new_str.replace('++', '+')
    return new_str


print('Введите натуральную степень k:')
k = int(input())

list1 = creat_list1(k)
list2 = creat_list2(k)
print(list1)
print(list2)

new_str1 = comp_str(list1, k)
new_str2 = comp_str(list2, k)
#print(new_str1)
#print(new_str2)
print()

data1 = correct_str(new_str1)
data2 = correct_str(new_str2)
print(data1)
print(data2)


# ЗАДАЧА 2

# функция делает из строки список
def creat_list(data: str):
    new_data = data.replace('=0', '') # удаление из строки =0
    if data.startswith('x'):
        new_data = new_data.replace('x', '1*x', 1)
        new_data = new_data.replace('-x', '-1*x') 
        new_data = new_data.replace('+x', '+1*x') 
        new_data = new_data.replace('+', ' ') 
        new_data = new_data.replace('-', ' -') 
    else:
        new_data = new_data.replace('-x', '-1*x') 
        new_data = new_data.replace('+x', '+1*x') 
        new_data = new_data.replace('+', ' ') 
        new_data = new_data.replace('-', ' -') 
    
    new_data = new_data.split() # а теперь разбиваем по пробелам и получаем список
    return new_data


new_data1 = creat_list(data1)
new_data2 = creat_list(data2)
#print(new_data1)
#print(new_data2)
#print()

# преобразование списка в словарь
def creat_newdict(lst):
    new_dict = {}
    for i in lst:
        if '*' not in i :
            new_dict[1] = int(i)
        else:
            new_dict[i.split('*')[1]] = int(i.split('*')[0])
    return new_dict

new_dict1 = creat_newdict(new_data1)
new_dict2 = creat_newdict(new_data2)
#print(new_dict1)
#print(new_dict2)
print()
# функция суммирует значения двух словарей с одинаковыми ключами
def summa_2(dict1, dict2):
    sum_dicts = dict1.copy()
    for key, val in dict2.items():
        sum_dicts[key] = sum_dicts.get(key, 0) + val
    return sum_dicts # итоговый многочлен, пока в виде словаря
 
sum_d = summa_2(new_dict1, new_dict2)
#print(sum_d)

# функция преобразует словарь в список из строк
def sum_d_lst(dict):
    sum_d_list = []
    for key, val in dict.items():
        if val != 0:
                sum_d_list.append(''.join('{}*{}'.format(val, key)))
        else:
            continue 
    return sum_d_list


# функция преобразует список в строку
def sum_d_str2(lst):
    sum_d_str = ''
    sum_d_str += ('+'.join(lst))    
    sum_d_str += '=0'
    sum_d_str = sum_d_str.replace('+-', '-')
    sum_d_str = sum_d_str.replace('+1*', '')
    sum_d_str = sum_d_str.replace('-1*', '')
    sum_d_str = sum_d_str.replace('*1=', '=')
    return sum_d_str


res_sum = sum_d_str2(sum_d_lst(sum_d))
print(res_sum)

