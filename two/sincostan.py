from math import sin, cos, tan, radians

a = int(input('Write an angle: '))
rad = radians(a)

s = sin(rad)
c = cos(rad)
t = tan(rad)

print(f'The sine of {a} is {s:.2f}.\nThe cosine of {a} is {c:.2f}.\nThe tangent of {a} is {t:.2f}.')
