''' Manipulação de dados em linhas e colunas '''

import numpy as np

a = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 1, 2, 3, 4, 5]])
#print(a, a.shape)

# Acessando valores (slicing)
a[0, 5] # 1º valor linhas e o 2º para colunas
a[0]
a[0, -2]
a[:, 2] # pegar coluna específica
a[0, 1:]
a[1, 0::2]
a[::-1] # inverter valores da matriz
a[:, ::-1] # inverter colunas da matriz

# Atribuição de valores
a[1,5] = 34
a[:,2] = 35

# Exemplos com matriz 3D (Tridimensional)
b = np.array([[[1,2], [3,4]], [[5,6], [7,8]]])
print(b, b.shape)
b.ndim
b[0] # acessando primeira matriz
b[0,1] # acessando 1ª matriz e a 1ª linha
b[0,1,0] # acessando 1ª matriz / 1ª linha / 1º valor
b[0,1,0] = 21 # acessando 1ª matriz / 1ª linha / 1º valor e alterando o valor
b[1,0,:] # acessando todos os valores da 1ª linha da 2ª matriz
b[0,:,1] # acessando todos os valores da 2ª coluna da 1ª matriz
b[0,1] = [22, 23] # alterando mais de um valor
b[0, 1].shape
b[0].shape
