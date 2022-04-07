import math

x1 = float(input("Digite primeiro valor de x: "))
y1 = float(input("Digite primeiro valor de y: "))
x2 = float(input("Digite segundo valor de x: "))
y2 = float(input("Digite segundo valor de y: "))

if x1 < 0 and x2 >= 0:  
    x3 = (x1*-1) + x2
elif x1 >= 0 and x2 < 0:
    x3 = x1 + (x2 * -1)
elif x1 < 0 and x2 < 0:
    if x1 > x2:
        x3 = x1 - x2
    else:
        x3 = x2 - x1
elif x1 >= 0 and x2 >= 0:
    if x1 >= x2:
        x3 = x1 - x2
    else:
        x3 = x2 - x1

if y1 < 0 and y2 >= 0:  
    y3 = (y1*-1) + y2
elif y1 >= 0 and y2 < 0:
    y3 = y1 + (y2 * -1)
elif y1 < 0 and y2 < 0:
    if y1 > y2:
        y3 = y1 - y2
    else:
        y3 = y2 - y1
elif y1 >= 0 and y2 >= 0:
    if y1 >= y2:
        y3 = y1 - y2    
    else:
        y3 = y2 - y1

resultado = math.sqrt(x3**2 + y3**2) 

if resultado >= 10:
    print("longe")
else:
    print("perto")    