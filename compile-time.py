a =int(input('Введите сторону а: '))
b = int(input('Введите сторону b: '))
c = int(input('Введите сторону c: '))

if a^2+b^2==c^2:
    print ('Прямоугольный')
elif a^2+c^2==b^2:
    print ('Прямоугольный')
else:
    if c^2+b^2==a^2:
        print ('Прямоугольный')
    else:
        print ('Не прямоугольный')