a = int(input())
b = int(input())
c = int(input())
n = a % 10 == b % 10 == c % 10
m = (a // 10) % 10 == (b // 10) % 10 == (c // 10) % 10
if n:
    print(a % 10)
elif m:
    print((a // 10) % 10)
