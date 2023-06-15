# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

# Здесь пишем код

with open("test_file/task_3.txt", 'r', encoding='utf-8') as f:
    a = 0
    sum_list = []
    for line in f.readlines():
        if len(line) > 2:
            a += int(line[:-1])
        else:
            sum_list.append(a)
            a = 0
sum_list.sort()
three_most_expensive_purchases = sum(sum_list[-3:])


assert three_most_expensive_purchases == 202346
