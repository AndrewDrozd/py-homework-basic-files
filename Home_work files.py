import os

# Задание 1 

with open('recipes.txt', 'rt') as file:
    cook_book = {}
    for line in file:
        dishes = line.strip()
        count_ingredient = int(file.readline().strip())
        recipes = []
        for _ in range(count_ingredient):
            ingredient_name, quantity, measure = file.readline().strip().split(" | ")
            recipes.append({
                'ingredient_name': ingredient_name,
                'quantity': int(quantity),
                'measure': measure
                })
        file.readline()
        cook_book[dishes] = recipes
        
    print(f'cook_book =\n{cook_book}')
    
# Задание 2

def get_shop_list_by_dishes(dishes, person_count):
    res = {}
    for book_dish in dishes:
        if book_dish in cook_book:
            for menu_dish in cook_book[book_dish]:
                if menu_dish['ingredient_name'] not in res:
                    res[menu_dish['ingredient_name']] = {menu_dish['measure'], menu_dish['quantity'] * person_count}
                else:
                    res[menu_dish['ingredient_name']]['quantity'] += menu_dish['quantity'] * person_count
        else:
            print(f'Такого блюда нет в списке!')
    return res
            
print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))

# Задание 3

import os
from pprint import pprint

folder_path = r"C:\Users\arena\Documents\андрей\Python подсказки\Python подсказки\new_proj"
file_paths = [os.path.join(folder_path, name) for name in os.listdir(folder_path)]

my_files = os.listdir(folder_path)
#создаем список для загрузки данных из файлов
common_txt_file_list = []
#делаем цикл по списку имен файлов
for file_name in my_files:
    with open(f'{folder_path}\{file_name}', 'r', encoding="utf8") as f:
        file_lines = f.readlines()
        #добавляем данные по файлу 
        common_txt_file_list.append([str(len(file_lines)), file_name, file_lines])

for rewrite in common_txt_file_list:
    
    with open('res.txt', 'w', encoding="utf8") as rewrite_file:
        rewrite_file.write(str(rewrite))
    with open('res.txt', 'r', encoding="utf8") as rewrite_file:
        print(rewrite_file.read())

pprint(sorted(common_txt_file_list))
