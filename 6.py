a = 2
b = 5
day = 1
while a < b:
    km = a / 100 * 10
    day = day + 1
    a = a + km
print(f'На {day}-ый день спортсмен достигнет результата - не менее 5 км.')
