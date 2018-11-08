"""Extraire et créer un fichier EXCEL contenant la liste des élèves ayant la moyenne"""
"""Extaction des élèves ayant la moyenne"""
import csv

f = open('EcoleDakar.csv')
fichierCSV = csv.reader(f, delimiter = ';')


header = next(fichierCSV)
print(header)
lignes = [row for row in fichierCSV]

listeX = []
listeY = []
listeZ = []
print("La liste des élèves ayant la moyenne est : ", )
for i in range (1,50):
    colones = [row for row in lignes[i]]
    mean = colones[3]
    if mean >= '10' :
      x = colones[0]
      y = colones[1]
      z= colones[3]
      print(x, y, z)
      listeX.append(x)
      listeY.append(y)
      listeZ.append(z)

"""print(listeX)
print(listeY)
print(listeZ)"""

"""Création d'un fichier CSV contenant la liste des élèves ayant la moyenne """

of = open('EleveMoyenne.csv', 'w', newline = '')
ofichierCSV = csv.writer(of, delimiter = ';', quoting=csv.QUOTE_ALL)

ofichierCSV.writerow(["Nom", "Prénom", "Moyenne"])
ofichierCSV.writerow([listeX, listeY, listeZ])
        

