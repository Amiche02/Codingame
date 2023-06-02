import sys

N = int(input())
d = int(input())

produit = 1

for _ in range(N):
    x = int(input())
    produit *= x

if produit % d == 0:
    print("Perfect")
else:
    print("Imperfect")
