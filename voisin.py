import sys
import math

# Don't let the machines win. You are humanity's last hope...

grid = []

width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis
for i in range(height):
    line = input()  # width characters, each either 0 or .
    grid.append(line)
    
for i in range(height):
    for j in range(width):
        if grid[i][j] == '0':
            x1, y1 = j, i  # Coordonnées du nœud
            
            # Recherche du voisin de droite
            if j < width - 1:
                for k in range(j + 1, width):
                    if grid[i][k] == '0':
                        x2, y2 = k, i  # Coordonnées du voisin de droite
                        break
                else:
                    x2, y2 = -1, -1  # Aucun voisin de droite
            else:
                x2, y2 = -1, -1  # Aucun voisin de droite
            
            # Recherche du voisin du bas
            if i < height - 1:
                for k in range(i + 1, height):
                    if grid[k][j] == '0':
                        x3, y3 = j, k  # Coordonnées du voisin du bas
                        break
                else:
                    x3, y3 = -1, -1  # Aucun voisin du bas
            else:
                x3, y3 = -1, -1  # Aucun voisin du bas
            
            print(f"{x1} {y1} {x2} {y2} {x3} {y3}")
