from collections import deque

# 1: Criando a lista
frutas = ["Maca", "Laranja", "Banana", "Pera", "Kiwi", "Manga"]

# 2: Pilha — append() e pop() → LIFO (último a entrar, primeiro a sair)
frutas.append("Uva")
frutas.append("Pêssego")
frutas.append("Melão")
frutas.pop()  # remove o último: "Melão"

# Fila — deque com appendleft()/popleft() → FIFO (primeiro a entrar, primeiro a sair)
frutas = deque(frutas)       # converte a lista para deque mantendo os elementos
frutas.append("Melancia")    # adiciona no fim
frutas.append("Tangerina")   # adiciona no fim
frutas.appendleft("Abacaxi") # insere no início (característica da fila)

# 3: Laço para imprimir todos os elementos
for fruta in frutas:
    print(f"Fruta: {fruta}")

# 4: Condição para imprimir somente Maçã e Laranja
print("\nSomente Maçã e Laranja:")
for fruta in frutas:
    if fruta in ("Maca", "Laranja"):
        print(fruta)