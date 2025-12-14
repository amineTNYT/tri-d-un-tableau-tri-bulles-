                                                              ALGORITHME TRI BULLE

<img width="703" height="366" alt="Capture d’écran 2025-11-02 145915" src="https://github.com/user-attachments/assets/66d2fec1-3f5d-4394-8eb8-0fdb16956875" />
# tri_bulle boucle tanque


Procédure Tribulles (@ T :Tab ; n :entier)
Début
permut<---vrai
Tant que( permut=Vrai) faire
    permutFaux
    Pour i de 0 à n-2 faire
          Si (T[i]>T[i+1]) alors
          aux<---T[i+1]
          T[i+1]<---T[i]
          T[i]<---aux
          permut<---vrai
          FinSi
    FinPour
    n<---n-1
Fin tant que
Fin
