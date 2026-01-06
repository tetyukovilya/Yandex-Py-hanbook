a = int(input())
b = int(input())
n1 = (a // 10) % 10
n2 = a % 10
m1 = (b // 10) % 10
m2 = b % 10
result = [n1, n2, m1, m2]
r1 = max(result)
result.remove(max(result))
r3 = min(n1, n2, m1, m2)
result.remove(min(result))
r2 = (min(result) + max(result)) % 10
print(r1, r2, r3, sep='')