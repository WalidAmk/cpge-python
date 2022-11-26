
# Algo 1

n = int(input('Entrer un nombre : '))
for i in range(1, n+1, 1):
    str = ''
    for j in range(1, i+1, 1):
        str = str + '*'
    print(str)


#*********
# Algo 2

'''
def creeInt(index, length):
    a = int(length/2) - index
    b = int(length / 2) + index
    if a < 0:
        a = a*(-1)
    if b > length - 1:
        b = length - a - 1

    lt = []
    for i in range(a, b+1, 1):
        lt.append(i)
    return lt
len = int(input('Entrer un nombre impaire : '))
if len%2 == 0:
    len = len + 1
for i in range(len):
    str = ''
    for j in range(len):
        if j in creeInt(i, len):
            str = str + '*'
        else:
            str = str + ' '
    print(str)
'''





