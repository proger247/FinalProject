import json


# Функция сортировки пузырем для списков
def sort_dict(a):

    for mx in range(len(a) - 1, -1, -1):
        swapped = False
        for i in range(mx):
            if a[i][1] > a[i + 1][1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True
        if not swapped:
            break


with open('car_list.json', 'r') as car_list:
    # car_list = car_list.read()
    my_list = json.load(car_list)

my_list = list(my_list.items()) # Преобразование значений словаря в список для последующей сортировки
sort_dict(my_list) # Вызов функции сортировки
my_list = dict(my_list) # Преобразование отсортированного списка в словарь

print(my_list)

# Запись отсортированного словаря в файл
with open('dict_auto.json','w') as f:
    json.dump(my_list, f)

