first_name = 'Петя'
first_speed = float(input())
second_name = 'Вася'
second_speed = float(input())
third_name = 'Толя'
third_speed = float(input())
if first_speed < second_speed:
    first_speed, second_speed = second_speed, first_speed  # Обмен значениями скоростей
    first_name, second_name = second_name, first_name  # Обмен именами велогонщиков
elif first_speed:
    print(first_name, second_name, third_name, sep='\n')