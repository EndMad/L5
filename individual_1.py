#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import randint
A = [randint(-100,10) for i in range(10)]
print(*A)
print(*[i for i in A if not i % 9 and i < 3])
print(sum((1 for i in A if not i % 9 and i < 3)))
print(sum((i for i in A if not i % 9 and i < 3)))
