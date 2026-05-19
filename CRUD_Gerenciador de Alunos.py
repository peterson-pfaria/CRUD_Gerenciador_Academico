
lista_estudantes = []
lista_professores = []
lista_disciplinas = []
lista_turmas = []
lista_matriculas = []

codigo_estudante = 1
codigo_professor = 1
codigo_disciplina = 1
codigo_turma = 1
codigo_matricula = 1

# Menu
def menu_principal():
    print("\n" + "-"*10, "MENU PRINCIPAL", "-"*10)
    print("(1) Gerenciar Estudantes")
    print("(2) Gerenciar Professores")
    print("(3) Gerenciar Disciplinas")
    print("(4) Gerenciar Turmas")
    print("(5) Gerenciar Matrículas")
    print("(9) Sair")
    return input("Escolha uma opção: ")

def menu_operacoes(tipo):
    print(f"\n{'*'*10} [{tipo.upper()}] MENU DE OPERAÇÕES {'*'*10}")
    print("(1) Incluir")
    print("(2) Listar")
    print("(3) Atualizar")
    print("(4) Excluir")
    print("(9) Voltar ao menu principal")
    return input("Escolha uma operação: ")

#Gerador de codigos
def gerador_codigos(tipo):
    global codigo_estudante, codigo_professor, codigo_disciplina, codigo_turma, codigo_matricula
    if tipo == "estudante":
        codigo = codigo_estudante
        codigo_estudante += 1
    elif tipo == "professor":
        codigo = codigo_professor
        codigo_professor += 1
    elif tipo == "disciplina":
        codigo = codigo_disciplina
        codigo_disciplina += 1
    elif tipo == "turma":
        codigo = codigo_turma
        codigo_turma += 1
    elif tipo == "matricula":
        codigo = codigo_matricula
        codigo_matricula += 1
    return codigo

def localizador_codigos(lista, codigo):
    for item in lista:
        if item["codigo"] == codigo:
            return item
    return None

def inclusao(lista, tipo, campos):
    print(f"\n{'='*10} Inclusão de {tipo.title()} {'='*10}")
    item = {"codigo": gerador_codigos(tipo)}
    for campo in campos:
        item[campo] = input(f"Digite o {campo} do {tipo}: ")
    lista.append(item)
    print(f"{tipo.title()} incluído com sucesso! Código: {item['codigo']}")

def listagem(lista, tipo):
    print(f"\n{'='*10} Listagem de {tipo.title()}s {'='*10}")
    if not lista:
        print(f"Nenhum {tipo} cadastrado.")
    else:
        for item in lista:
            dados = " | ".join(f"{k}: {v}" for k, v in item.items())
            print(dados)

def atualizacao(lista, tipo, campos):
    print(f"\n{'='*10} Edição de {tipo.title()} {'='*10}")
    try:
        codigo = int(input("Digite o código para editar: "))
        item = localizador_codigos(lista, codigo)
        if item:
            for campo in campos:
                novo_valor = input(f"Novo {campo} ({item[campo]}): ")
                if novo_valor:
                    item[campo] = novo_valor
            print(f"{tipo.title()} atualizado com sucesso!")
        else:
            print(f"{tipo.title()} não encontrado.")
    except ValueError:
        print("Código inválido.")

def exclusao(lista, tipo):
    print(f"\n{'='*10} Exclusão de {tipo.title()} {'='*10}")
    try:
        codigo = int(input("Digite o código para excluir: "))
        item = localizador_codigos(lista, codigo)
        if item:
            lista.remove(item)
            print(f"{tipo.title()} excluído com sucesso!")
        else:
            print(f"{tipo.title()} não encontrado.")
    except ValueError:
        print("Código inválido.")
print("Bem vindo ao Sistema")
while True:
    opcao = menu_principal()
    if opcao == "1":
        while True:
            operacao = menu_operacoes("Estudantes")
            if operacao == "1":
                inclusao(lista_estudantes, "estudante", ["nome", "cpf"])
            elif operacao == "2":
                listagem(lista_estudantes, "estudante")
            elif operacao == "3":
                atualizacao(lista_estudantes, "estudante", ["nome", "cpf"])
            elif operacao == "4":
                exclusao(lista_estudantes, "estudante")
            elif operacao == "9":
                break
            else:
                print("Opção inválida.")

    elif opcao == "2": 
        while True:
            operacao = menu_operacoes("Professores")
            if operacao == "1":
                inclusao(lista_professores, "professor", ["nome", "cpf"])
            elif operacao == "2":
                listagem(lista_professores, "professor")
            elif operacao == "3":
                atualizacao(lista_professores, "professor", ["nome", "cpf"])
            elif operacao == "4":
                exclusao(lista_professores, "professor")
            elif operacao == "9":
                break
            else:
                print("Opção inválida.")

    elif opcao == "3":
        while True:
            operacao = menu_operacoes("Disciplinas")
            if operacao == "1":
                inclusao(lista_disciplinas, "disciplina", ["nome"])
            elif operacao == "2":
                listagem(lista_disciplinas, "disciplina")
            elif operacao == "3":
                atualizacao(lista_disciplinas, "disciplina", ["nome"])
            elif operacao == "4":
                exclusao(lista_disciplinas, "disciplina")
            elif operacao == "9":
                break
            else:
                print("Opção inválida.")

    elif opcao == "4": 
        while True:
            operacao = menu_operacoes("Turmas")
            if operacao == "1":
                inclusao(lista_turmas, "turma", ["nome"])
            elif operacao == "2":
                listagem(lista_turmas, "turma")
            elif operacao == "3":
                atualizacao(lista_turmas, "turma", ["nome"])
            elif operacao == "4":
                exclusao(lista_turmas, "turma")
            elif operacao == "9":
                break
            else:
                print("Opção inválida.")

    elif opcao == "5":
        while True:
            operacao = menu_operacoes("Matrículas")
            if operacao == "1":
                inclusao(lista_matriculas, "matricula", ["id_estudante", "id_turma"])
            elif operacao == "2":
                listagem(lista_matriculas, "matricula")
            elif operacao == "3":
                atualizacao(lista_matriculas, "matricula", ["id_estudante", "id_turma"])
            elif operacao == "4":
                exclusao(lista_matriculas, "matricula")
            elif operacao == "9":
                break
            else:
                print("Opção inválida.")

    elif opcao == "9":
        print("Saindo do sistema... Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")