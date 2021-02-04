#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# В списке, состоящем из вещественных элементов, вычислить:
# 1) количество элементов списка, равных 0;
# 2) сумму элементов списка, расположенных после минимального элемента.
# Упорядочить элементы списка по возрастанию модулей элементов.

if __name__ == '__main__':
    lst = list(map(int, input('Введите список ').split()))
    print(sum(not bool(i) for i in lst))
    print(sum(lst[lst.index(min(lst)) + 1:]))
    lst.sort(key=lambda x: abs(x))
    print(lst)
