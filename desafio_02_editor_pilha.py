# Desafio 2: Editor de texto com opção de "desfazer"
# Estrutura utilizada: pilha (lista) com append() e pop() — comportamento LIFO

pilha = []

while True:
    print("\nEDITOR DE TEXTO")
    print("[1] - Digitar palavra")
    print("[2] - Desfazer última palavra")
    print("[3] - Mostrar texto")
    print("[4] - Sair")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        palavra = input("Digite uma palavra: ").strip()
        if palavra != "":
            pilha.append(palavra)
            print(f"Palavra adicionada: {palavra}")
        else:
            print("Nenhuma palavra digitada.")

    elif opcao == "2":
        if len(pilha) > 0:
            removida = pilha.pop()
            print(f"Palavra removida: {removida}")
        else:
            print("Nada para desfazer. O editor está vazio.")

    elif opcao == "3":
        if len(pilha) > 0:
            print("Texto atual: " + " ".join(pilha))
        else:
            print("O editor está vazio.")

    elif opcao == "4":
        print("Saindo do editor.")
        break

    else:
        print("Opção inválida. Tente novamente.")
