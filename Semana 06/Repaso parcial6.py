n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())

p1 = float(input())
p2 = float(input())
p3 = float(input())
p4 = float(input())
p5 = float(input())

puntuacion_total = ((n1*p1)+(n2*p2)+(n3*p3)+(n4*p4)+(n5*p5))
print(f"{puntuacion_total:.0f}") # Siempre pone comillas cuando es formateado porque sino no agarra