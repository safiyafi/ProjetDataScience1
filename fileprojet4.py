"""Extraire et créer un fichier EXCEL contenant les statistiques globales de l’école"""

import csv

f = open('EcoleDakar.csv')
fichierCSV = csv.reader(f, delimiter = ';')
lignes = [row for row in fichierCSV]
effectif = len(lignes)
print("L'effectif des élèves dans l'école est :", effectif)

   
"""Moyenne de l'école"""
somme = 0
for i in range (1,50):
    colones = [row for row in lignes[i]]
    a = float(colones[3])
    somme = somme + a
mean = somme / effectif
Mean = round(mean,2)
print("La moyenne de l'école est :", Mean)

    
F_effectif = 0
M_effectif = 0

"""Pourcentage de fille""" 
for i in range (1,50):
    colones = [row for row in lignes[i]]
    b = colones[7]
    if b == 'F':
       F_effectif += 1
    else :
       M_effectif += 1
print("L'effectif des filles dans l'école est égal à :", F_effectif , "filles")
print("L'effectif des garçons dans l'école est égal à :", M_effectif, "garçons")

f_pourcentage = (F_effectif * 100 / effectif)
F_pourcentage = round(f_pourcentage,2)
print("le pourcentage de filles dans l'école est :", F_pourcentage)

"""pourcentage de garçons"""
m_pourcentage = (M_effectif * 100 / effectif)
M_pourcentage = round(m_pourcentage,2)

print("le pourcentage de filles dans l'école est :", M_pourcentage)


"""La région qui a les meilleurs élèves ( la région ayant enregistré la plus forte moyenne)"""
max = 0
for i in range (1,50):
    colones = [row for row in lignes[i]]
    c = float(colones[3])
    if c > max :
        max = c
    d = colones[5]
print("La meilleure note enrégistrée au niveau de l'école est : ",max)

print("La région où la meilleure note a été enrégistrée est : ", d )

"""Les Statistiques de l'école"""
of = open('StatistiquesEcole', 'w', newline = '')
ofichierCSV = csv.writer(of, delimiter = ';', quoting=csv.QUOTE_ALL)

ofichierCSV.writerow(["Moyenne totale", "Pourcentage Filles", "Pourcentage Garçons", "Région d'excellence"])
listeA = []
listeA.append(Mean)
listeB = []
listeB.append(F_pourcentage)
listeC = []
listeC.append(M_pourcentage)
listeD = []
listeD.append(d)

ofichierCSV.writerow([listeA, listeB, listeC, listeD])
        

    

