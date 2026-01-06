a = int(input())
b = (a // 100) % 10
c = (a // 10) % 10
d = a % 10
gaz1 = [b, c, d]
gaz2 = [b, c, d]
n1 = str(min(gaz2))
gaz2.remove(min(gaz2))
n2 = str(min(gaz2))
m1 = str(max(gaz1))
gaz1.remove(max(gaz1))
m2 = str(max(gaz1))
print(n2 + n1, m1 + m2, sep=' ')
