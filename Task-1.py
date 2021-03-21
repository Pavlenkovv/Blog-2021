'''
напишите функцию slice_less,
на вход принимает:
	1. первый аргумент “my_list” - список из целых чисел
	2. второй аргумент “lesser” - целое число
выводит:
отсортированный от большего к меньшему список my_list, где все значения больше чем lesser
'''


def slice_less(my_list, lesser):
    return sorted((x for x in my_list if x > lesser), reverse=True)


arr = [1, 3, 4, 56, 7, 43, 302, 443, 405, 473, 1, 36, 12, 6, 76, 456]
m_int = 20
print(slice_less(arr, m_int))
