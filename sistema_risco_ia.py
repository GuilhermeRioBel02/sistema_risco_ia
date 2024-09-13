import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Definindo as variáveis de entrada
credito = ctrl.Antecedent(np.arange(0, 11, 1), 'credito')
renda = ctrl.Antecedent(np.arange(0, 11, 1), 'renda')
divida = ctrl.Antecedent(np.arange(0, 11, 1), 'divida')

# Definindo a variável de saída
risco = ctrl.Consequent(np.arange(0, 11, 1), 'risco')

# Definindo as funções de pertinência
credito['ruim'] = fuzz.trimf(credito.universe, [0, 0, 5])
credito['bom'] = fuzz.trimf(credito.universe, [0, 5, 10])
credito['excelente'] = fuzz.trimf(credito.universe, [5, 10, 10])

renda['baixa'] = fuzz.trimf(renda.universe, [0, 0, 5])
renda['media'] = fuzz.trimf(renda.universe, [0, 5, 10])
renda['alta'] = fuzz.trimf(renda.universe, [5, 10, 10])

divida['baixa'] = fuzz.trimf(divida.universe, [0, 0, 5])
divida['moderada'] = fuzz.trimf(divida.universe, [0, 5, 10])
divida['alta'] = fuzz.trimf(divida.universe, [5, 10, 10])

risco['baixo'] = fuzz.trimf(risco.universe, [0, 0, 5])
risco['medio'] = fuzz.trimf(risco.universe, [0, 5, 10])
risco['alto'] = fuzz.trimf(risco.universe, [5, 10, 10])

# Definindo as regras
regra1 = ctrl.Rule(credito['excelente'] & divida['baixa'], risco['baixo'])
regra2 = ctrl.Rule(credito['ruim'] & divida['alta'], risco['alto'])
regra3 = ctrl.Rule(credito['bom'] & renda['media'] & divida['moderada'], risco['medio'])

# Criando o sistema de controle
sistema_risco = ctrl.ControlSystem([regra1, regra2, regra3])
simulacao = ctrl.ControlSystemSimulation(sistema_risco)

# Atribuindo valores e computando o risco
simulacao.input['credito'] = 7
simulacao.input['renda'] = 5
simulacao.input['divida'] = 3
simulacao.compute()

# Mostrando o resultado
print(f"Risco calculado: {simulacao.output['risco']}")

print(simulacao.output.keys())
