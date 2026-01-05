a = int(input())
b = a % 10
c = (a // 10) % 10
d = (a // 100) % 10
gaz = (max(b, c, d) + min(b, c, d))
if gaz == b * 2:
    print("YES")
elif gaz == c * 2:
    print("YES")
elif gaz == d * 2:
    print("YES")
else:
    print("NO")