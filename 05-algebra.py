''' Algebra e desafio intermediário '''

import numpy as np

# Inicializando tipos diferentes de Arrays

# Zeros/Ones
np.zeros(3)
np.zeros([3,5])
np.zeros([2,3,5])

np.ones([4,2,2])

# outros números
np.full([3,3], 21)

# método full_like
a = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 1, 2, 3, 4, 5]])
np.full_like(a, 25)

# números aleatórios
np.random.rand(2,2,3)

# números inteiros aleatórios
np.random.randint(7, size=(2,3,5))
np.random.randint(7, 10, size=(2,3,5))

# Operações de algebra
# matriz identidade
np.identity(5)

# repetição de array em linhas
ex = np.array([[1,2,3]])
np.repeat(ex, 3)
np.repeat(ex, 3, axis=0)