
# Ecrire * par ordre croissant
n = int(input('Entrer un nombre : '))
for i in range(1, n+1, 1):
    str = ''
    for j in range(1, i+1, 1):
        str = str + '*'
    print(str)


