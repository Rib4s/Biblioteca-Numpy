''' Dimensões e Tipos de Dados '''

import numpy as np

# Conceitos inciais 
a = np.array([1, 2, 3])
print(a)


b = np.array([[1.0, 3.0], [2.0, 4.0]])
print(b)

# Dimensões de matrizes
a.ndim
b.ndim

# Formato
a.shape
b.shape

# Tipo de dado
a.dtype
b.dtype

# Tamanho de cada item da matriz (em bytes)
a.itemsize
b.itemsize

# É possível limitar o tamanho de array como no exemplo abaixo
idades = np.array([1, 2, 3, 27, 38], dtype='int8') # int8 -128 até 127
idades.dtype
idades.itemsize
idades.nbytes