# Desafio 02
import numpy as np

m = np.arange(1,31).reshape(6,5)
print(m)

# Questões:
# 1- Faça um slice que retorna a ultima linha da matriz
m[-1]

# 2- Faça um slice na matriz que retorne uma 
# matriz utilizando os números: 19, 20, 24, 25
m[3:5, 3:]

# 3- Retorne a média dos valores das últimas 3 linhas
np.mean(m[3:]) # Geral 3 linhas
np.mean(m[3])
np.mean(m[4])
np.mean(m[5])

# 4- Retorne a diagonal que vai do nº 2 até o nº 20
m[[0,1,2,3],[1,2,3,4]]

# 5- Queremos o retorno sendo uma matriz do tipo:
'''   [ 4,  5
       24, 25
       29, 30]   '''

# solução 1:
m[[0,4,5], 3:]

# solução 2:
v1 = np.array(m[0, 3:])
v2 = np.array(m[4:, 3:])
np.vstack([v1,v2])
