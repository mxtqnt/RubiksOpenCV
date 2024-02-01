import csv
from camera import camera
from plano2d import desenhar
from normalizacao import conferencia

data = camera()
data = [elemento for vetor in data for elemento in vetor]

matriz = [[0 for _ in range(3)] for _ in range(18)] 
contador = 0
for i in range(18):
    for j in range(3):
        matriz[i][j] = data[contador]
        contador += 1

corescentrais = [data[i] for i in [4, 13, 22, 31, 40, 49]]

data = conferencia(corescentrais, data)

desenhar(data)