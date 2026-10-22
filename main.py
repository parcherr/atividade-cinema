while True:
    print("""===== SISTEMA DE AVALIAÇÃO DO CINEMA =====

    1. Cadastrar avaliação
    2. Listar avaliações
    3. Consultar estatísticas
    4. Sair
    """)


    while True:
        opcao = int(input("Escolha uma opção: ")) 
        if opcao in [1, 2, 3, 4]:
            break
        else:
            print("Essa opção não é valida!")


    if opcao == 1: 
        print("")
        idade = int(input("Digite a sua idade: "))

        print("""
        OPÇÕES DE AVALIAÇÃO
        1. Ótimo
        2. Bom
        3. Regular
        4. Péssimo
        """)

        while True:
            avaliacao = int(input("Digite sua avaliação: "))
            if avaliacao in [1, 2, 3, 4]:

                if avaliacao == 1: 
                    avaliacao = "Ótimo"
                elif avaliacao == 2: 
                    avaliacao = "Bom"
                elif avaliacao == 3:
                    avaliacao = "Regular"
                elif avaliacao == 4: 
                    avaliacao = "Péssimo"

                break

            else:
                print("Essa opção não é valida!")

        with open("avaliacoes.txt", "a") as avaliacoes:
            avaliacoes.write(f"{idade};{avaliacao} \n")


    if opcao == 2:
        print("")
        print("""===== AVALIAÇÕES CADASTRADAS =====
        """)

        try:
            cont = 1
            with open("avaliacoes.txt", "r") as avaliacoes:
                for linha in avaliacoes: 
                    linha = linha.strip()
                    if linha != "":
                        idade, avaliacao = linha.split(";")
                        print(f"Cliente {cont} - Idade: {idade} - Avaliação: {avaliacao}")
                        cont += 1
        except FileNotFoundError:
            print("Erro: Não foi possível encontrar avaliações no arquivo .txt!")

        print("")


    if opcao == 3:
        print("")
        print("""===== ESTATÍSTICAS DAS AVALIAÇÕES =====
        """)

        try:
            avaliacaovelho = avaliacaonovo = None
            menoridade = 1000
            count = cotimo = cbom = cregular = cpessimo = maioridade = 0
            with open("avaliacoes.txt", "r") as avaliacoes:
                        for linha in avaliacoes: 
                            linha = linha.strip()
                            if linha != "":
                                idade, avaliacao = linha.split(";")
                                idade = int(idade)
                                print(idade, avaliacao)

                                if avaliacao == "Ã“timo":
                                    cotimo += 1
                                    avaliacao = "Ótimo"
                                elif avaliacao == "Bom":
                                    cbom += 1
                                elif avaliacao == "Regular":
                                    cregular += 1
                                elif avaliacao == "PÃ©ssimo":
                                    cpessimo += 1  
                                    avaliacao = "Péssimo"               
                                count += 1

                                if idade > maioridade:
                                    maioridade = idade
                                    avaliacaovelho = avaliacao

                                if idade < menoridade:
                                    menoridade = idade
                                    avaliacaonovo = avaliacao
        
            print(f"""
            Total de respondentes: {count}
            Ótimo: {cotimo}
            Bom: {cbom}
            Regular: {cregular}
            Péssimo: {cpessimo}
            Respondente mais velho:
            Idade: {maioridade}
            Avaliação: {avaliacaovelho}
            Respondente mais novo:
            Idade: {menoridade}
            Avaliação: {avaliacaonovo}
            """)

        except FileNotFoundError:
            print("Erro: Não foi possível encontrar avaliações no arquivo .txt!")
        print("")

    if opcao == 4:
        break

print("")
print("Obrigado por avaliar o nosso cinema!")