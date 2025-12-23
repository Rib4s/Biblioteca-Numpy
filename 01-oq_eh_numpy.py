''' O que é Numpy? '''

### Definição ###

'''NumPy é uma biblioteca fundamental da linguagem Python voltada para 
computação científica e matemática, amplamente utilizada para manipulação 
eficiente de dados numéricos. Ela fornece suporte a arrays multidimensionais e matrizes, 
além de uma grande coleção de funções matemáticas de alto desempenho para 
operações como álgebra linear, estatística, transformadas de Fourier e geração 
de números aleatórios. O NumPy é otimizado em baixo nível (escrito em C), 
o que o torna muito mais rápido do que listas Python para cálculos numéricos, 
sendo a base de diversas outras bibliotecas como Pandas, SciPy, Matplotlib e Scikit-learn.'''

import numpy as np

# Criar uma matriz (2lin x 3col)
matriz = np.array([[1, 2, 3], [4, 5, 6]])
print(matriz)