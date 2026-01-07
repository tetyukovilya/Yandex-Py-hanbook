a = int(input())
b = int(input())
c = int(input())
void = ""
if a > b > c and a > c:
    print(void, "Петя", void, "\n", "Вася", void, void, "\n", void, void, "Толя\n", "II", "I", "III", sep="  ")
elif b > a > c and b > c:
    print(void, "Вася", void, "\n", "Петя", void, void, "\n", void, void, "Толя\n", "II", "I", "III", sep="  ")
elif c > a > b and c > b:
    print(void, "Толя", void, "\n", "Петя", void, void, "\n", void, void, "Вася\n", "II", "I", "III", sep="  ")
elif b > c > a and b > a:
    print(void, "Вася", void, "\n", "Толя", void, void, "\n", void, void, "Петя\n", "II", "I", "III", sep="  ")
elif a > c > b and a > b:
    print(void, "Петя", void, "\n", "Толя", void, void, "\n", void, void, "Вася\n", "II", "I", "III", sep="  ")
else:
    print(void, "Толя", void, "\n", "Вася", void, void, "\n", void, void, "Петя\n", "II", "I", "III", sep="  ")