# Desafio 3: Fila de atendimento universitário
# Estrutura utilizada: fila (lista) com append() e pop(0) — comportamento FIFO

fila = []
contador_senha = 100  # Senha inicial

while True:
    print("\nSECRETARIA ACADÊMICA")
    print("[1] - Retirar senha")
    print("[2] - Chamar próximo aluno")
    print("[3] - Mostrar fila")
    print("[4] - Sair")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        nome = input("Nome do aluno: ").strip()
        if nome != "":
            fila.append(nome)
            print(f"{nome} entrou na fila de atendimento.")
        else:
            print("Nome inválido.")

    elif opcao == "2":
        if len(fila) > 0:
            proximo = fila.pop(0)
            print(f"Chamando aluno: {proximo}")
        else:
            print("A fila está vazia.")

    elif opcao == "3":
        if len(fila) > 0:
            print("Fila atual:")
            for i in range(len(fila)):
                print(f"{i + 1}º - {fila[i]}")
        else:
            print("A fila está vazia.")

    elif opcao == "4":
        print("Encerrando o sistema.")
        break

    else:
        print("Opção inválida. Tente novamente.")
