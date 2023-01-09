# Задача 2.
# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов 
# (складываются числа, у которых "х" в одинаковых степенях). 

# считывание двух многочленов из предыдущей задачи:
with open('DZ_Task01-1.txt', 'r') as data:
    data1 = data.read()
with open('DZ_Task01-2.txt', 'r') as data2:
    data2 = data2.read()
print(data1)
print(data2)


# функция делает из строки список
def creat_list(data: str):
    new_data = data.replace('=0', '') 
    new_data = new_data.replace('+', ' ') 
    new_data = new_data.split() 
    return new_data


new_data1 = creat_list(data1)
new_data2 = creat_list(data2)
#print(new_data1)
#print(new_data2)

# преобразование списка в словарь
def creat_newdict(lst):
    new_dict = {}
    for i in lst:
        if '*' not in i :
            if 'x' in i:
                new_dict['x'] = 1
            else:
                new_dict[1] = int(i)
        else:
            new_dict[i.split('*')[1]] = int(i.split('*')[0])
    return new_dict

new_dict1 = creat_newdict(new_data1)
new_dict2 = creat_newdict(new_data2)
#print(new_dict1)
#print(new_dict2)

# функция суммирует значения двух словарей с одинаковыми ключами
def summa_2(dict1, dict2):
    sum_dicts = dict1.copy()
    for k, v in dict2.items():
        sum_dicts[k] = sum_dicts.get(k, 0) + v
    return sum_dicts # итоговый многочлен, пока в виде словаря
 
sum_d = summa_2(new_dict1, new_dict2)
#print(sum_d)

# функция преобразует словарь в список из строк
def sum_d_lst(dict):
    sum_d_list = []
    for key, val in dict.items():
        if key != 1:
            sum_d_list.append(''.join('{}*{}'.format(val, key)))
        else:
            sum_d_list.append(''.join('{}'.format(val,)))
    return sum_d_list


# функция преобразует список в строку
def sum_d_str2(lst):
    sum_d_str = ''
    sum_d_str += (' + '.join(lst))    
    sum_d_str += ' = 0'
    return sum_d_str


res_sum = sum_d_str2(sum_d_lst(sum_d)) 
print(res_sum)

# запись итогового многочлена в файл
with open('DZ_Task02.txt', 'w') as file:
    file.write(res_sum)