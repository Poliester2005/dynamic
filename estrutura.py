
# Função para capturar os movimentos do cirurgião
def capturar_movimentos():
    movimentos = []
    # Captura fictícia de movimentos
    movimentos.append({"posicao": (1.0, 2.5, 3.0), "rotacao": (0.1, 0.2, 0.3), "botao": True})
    movimentos.append({"posicao": (1.5, 2.8, 3.2), "rotacao": (0.1, 0.3, 0.4), "botao": False})
    return movimentos

# Função para armazenar resultados intermediários
def armazenar_resultados(tempo_execucao, erros, precisao):
    resultados = []
    resultados.append({"tempo_execucao": tempo_execucao, "erros": erros, "precisao": precisao})
    return resultados

# Função para avaliar o desempenho do cirurgião
def avaliar_desempenho(cirurgiao, tempo_execucao, erros, precisao):
    avaliacao = {}
    feedback = ""
    if precisao > 90 and erros < 5:
        feedback = "Bom desempenho."
    else:
        feedback = "Precisa melhorar a precisão."
    avaliacao[cirurgiao] = {
        "tempo_execucao": tempo_execucao,
        "erros": erros,
        "precisao": precisao,
        "feedback": feedback
    }
    return avaliacao

# Exemplo de chamadas

# Capturando movimentos do cirurgião
movimentos_cirurgiao = capturar_movimentos()
print("Movimentos do Cirurgião:", movimentos_cirurgiao)

# Armazenando resultados intermediários
resultados = armazenar_resultados(120.5, 2, 94.5)
print("Resultados Intermediários:", resultados)

# Avaliando o desempenho
avaliacao_cirurgiao_1 = avaliar_desempenho("cirurgiao_1", 120.5, 2, 94.5)
print("Avaliação do Cirurgião:", avaliacao_cirurgiao_1)
