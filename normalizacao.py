def calcular_diferenca_cores(cor1, cor2):
    diferenca = 0
    for i in range(3):
        diferenca += abs(cor1[i] - cor2[i])

    return diferenca

def encontrar_cor_mais_proxima(cor_referencia, vetor_cores):
    menor_diferenca = float('inf')
    cor_mais_proxima = None

    for cor in vetor_cores:
        diferenca = calcular_diferenca_cores(cor_referencia, cor)
        if diferenca < menor_diferenca:
            menor_diferenca = diferenca
            cor_mais_proxima = cor

    return cor_mais_proxima

def conferencia(corescentrais, coresfoto):
    verde    = corescentrais[0]
    laranja  = corescentrais[1]
    azul     = corescentrais[2]
    vermelho = corescentrais[3]
    amarelo  = corescentrais[4]
    branco   = corescentrais[5]

    coresdesenho = [(72, 155, 0, 0), (0, 88, 255, 0), (173, 70, 0, 0), (52, 18, 183, 0), (0, 213, 255, 0), (255, 255, 255, 0)]

    # corverde    = (72, 155, 0, 0)
    # corlaranja  = (0, 88, 255, 0)
    # corazul     = (173, 70, 0, 0)
    # corvermelho = (52, 18, 183, 0)
    # coramarelo  = (0, 213, 255, 0)
    # corbranco   = (55, 255, 255, 0)

    cores_vetor = [azul, laranja, vermelho, verde, amarelo, branco]
    cores_nomes = ['azul', 'laranja', 'vermelho', 'verde', 'amarelo', 'branco']

    for indexcorpadrao, item in enumerate(coresfoto, start = 0):
        cor_referencia = item
        cor_mais_proxima = encontrar_cor_mais_proxima(cor_referencia, cores_vetor)
        for index, corpadrao in enumerate(cores_vetor, start = 0):
            if corpadrao == cor_mais_proxima:
                nome_cor_proxima = cores_nomes[index]
                coresfoto[indexcorpadrao] = coresdesenho[index]
        print(f'A cor mais próxima de {cor_referencia} é {nome_cor_proxima}')

    return coresfoto