#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Ввести список А из 10 элементов, найти сумму элементов,
# меньших по модулю 3 и кратных 9,
# их количество и вывести результаты на экран.

if __name__ == '__main__':
    from random import randint
    A = [randint(-100, 10) for i in range(10)]
    print(*A)
    print(*[i for i in A if not i % 9 and i < 3])
    print(sum((1 for i in A if not i % 9 and i < 3)))
    print(sum((i for i in A if not i % 9 and i < 3)))
