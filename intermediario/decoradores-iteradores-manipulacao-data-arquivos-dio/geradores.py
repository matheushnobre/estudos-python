def meu_gerador(numeros: list[int]):
    for num in numeros:
        yield num * 2

for i in meu_gerador(numeros=[1, 2, 3, 4, 5]):
    print(i)