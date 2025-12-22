#                                                                                     ALGORITHME TRI BULLE

## 1️⃣ Tri à bulles — Boucle « Répéter … Jusqu’à »
```
Procédure tri_bulle (@ T : tab ; n : entier)
Début
    Répéter
        permut ← Faux
        Pour i de 0 à n - 2 faire
            Si T[i] > T[i + 1] alors
                Aux ← T[i]
                T[i] ← T[i + 1]
                T[i + 1] ← Aux
                permut ← Vrai
            Fin si
        Fin Pour
    Jusqu’à (permut = Faux)
Fin
```
```
  ###    TDOL
Objet    | Type / Nature
-----------------------
i        | Entier
Aux      | Entier
permut   | Booléen
```

<img width="703" height="366" alt="Capture d’écran 2025-11-02 145915" src="https://github.com/user-attachments/assets/66d2fec1-3f5d-4394-8eb8-0fdb16956875" />



# 2️⃣ Tri à bulles — Boucle « Tant que »
```
Procédure Tribulles (@ T : Tab ; n : entier)
Début
    permut ← Vrai
  
    Tant que (permut = Vrai) faire
        permut ← Faux
        Pour i de 0 à n - 2 faire
            Si T[i] > T[i + 1] alors
                aux ← T[i + 1]
                T[i + 1] ← T[i]
                T[i] ← aux
                permut ← Vrai
            FinSi
        FinPour
  
        n ← n - 1
    Fin tant que
Fin
```

```
#      TDOL

Objets     | Type / Nature
-------------------------
permut     | Booléen
i, aux     | Entier
```
<img width="977" height="707" alt="Capture d’écran 2025-12-14 110920" src="https://github.com/user-attachments/assets/22997cc7-8faf-4634-882e-7f198d8120ee" />

