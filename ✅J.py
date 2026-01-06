a = int(input())
b = (a // 10) % 10 + (a % 10)
c = (a // 100) % 10 + (a // 10) % 10
if b > c:
    print(b, c, sep="")
else:
    print(c, b, sep="")