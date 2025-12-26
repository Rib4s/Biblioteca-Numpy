''' Estatística Basica '''

import numpy as np

# Linear algebra
a = np.ones([2,3])
b = np.full([3,2], 5)
print(a)
print(b)
np.matmul(b,a)
np.matmul(a,b)

# Encontrar o determinante
identidade = np.identity(3)
np.linalg.det(identidade)

# Estatística
dados = np.random.randint(-50, 50, size=(10,10))
np.min(dados) # valor mínimo
np.max(dados) # valor máximo

# valor mínimo/máximo por coluna (0) e por linha (1)
np.min(dados, axis=0) # colunas
np.min(dados, axis=1) # linhas
np.max(dados, axis=0) # colunas
np.max(dados, axis=1) # linhas

# soma
np.sum(dados)
np.sum(dados, axis=0)
np.sum(dados, axis=1)

# média
np.mean(dados)
np.mean(dados, axis=0)
np.mean(dados, axis=1)
