# Calcula os inputs do Perceptron
def perceptron(inputs, weights, bias):
    weighted_sum = sum(i * w for i, w in zip(inputs, weights)) + bias
    
    # Output do Perceptron: 1 = Sim, 0 = Não
    return 1 if weighted_sum >= 0 else 0

# Exemplo 1: Teste de Sim
inputs1 = [2, -1, 0.5]
weights1 = [0.6, 0.4, -1.5]
bias1 = 0.7
output1 = perceptron(inputs1, weights1, bias1)
print(f"Acha que é uma boa ideia tomar uma água gelada? {'Sim' if output1 == 1 else 'Não'}")

# Exemplo 2: Teste de Não
inputs2 = [1, 2, -1]
weights2 = [-0.5, 0.3, 0.8]
bias2 = -0.2
output2 = perceptron(inputs2, weights2, bias2)
print(f"Usar casaco nesse calor vale a pena? {'Sim' if output2 == 1 else 'Não'}")

# Exemplo 3: Confirmação do Teste de Sim
inputs3 = [0, 1, 1.5]
weights3 = [0.9, -0.4, 0.7]
bias3 = 0.1
output3 = perceptron(inputs3, weights3, bias3)
print(f"Uma ventania seria uma boa agora? {'Sim' if output3 == 1 else 'Não'}")
