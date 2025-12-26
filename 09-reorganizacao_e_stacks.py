''' Reorganizações e Stacks '''

import numpy as np

# Reorganização de arrays
matriz = np.array([[1,2,3,4], [5,6,7,8]]) # formato (2, 4)

matriz.reshape([4,2]) # (4, 2)
matriz.reshape([1,8]) # (1, 8)
matriz.reshape([8,1]) # (8, 1)

# Stack de Vetores - Concatenação de vetores de mesma dimensão
v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])

np.vstack([v1,v2])
np.hstack([v1,v2])

a = np.vstack([v1,v1,v2,v2])
np.vstack([a,v2])

# Tanto para vstack quanto para hstack é necessário ter o mesmo nº de colunas (v) e linhas (h)


# Mudança de dtype
a.dtype
a = a.astype('float32')