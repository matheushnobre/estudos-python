iterable = ['Eu', 'tenho', '__iter__']
iterator = iter(iterable)

for n in range(3):
    print(next(iterator))