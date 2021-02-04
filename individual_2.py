#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Ввести список А из 10 элементов, найти сумму элементов,
# меньших по модулю 3 и кратных 9,
# их количество и вывести результаты на экран.

if __name__ == '__main__':
    lst = list(map(int, input('Введите список ').split()))
    print(sum(not bool(i) for i in lst))
    print(sum(lst[lst.index(min(lst)) + 1:]))
    lst.sort(key=lambda x: abs(x))
    print(lst)
