my_dict = {'Yurie' : 1979} #ключ.значение
print(my_dict)
print(my_dict['Yurie'])# вывод значения ключа
print(my_dict.get('Jonn'))# проверка несуществующего ключа
print(my_dict.get('Jonn', 'Такого ключа нет'))# проверка несуществующего ключа, с фразой
my_dict.update({'Max': 1980,# добавление нескольких пар (ключ.значение)
                'Alex': 1990})
print(my_dict)
a = my_dict.pop('Max')# удаление пары с записью значения
print(a)
print(my_dict)
#Множества
my_set = {1, 2, 3, 4, 5, 1, 2, 3, 'aplle', (1, 2, 3)}
print(my_set) #команда выводит только уникальные значения
print(type(my_set))
print(my_set.add(6))# добавление
print(my_set.add(7))
print(my_set)
print(my_set.discard(1))# удаление
print(my_set)


