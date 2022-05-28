import re
buffer_len = 1
work_buffer = ""
h = 0
b = 0
j = 0
flag1 = False
flag2 = False
flag3 = False
try:
   while 1:
       k = input('Введите число k:')    #ввод числа k
       if (k >= '0') and (k <= '9'):
           digit = int(k)
           break
       else:
           print('Программа не может переводить числа в такую систему счисления, '
                 'либо такой системы счисления не существует.')
   with open("laba 2.txt", 'r+', encoding='utf-8') as file:   #открытие файла
       print("\n Результат работы программы.")
       buffer = file.read(buffer_len)     #чтение символа из файла
       if not buffer:     #если файл пуст
           print("\n Рабочий файл пустой.")
           flag3 = True
       while buffer:      #если файл не пуст
           work_buffer += buffer
           if re.findall(r'[.!?]', buffer):     #поиск конца предложения
               flag1 = True
               g = re.split(r'\D', work_buffer)
               g = g[:len(g) - 1]
               for i in range(len(g)):      #поиск чисел и их обработка
                   if g[i].isdigit():
                       if len(g[i]) != digit:
                           h += 1
                       else:
                           b += 1
               if h != 0 and b == 0:     #вывод предложений, которые соответсуют условию
                   flag2 = True
                   j += 1
                   if j == 1:
                       print("\nПредложения, в которых не содержатся ", digit, "- значные числа:")
                   print(work_buffer)
               h = 0
               b = 0
               work_buffer = ""
               g = ""
           buffer = file.read(buffer_len)
       if not flag2 and flag1:    #если нужных предложений не найдено
           print("\nВ файле отсутсвуют предложения, которые соответствуют условию задачи.")
       if not flag1 and not flag3:     #если нет знаков окончания предложения
           print("\nВ файле отсутствуют знаки препинания.")
except FileNotFoundError:       #отсутствие файла
   print("\nФайл проекта не обнаружен в директории.")