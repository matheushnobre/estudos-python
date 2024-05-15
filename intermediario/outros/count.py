from itertools import count

# Count é um iterador sem fim
c = count(start=10, step=2)

print(next(c))
print(next(c))
print(next(c))
print(next(c))