import math
a = float(input())
b = float(input())
c = float(input())

disc = b**2 - 4*a*c
if a == 0:
    if b == 0:
        if c == 0:
            print("Infinite solutions")
        else:
            print("No solution")
    else:
        x = -c / b
        print(f"{x:.2f}")
elif disc > 0:
    sqrt_disc = math.sqrt(disc)
    x1 = (-b - sqrt_disc) / (2 * a)
    x2 = (-b + sqrt_disc) / (2 * a)
    print(f"{min(x1, x2):.2f} {max(x1, x2):.2f}")
elif disc == 0:
    x = -b / (2 * a)
    print(f"{x:.2f}")
else:
    print("No solution")
