import cv2
import numpy

def desenhar(data):
    w, h = 600, 800
    imagem = numpy.full((w, h, 3), (30, 30, 30), dtype=numpy.uint8)
    tamanho_face = (w//2)//2
    quadrados = tamanho_face//3
    y_meio = w//2 - (tamanho_face)//2
    x_meio = h//2 - (tamanho_face * 2)
    coordenadas = [(x_meio, y_meio), (x_meio + tamanho_face, y_meio), (x_meio + tamanho_face*2, y_meio), (x_meio + tamanho_face*3, y_meio), (x_meio + tamanho_face, y_meio - tamanho_face), (x_meio + tamanho_face, y_meio + tamanho_face)]
    faces = [data[i:i+9] for i in range(0, len(data), 9)]
    for index, face in enumerate(faces, start = 0):
        for i in range(3):
            for j in range(3):
                x, y = coordenadas[index]
                x += j * quadrados
                y += i * quadrados
                imagem = cv2.rectangle(imagem, (x, y), (x + quadrados, y + quadrados), face[i * 3 + j], -1)
    
    cv2.imshow('Camera', imagem)
    key = cv2.waitKey()