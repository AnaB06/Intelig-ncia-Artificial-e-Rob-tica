# #pip install scikit-fuzzy

import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
from skfuzzy import control as ctrl

# #Variaveis de Entrada (Antecedent)
# calorias = ctrl.Antecedent(np.arange(0, 5000, 100), 'calorias')

# #Variaveis de saída (Consequent)
# peso = ctrl.Consequent(np.arange(0, 300, 10), 'peso')

# # automf -> Atribuição de categorias automaticamente
# calorias.automf(names=['caloria baixa','caloria media','muita caloria'],)

# # atribuicao sem o automf
# peso['pesado'] = fuzz.gaussmf(peso.universe, 90, 25)
# peso['medio'] = fuzz.gaussmf(peso.universe, 60, 15)
# peso['leve'] = fuzz.gaussmf(peso.universe, 10, 10)


# #Visualizando as variáveis
# calorias.view()
# peso.view()



# #Criando as regras
# regra_1 = ctrl.Rule(calorias['caloria baixa'], peso['leve'])
# regra_2 = ctrl.Rule(calorias['caloria media'], peso['medio'])
# regra_3 = ctrl.Rule(calorias['muita caloria'], peso['pesado'])

# controlador = ctrl.ControlSystem([regra_1, regra_2, regra_3])


# #Simulando
# Calculopeso = ctrl.ControlSystemSimulation(controlador)

# notacalorias = int(input('calorias: '))
# Calculopeso.input['calorias'] = notacalorias
# Calculopeso.compute()

# valorpeso = Calculopeso.output['peso']

# print("\ncalorias %d \npeso de %5.2f" %(
#         notacalorias,
#         valorpeso))


# calorias.view(sim=Calculopeso)
# peso.view(sim=Calculopeso)

# plt.show()


#pip install scikit-fuzzy

import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
from skfuzzy import control as ctrl

# Variáveis de Entrada (Antecedent)
calorias = ctrl.Antecedent(np.arange(0, 5000, 100), 'calorias')

# Variáveis de saída (Consequent)
peso = ctrl.Consequent(np.arange(0, 300, 10), 'peso')

# Definindo as funções de pertinência para calorias manualmente
calorias['baixa'] = fuzz.trapmf(calorias.universe, [0, 0, 1000, 2000])
calorias['media'] = fuzz.trimf(calorias.universe, [1500, 2500, 3500])
calorias['alta'] = fuzz.trapmf(calorias.universe, [3000, 4000, 5000, 5000])

# Definindo as funções de pertinência para peso manualmente
peso['leve'] = fuzz.gaussmf(peso.universe, 50, 15)
peso['medio'] = fuzz.gaussmf(peso.universe, 80, 20)
peso['pesado'] = fuzz.gaussmf(peso.universe, 120, 30)

# Visualizando as variáveis
calorias.view()
peso.view()

# Criando as regras
regra_1 = ctrl.Rule(calorias['baixa'], peso['leve'])
regra_2 = ctrl.Rule(calorias['media'], peso['medio'])
regra_3 = ctrl.Rule(calorias['alta'], peso['pesado'])

# Criando o controlador de sistema
controlador = ctrl.ControlSystem([regra_1, regra_2, regra_3])

# Simulação
Calculopeso = ctrl.ControlSystemSimulation(controlador)

# Entrada de calorias
notacalorias = int(input('Quantas calorias: '))
Calculopeso.input['calorias'] = notacalorias
Calculopeso.compute()

# Resultado de peso
valorpeso = Calculopeso.output['peso']

# Exibindo o resultado
print("\nCalorias: %d \nPeso estimado: %.2f kg" % (notacalorias, valorpeso))

# Visualizando os gráficos com os resultados
calorias.view(sim=Calculopeso)
peso.view(sim=Calculopeso)

plt.show()

