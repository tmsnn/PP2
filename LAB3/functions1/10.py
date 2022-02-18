def uni(numbers):
    a = []
    for num in numbers:
        if num not in a:
            a.append(num)
    print(*a)
numbers = list(map(int, input().split()))
uni(numbers)
        
