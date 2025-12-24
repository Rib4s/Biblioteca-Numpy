# Desafio 01

import numpy as np

# Recriar a matriz abaixo:
# Não é válido fazer manualmente, fazer por slicing
'''
5  5  5  5  5
3  0  0  0  3
3  0  15 0  3
3  0  0  0  3
3  3  3  3  3
'''

# Resolução:

resultado = np.full([5,5],3) # criando uma matriz (5x5) com números 3
temporaria = np.zeros([3,3], dtype='int8') # criando matriz temp. com números 0
temporaria[1,1] = 15 # substituindo valor central para o nº 15 método slicing
resultado[
    1:-1, # filtrando as linhas 
    1:-1 # filtrando as colunas
    ] = temporaria # substituindo valores filtrados
resultado[0,:] = 5
