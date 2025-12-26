''' Matemática Intermediária e Cópias '''

import numpy as np
import math

# Cuidado ao copiar matrizes
# atenção no exemplo abaixo temos:
a = np.array([1,2,3])
b = a # duas variáveis apontando para o mesmo objeto na memória
b[0] = 256
print(b)
print(a)
a[2] = 21
print(a)
print(b)
# quando se altera a o b tbm muda

# Maneira recomendada para copiar usar .copy():
a = np.array([1,2,3])
b = a.copy()
b[0] = 256
print(b)
print(a)

# Operações matemáticas
a = np.array([1,2,3,4])

a + 2
a - 2
a * 2
a ** 2
print(a)
a += 5 # é possível fazer atribuições
print(a)

# multiplicando matrizes:
b = np.array([5, -5, 5, -5])
a - b

# Operações matemáticas mais complexas
a = a * math.pi
np.cos(a)
np.sin(a)