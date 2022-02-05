"""
Problem B: 196111. Boris the Chef.
Chef Boris is testing new dishes. He wants to find the most delicious dishes. But Boris is not only a chef, but also a programmer. Therefore, a dish is considered tasty if the sum of the ASCII codes of all letters in its name is more than 300. Write a program that will find tasty dishes.

Input format
You are given string  - name of the dish.

Output format
Print It is tasty! if the dish is tasty. Otherwise, print Oh, no!.
"""
summ = 0
a = str(input())
for b in a:
    summ += ord(b)

if summ > 300:
    print('It is tasty!', end = '')
else:
    print('Oh, no!')