immutable_var = 1 , 2 , 3 , 4 , 5
print(immutable_var)
#Попытка изменить элемент кортежа приведёт к ошибке Кортежи неизменяемы, после их создания изменить содержимое невозможно
# насколько правильно я ответил жду в комментарии
mutable_list = [6, 7, 8, 9]
print(mutable_list)
mutable_list[0] = 0
print(mutable_list)
