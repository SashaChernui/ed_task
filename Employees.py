employee = int(input('Кол-во сотрудников в офисе: '))
employees = []

for ID in range(employee):
 ID = int(input('ID сотрудника: '))
 employees.append(ID)


ID = int(input('Какой ID ищем?: '))
search = False
for num in employees:
 if num == ID:
  search = True


if search:
    print("Сотрудник работает!")
else:
    print("Сотрудник не работает!")
