''' Advanced Indexing – Boolean Masking '''

import numpy as np

dados = np.random.randint(0, 20, size=(5,5))
dados > 10
dados[dados > 10]

np.any(dados > 10)
np.any(dados > 10, axis=0)
np.any(dados > 10, axis=1)

np.all(dados > 10)
np.all(dados > 10, axis=0)
np.all(dados > 10, axis=1)

# mais de uma condição
((dados > 10) & (dados > 15)) # condição se verdadeiro
~((dados > 10) & (dados > 15)) # inverso da condição

# acessando índices da matriz
a = np.array([1,2,3,4,5,6,7,8,9,10])
a[[1, 2, 9]]
a[[1, 2, -1]]
a[[-9, 2, -1]] == a[[1, 2, 9]]