import numpy as np

linhas = int(input('Digite o número de linhas: '))
colunas = int(input('Digite o número de colunas: '))
matriz = np.zeros((linhas,colunas), dtype=int)
for l in range(linhas):
    for c in range(colunas):
        matriz[l][c] = int(input(f'Digite um valor para a posição [{l}][{c}]: '))
print(matriz)