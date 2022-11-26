

x = int(input('Entrer un nombre : '))

for i in range(1, x+1, 1):
    str = ''
    for j in range(1, i+1, 1):
        str = str + '*'
    print(str)


