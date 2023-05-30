from pprint import pprint

with open('File1.txt','rt',encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        dish = line.strip()
        number_of_ingridients = int(file.readline())
        ingridients = []
        for i in range(number_of_ingridients):
            ingr = file.readline()
            ingridient_name,quantity,measure = ingr.strip().split(' | ')
            ingridient = {
                'ingridient_name' : ingridient_name,
                'quantity' : quantity,
                'measure' : measure
            }
            ingridients.append(ingridient)
        file.readline()   
        cook_book[dish] = ingridients

    pprint(cook_book,sort_dicts=False)
    print(cook_book.values())

# print(cook_book)
from collections import Counter
def get_shop_list_by_dishes(dishes, person_count):
    result = {}
    res = []
    res1= []
    count = 1
    for bludos in dishes:
        bludo = bludos.strip()
        if bludo in cook_book.keys():
            res.append(cook_book[bludo])
    for list in res:
        for ingridient in list:
            if ingridient not in res1:
                res3 = {ingridient['ingridient_name'] : {'quantity' : int(ingridient['quantity'])*person_count*count,'measure' : ingridient['measure']}}
                res1.extend(res3.items())
    for a in res1:
        if res1.count(a) > 1:
            count += 1
            a = {ingridient['ingridient_name'] : {'quantity' : int(ingridient['quantity'])*person_count*count,'measure' : ingridient['measure']}}
            res1.extend(a.items())
            break
    result = dict(res1)   
    pprint(result)

# Проверка для суммирования ингридиентов
get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2)
print()
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

import os

file_path = os.getcwd()
folder = 'task3'
folder2 = 'Homework2_oop'
full_path = os.path.join(file_path,folder)
full_path1 = os.path.join(file_path,folder,'1.txt')
full_path2 = os.path.join(file_path,folder,'2.txt')
full_path3 = os.path.join(file_path,folder,'3.txt')
with open (full_path1,encoding='utf-8') as input_file1,open (full_path2,encoding='utf-8') as input_file2,open (full_path3,encoding='utf-8') as input_file3,open ('res.txt','w',encoding='utf-8') as output_file:
    res = []
    first = input_file1.readlines()
    second = input_file2.readlines()
    third = input_file3.readlines()
    first1 = ''.join(first)
    second1 = ''.join(second)
    third1 = ''.join(third) 
    if len(first) < len(second) and len(first) < len(third):
        output_file.writelines(f'1.txt\n{len(first)}\n{first1}\n')
        if len(second) < len(third):
            output_file.writelines(f'2.txt\n{len(second)}\n{second1}\n')
            output_file.writelines(f'3.txt\n{len(third)}\n{third1}\n')
        else:
            output_file.writelines(f'3.txt\n{len(third)}\n{third1}\n')
            output_file.writelines(f'2.txt\n{len(second)}\n{second1}\n')

    if len(second) < len(first) and len(second) < len(third):
        output_file.writelines(f'2.txt\n{len(second)}\n{second1}\n')
        if len(first) < len(third):
            output_file.writelines(f'1.txt\n{len(first)}\n{first1}\n')
            output_file.writelines(f'3.txt\n{len(third)}\n{third1}\n')
        else:
            output_file.writelines(f'3.txt\n{len(third)}\n{third1}\n')
            output_file.writelines(f'1.txt\n{len(first)}\n{first1}\n')

    if len(third) < len(first) and len(third) < len(second):
        output_file.writelines(f'3.txt\n{len(third)}\n{third1}\n')
        if len(first) < len(second):
            output_file.writelines(f'1.txt\n{len(first)}\n{first1}\n')
            output_file.writelines(f'2.txt\n{len(second)}\n{second1}\n')
        else:
            output_file.writelines(f'2.txt\n{len(second)}\n{second1}\n')
            output_file.writelines(f'1.txt\n{len(first)}\n{first1}\n')