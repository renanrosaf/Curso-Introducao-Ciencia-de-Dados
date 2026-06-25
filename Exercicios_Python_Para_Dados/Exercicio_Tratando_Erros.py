# Variáveis iniciais
total = 0
soma_notas = 0.0
qtd_nota = 0

# Try externo: valida o total de alunos
try:
    total = int(input("Digite o total de alunos da sala: "))
    if total <= 0:
        raise ValueError("O total de alunos deve ser maior que zero.")

except ValueError as e:
    print(f"Erro: {e}. Digite um número inteiro positivo.")
    total = 0  # garante que o while não execute

# Loop de coleta de notas
while qtd_nota < total:
    # Try interno: valida cada nota individualmente
    try:
        nota = float(input(f"Digite a nota do aluno {qtd_nota + 1}/{total}: "))

        if nota < 0 or nota > 10:
            raise ValueError("Nota deve estar entre 0 e 10.")

        soma_notas += nota  # ← acumula corretamente na variável separada
        qtd_nota += 1

    except ValueError as e:
        print(f"Nota inválida: {e} Tente novamente.")

# Try da divisão — exigido pelo exercício
try:
    media_notas = soma_notas / total
    print(f"\nMédia de notas da turma: {media_notas:.2f}")

except ZeroDivisionError:
    print("Erro: Nenhum aluno cadastrado, divisão por zero.")

finally:
    print(f"Total de notas cadastradas: {qtd_nota}")