def calculate_eight() -> list[str]:
    return ["5 + 3", "10 - 2", "4 * 2", "16 // 2"]
expressao = calculate_eight()
resultados = [eval(exp) for exp in expressao]
