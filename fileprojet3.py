"""Extraire et créer un fichier EXCEL contenant les élèves ayant plus de 20 ans"""

"""Extraire la liste des élèves ayant plusde 20 ans dans un fichier CSV"""
import csv

f = open('EcoleDakar.csv')
fichierCSV = csv.reader(f, delimiter = ';')

lignes = [row for row in fichierCSV]
print(lignes[2])
colones = [row for row in lignes[2]]
print(colones[0],colones[1], colones[4])
listeX = []
listeY = []
listeZ = []
print("La liste des élèves ayant plus de 20 ans  est : ")
for i in range (1,50):
    colones = [row for row in lignes[i]]
    age = float(colones[4])
    if age > 20 :
      x = colones[0]
      y = colones[1]
      z = colones[4]
      print(x, y, z)
      listeX.append(x)
      listeY.append(y)
      listeZ.append(z)

"""print(listeX)
print(listeY)
print(listeZ"""

"""Ecrire la liste  des élèves aya plus 20 ans sur un fichier CSV"""     
of = open('EleveAgé.csv', 'w', newline = '')
ofichierCSV = csv.writer(of, delimiter = ';', quoting=csv.QUOTE_ALL)

ofichierCSV.writerow(["Nom", "Prénom", "Age"])
ofichierCSV.writerow([listeX, listeY, listeZ])
        
