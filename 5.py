revenue = int(input('Введите выручки фирмы: '))
cost = int(input('Введите издержки фирмы: '))
if revenue > cost:
    print('Фирма отработала с прибылью')
    profit = revenue - cost
    profitability = profit / revenue * 100
    print('Рентабельность выручки:', profitability, '%')
    staff = int(input('Введите численность сотрудников фирмы: '))
    profit_staff = profit / staff
    print('Прибыль фирмы на одного сотрудника:', profit_staff)
elif cost < revenue:
    print('Фирма отработала в убыток')
else:
    print('Фирма не отработала с прибылью, но и не понесла убытков')
