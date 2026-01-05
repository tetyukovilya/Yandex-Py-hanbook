number = int(input())
a = number // 1000           # первая цифра
b = (number // 100) % 10     # вторая цифра
c = (number // 10) % 10      # третья цифра
d = number % 10              # четвертая цифра
if a == d and b == c:
    print("YES")
else:
    print("NO")