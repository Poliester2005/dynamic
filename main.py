import random

# Função para capturar os movimentos do cirurgião
def capturar_movimentos():
    movimentos = []
    for _ in range(10):  # Simulando 10 movimentos
        movimento = {
            "posicao": (round(random.uniform(1.0, 5.0), 2), round(random.uniform(1.0, 5.0), 2), round(random.uniform(1.0, 5.0), 2)),
            "rotacao": (round(random.uniform(0.1, 1.0), 2), round(random.uniform(0.1, 1.0), 2), round(random.uniform(0.1, 1.0), 2)),
            "botao": random.choice([True, False])  # Simulando estado do botão
        }
        movimentos.append(movimento)
    return movimentos

# Função para executar a simulação
def executar_simulacao(movimentos):
    tempo_execucao = len(movimentos) * random.uniform(10, 15)  # Cada movimento leva entre 10-15 segundos
    erros = sum([1 for mov in movimentos if mov["botao"] is False])  # Conta quantos movimentos com o botão não pressionado
    precisao = round(random.uniform(80, 100), 2)  # Simulação de uma precisão entre 80% e 100%
    
    resultados = {
        "tempo_execucao": tempo_execucao,
        "erros": erros,
        "precisao": precisao
    }
    return resultados

# Função para avaliar o desempenho
def avaliar_desempenho(resultados):
    feedback = ""
    if resultados["precisao"] > 90 and resultados["erros"] < 3:
        feedback = "Excelente precisão e poucos erros."
    elif resultados["precisao"] > 80 and resultados["erros"] < 5:
        feedback = "Bom desempenho, mas atenção aos erros."
    else:
        feedback = "Desempenho abaixo do esperado, precisa melhorar."
    
    avaliacao = {
        "tempo_execucao": resultados["tempo_execucao"],
        "erros": resultados["erros"],
        "precisao": resultados["precisao"],
        "feedback": feedback
    }
    return avaliacao

# Função para gerar relatório
def gerar_relatorio(avaliacao):
    relatorio = f"""
    Relatório de Desempenho:
    ------------------------
    Tempo de Execução: {avaliacao['tempo_execucao']} segundos
    Erros Cometidos: {avaliacao['erros']}
    Precisão: {avaliacao['precisao']}%
    
    Feedback: {avaliacao['feedback']}
    """
    return relatorio

# Exemplo de execução
movimentos = capturar_movimentos()
resultados_simulacao = executar_simulacao(movimentos)
avaliacao_final = avaliar_desempenho(resultados_simulacao)
relatorio_final = gerar_relatorio(avaliacao_final)

print(relatorio_final)
