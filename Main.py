#Используем квадрат Пифагора для определения характера человека
#Для начала узнаем дату человека
birth_day = input("Введите день своего рождения: ")
birth_month = input("Введите месяц своего рождения: ")
birth_year = input("Введите год своего рождения: ")

#Далее действуем согласно алгоритма: суммируем числа дня и месяца рождения

x = 0
for i in birth_day:
      x += (int(i))
y = 0
for l in birth_month:
      y += int(l)

z = 0
for k in birth_year:
      z += int(k)

#Выведем 1 число
first_n = x + y

#Выведем 2 число
second_n = z

#Получим первое рабочее число
work_n1 = first_n + second_n
work_n1_test = work_n1 - 9
if work_n1_test <= 0:
    print("Первое число:", "0", work_n1)
else:
    print("Первое число:", work_n1)

#Выведем второе рабочее число
sum = 0
work_n1 = str(work_n1)
for n in work_n1:
      sum += int(n)
sum_test = sum - 9
work_n2 = sum
if sum_test <= 0:
   print("Второе число:", "0", work_n2)
else:
    print("Второе число:", work_n2)

#Выведем третье рабочее число
birth_day = int(birth_day)
add = birth_day // 10
birth_day = str(birth_day)
work_n1 = int(work_n1)
work_n3 = work_n1 - add * 2
work_n3_test = work_n3 - 9
if work_n3_test <= 0:
   print("Третье число:", "0", work_n3)
else:
    print("Третье число:", work_n3)

#Выведем четвертое рабочее число
sum = 0
work_n3 = str(work_n3)
for p in work_n3:
      sum += int(p)
      work_n3 = work_n1 - add * 2
sum5_test = sum - 9
work_n4 = sum
if sum5_test <= 0:
    print("Четвертое число:", "0", work_n4)
else:
    print("Четвертое число:", work_n4)
