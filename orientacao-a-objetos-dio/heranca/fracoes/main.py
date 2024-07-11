import Fraction as f

a = f.Fraction(-2, 5)
b = f.Fraction(6, 9)

print(f'Frações criadas: \nA = {a}\nB = {b}')
print(f'A: numerador = {a.getNum()}, denominador = {a.getDen()}')
print(f'B: numerador = {b.getNum()}, denominador = {b.getDen()}')

print('\nOperações')
print(f'A + B = {a+b}')
print(f'A - B = {a-b}')
print(f'B - A = {b-a}')
print(f'A * B = {a*b}')
print(f'A / B = {a/b}')
print(f'B / A = {b/a}')

print('\nTestando operadores')
print('A == B?', a==b)
print('A != B', a!=b)
print('A > B?', a>b)
print('A >= B?', a>=b)
print('A < B?', a<b)
print('A <= B?', a<=b)