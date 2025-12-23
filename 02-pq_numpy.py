''' Por que Numpy? '''

''' NumPy é usado porque torna o código mais rápido, 
mais simples e mais profissional, sendo indispensável 
para quem trabalha com análise de dados, ciência de dados, 
engenharia, finanças e machine learning.'''

import numpy as np

# Comparando com listas (multiplicando listas)
a = [1, 3, 5]
b = [5, 4, 7]

# a * b # Isso irá gerar um ERRO! Pois listas não têm essa funcionalidade.
# TypeError: can't multiply sequence by non-int of type 'list'

# Usando NumPy:
x = np.array([[1, 3, 5], [2, 3, 1]])
y = np.array([[5, 4, 7], [1, 2, 3]])

resultado = x * y
print(resultado)