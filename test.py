import math as m
import sys as s
a = int(input("Введите первое число (a): "))
b = int(input("Введите второе число (b): "))
c = int(input("Введите третье число (c): "))
d = b ** 2 - 4 * a * c


if a == 0:
    print("Коэффицент при первом слагаемом уравнения не может быть равным нулю, измените его и попробуйте снова. Иначе вы пишите не квадратное уравнение :(")
    s.exit()

if d < 0:
    print("D = ", d)
    print("Так как дискриминант меньше нуля,то уравнение не имеет действительных решений")

if d == 0:
    x = -(b / (2 * a))
    if a < 0:
    	print("D = ", b, "^ 2 - 4 * (", a, ") * ", c, " = ", d)
    elif c < 0:
    	print("D = ", b, "^ 2 - 4 * ", a, " * (", c, ") = ", d)
    elif b < 0:
    	print("D = (", b, ")^ 2 - 4 * ", a, " * ", c, " = ", d)
    elif a < 0 and b < 0:
    	print("D = (", b, ")^ 2 - 4 * (", a, ") * ", c, " = ", d)
    elif a < 0 and b < 0 and c < 0:
    	print("D = (", b, ")^ 2 - 4 * (", a, ") * (", c, ") = ", d)
    elif b < 0 and c < 0:
    	print("D = (", b, ")^ 2 - 4 * ", a, " * (", c, ") = ", d)
    else:
    	print("D = ", b, "^ 2 - 4 * ", a, " * ", c, " = ", d)
    print("D = ", d)
    print("Так как дискриминант равен нулю, то уравнение имеет один корень")
    print("x = ", x)
		
if d > 0:
    x = (-b + m.sqrt(d)) / (2 * a)
    y = (-b - m.sqrt(d)) / (2 * a)
    if a < 0:
    	print("D = ", b, "^ 2 - 4 * (", a, ") * ", c, " = ", d)
    elif c < 0:
    	print("D = ", b, "^ 2 - 4 * ", a, " * (", c, ") = ", d)
    elif b < 0:
    	print("D = (", b, ")^ 2 - 4 * ", a, " * ", c, " = ", d)
    elif a < 0 and b < 0:
    	print("D = (", b, ")^ 2 - 4 * (", a, ") * ", c, " = ", d)
    elif a < 0 and b < 0 and c < 0:
    	print("D = (", b, ")^ 2 - 4 * (", a, ") * (", c, ") = ", d)
    elif b < 0 and c < 0:
    	print("D = (", b, ")^ 2 - 4 * ", a, " * (", c, ") = ", d)
    else:
    	print("D = ", b, "^ 2 - 4 * ", a, " * ", c, " = ", d)
    print("D = ", d)
    print("Так как дискриминант больше нуля, то уравнение имеет два корня")
    print("x1 = ", x)
    print("x2 = ", y)
