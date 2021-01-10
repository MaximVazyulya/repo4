# 1. Реализовать скрипт, в котором должна быть предусмотрена функция
# расчета заработной платы сотрудника. В расчете необходимо
# использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать
# скрипт с параметрами.


from sys import argv
name_file, workout_param, rate_param, prize_param = argv

def calc (name_file, workout_param, rate_param, prize_param):
    salary = (float(workout_param) * float(rate_param)) + float(prize_param)
    print("название файла : ", name_file)
    print("зарплата сотрудника = ", salary)
    return
calc(name_file, workout_param, rate_param, prize_param)
