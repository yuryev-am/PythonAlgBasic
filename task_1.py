"""
Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа)
для каждого предприятия.. Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести
наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже
среднего.
"""

from collections import namedtuple

prod_cnt = int(input('Введите количество предприятий: '))

company_list = []
CompanyInfo = namedtuple('CompanyInfo', 'name, Q1, Q2, Q3, Q4, YearProfit')
profit_year_all = 0

for i in range(1, prod_cnt + 1):
    name = input(f'Введите наименование предприятия {i}: ')
    profit = input(f'Введите прибыль компании по кварталам через пробел (Q1 Q2 Q3 Q4): ').split()
    profit_Q = [float(el) for el in profit]  # Преобразуем полученные значения к типу float
    profit_year = sum(profit_Q)  # Считаем прибыль за год
    company_list.append(CompanyInfo(name, profit_Q[0], profit_Q[1], profit_Q[2], profit_Q[3], profit_year))
    profit_year_all += profit_year

print(company_list)

avg_profit_year = profit_year_all / prod_cnt  # Считаем среднюю прибыль по компаниям

print('Средняя прибыль по всем компаниям: ', avg_profit_year)

less_avg = []  # Список компаний к которых прибыль меньше средней
more_avg = []  # Список компаний к которых прибыль выше средней или равна ей

for item in company_list:
    if item.YearProfit < avg_profit_year:
        less_avg.append(item)
    else:
        more_avg.append(item)

print(f'Компании с доходом ниже среднего:')

for item in less_avg:
    print(item.name)

print(f'Компании с доходом выше или равного среднему:')

for item in more_avg:
    print(item.name)
