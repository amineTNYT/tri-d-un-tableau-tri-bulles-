from numpy import array

def saisir():
    n = int(input("taille de tableau=:"))
    while not (3 <= n <= 11):
        n = int(input("taille de tableau=:"))
    return n

def remplir(n):
    for i in range(n):
        t[i] = int(input("t[" + str(i) + "]="))
    return t

def affiche(t, n):
    for i in range(n):
        print(t[i], end="|")

def tribulle(n): 
    p = True
    while p == True:
        p = False
        for i in range(n - 1):
            if t[i] > t[i + 1]: #ordre croissante
                aux = t[i + 1]
                t[i + 1] = t[i]
                t[i] = aux
                p = True
        n=n-1
    return t

# programme principal
n = saisir()
t = array([int] * n) #tableau t est de type entier 
t = remplir(n)
print('tableau finale: avant le tri')
affiche(t, n)
t = tribulle(n) 
print('tableau finale: après le tri')
affiche(t, n)










