a = float(input())
b = float(input())
c = float(input())

maximum = max(a, b, c)
minimum = min(a, b, c)
middle = a + b + c - maximum - minimum

if abs(maximum**2 - (middle**2 + minimum**2)) < 1e-9:
    print("100%")
elif maximum**2 < middle**2 + minimum**2:
    print("крайне мала")
else:
    print("велика")