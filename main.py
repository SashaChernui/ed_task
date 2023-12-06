numbers = []

number = int(input('Введите число:'))
num = 1

if number == 1:
   num += 1
else:
   num = number

for i in range (1,num,2):
    numbers.append(i)

print('Список из нечётных чисел от 1 до',number,':',numbers)


