# Лабоораторная работа №3 Написать функцию,
# которая принимает словарь и с помощью генераторного выражения создает и возвращает новый
# список, содержащий значения ключей входящего словаря.
import random # Импорт модуля random
def get_random_values (d):
    return[d[key] for key in random.sample(d.keys(), len(d))]
# Возвращение списка значений из словаря d, выбранных случайным образом
my_dict = {'a':1,'b':2,'c':3}
random_values_list = get_random_values(my_dict)
print(random_values_list) #Вывод списка random_values_list на экран