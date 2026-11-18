#Eu so importei isso para usar a fila
from collections import deque
#Aqui, esse import e apenas para limpar o terminal, para ficar mais bonito
import os

ARQUIVO = "dados_sistema.txt"

fila_pacientes = deque()
pilha_prontuarios = []
pacientes_internados = []

id_lista = 99
id_fila = 204
id_pilha_num = 888

def carregar_dados():
    global id_lista, id_fila, id_pilha_num
    if not os.path.exists(ARQUIVO):
        return
    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            if linha == "":
                continue
            partes = linha.split("|")
            tipo = partes[0]
            if tipo == "LISTA" and len(partes) == 5:
                pacientes_internados.append({"id": partes[1], "nome": partes[2], "leito": partes[3], "status": partes[4]})
                num = int(partes[1])
                if num > id_lista:
                    id_lista = num
            elif tipo == "FILA" and len(partes) == 4:
                fila_pacientes.append({"id": partes[1], "nome": partes[2], "prioridade": partes[3]})
                num = int(partes[1])
                if num > id_fila:
                    id_fila = num
            elif tipo == "PILHA" and len(partes) == 4:
                pilha_prontuarios.append({"id": partes[1], "paciente": partes[2], "procedimento": partes[3]})
                num = int(partes[1].split("-")[1])
                if num > id_pilha_num:
                    id_pilha_num = num

carregar_dados()

def mostrar_fila():
    pos = 1
    for paciente in fila_pacientes:
        print("Paciente: "+paciente["nome"]+" ----- ID: "+paciente["id"]+" ----- Prioridade: "+paciente["prioridade"]+" ----- Posicao: "+str(pos))
        pos+=1

def adicionar_paciente():
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        nome = input("Digite o nome do paciente: ")
        prioridade = input("Digite a prioridade: ")
        if nome == "" or prioridade == "":
            print("Preencha todos os campos!")
        else:
            global id_fila
            id_fila += 1
            fila_pacientes.append({"id": str(id_fila), "nome": nome, "prioridade": prioridade})
            with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
                for f in fila_pacientes:
                    arquivo.write("FILA|"+f["id"]+"|"+f["nome"]+"|"+f["prioridade"]+"\n")
                for p in pilha_prontuarios:
                    arquivo.write("PILHA|"+p["id"]+"|"+p["paciente"]+"|"+p["procedimento"]+"\n")
                for l in pacientes_internados:
                    arquivo.write("LISTA|"+l["id"]+"|"+l["nome"]+"|"+l["leito"]+"|"+l["status"]+"\n")
            print("Paciente adicionado na fila com sucesso!")
    except Exception as e:
        print(f"Erro: {e}")
    print("Deseja adicionar outro paciente? SIM - NAO")
    resp = input()
    if resp == "SIM":
        adicionar_paciente()
    else:
        print("Voltando ao menu")

def remover_paciente():
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        if len(fila_pacientes) == 0:
            print("Fila vazia!")
        else:
            fila_pacientes.popleft()
            with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
                for f in fila_pacientes:
                    arquivo.write("FILA|"+f["id"]+"|"+f["nome"]+"|"+f["prioridade"]+"\n")
                for p in pilha_prontuarios:
                    arquivo.write("PILHA|"+p["id"]+"|"+p["paciente"]+"|"+p["procedimento"]+"\n")
                for l in pacientes_internados:
                    arquivo.write("LISTA|"+l["id"]+"|"+l["nome"]+"|"+l["leito"]+"|"+l["status"]+"\n")
            print("Paciente removido do inicio da fila com sucesso!")
    except Exception as e:
        print(f"Erro: {e}")
    print("Deseja remover outro paciente? SIM - NAO")
    resp = input()
    if resp == "SIM":
        remover_paciente()
    else:
        print("Voltando ao menu")

def atualizar_paciente():
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        paciente_antigo = input("Digite o nome do paciente a ser atualizado: ")
        encontrado = False
        for p in fila_pacientes:
            if p["nome"] == paciente_antigo:
                paciente_novo = input("Digite o novo nome: ")
                nova_prioridade = input("Digite a nova prioridade: ")
                p["nome"] = paciente_novo
                p["prioridade"] = nova_prioridade
                with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
                    for f in fila_pacientes:
                        arquivo.write("FILA|"+f["id"]+"|"+f["nome"]+"|"+f["prioridade"]+"\n")
                    for p2 in pilha_prontuarios:
                        arquivo.write("PILHA|"+p2["id"]+"|"+p2["paciente"]+"|"+p2["procedimento"]+"\n")
                    for l in pacientes_internados:
                        arquivo.write("LISTA|"+l["id"]+"|"+l["nome"]+"|"+l["leito"]+"|"+l["status"]+"\n")
                print("Paciente atualizado com sucesso!")
                encontrado = True
                break
        if not encontrado:
            print("Paciente não encontrado na fila!")
    except Exception as e:
        print(f"Erro: {e}")
    print("Deseja atualizar outro paciente? SIM - NAO")
    resp = input()
    if resp == "SIM":
        atualizar_paciente()
    else:
        print("Voltando ao menu")

def mostrar_prontuarios():
    pos = 1
    for prontuario in pilha_prontuarios:
        print("Prontuario: "+prontuario["paciente"]+" ----- ID: "+prontuario["id"]+" ----- Procedimento: "+prontuario["procedimento"]+" ----- Posicao: "+str(pos))
        pos+=1

def adicionar_prontuario():
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        paciente = input("Digite o nome do paciente: ")
        procedimento = input("Digite o procedimento: ")
        if paciente == "" or procedimento == "":
            print("Preencha todos os campos!")
        else:
            global id_pilha_num
            id_pilha_num += 1
            id_str = "PRONT-"+str(id_pilha_num)
            pilha_prontuarios.append({"id": id_str, "paciente": paciente, "procedimento": procedimento})
            with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
                for f in fila_pacientes:
                    arquivo.write("FILA|"+f["id"]+"|"+f["nome"]+"|"+f["prioridade"]+"\n")
                for p in pilha_prontuarios:
                    arquivo.write("PILHA|"+p["id"]+"|"+p["paciente"]+"|"+p["procedimento"]+"\n")
                for l in pacientes_internados:
                    arquivo.write("LISTA|"+l["id"]+"|"+l["nome"]+"|"+l["leito"]+"|"+l["status"]+"\n")
            print("Prontuario adicionado com sucesso!")
    except Exception as e:
        print(f"Erro: {e}")
    print("Deseja adicionar outro prontuario? SIM - NAO")
    resp = input()
    if resp == "SIM":
        adicionar_prontuario()
    else:
        print("Voltando ao menu")

def remover_prontuario():
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        if len(pilha_prontuarios) == 0:
            print("Pilha vazia!")
        else:
            pilha_prontuarios.pop()
            with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
                for f in fila_pacientes:
                    arquivo.write("FILA|"+f["id"]+"|"+f["nome"]+"|"+f["prioridade"]+"\n")
                for p in pilha_prontuarios:
                    arquivo.write("PILHA|"+p["id"]+"|"+p["paciente"]+"|"+p["procedimento"]+"\n")
                for l in pacientes_internados:
                    arquivo.write("LISTA|"+l["id"]+"|"+l["nome"]+"|"+l["leito"]+"|"+l["status"]+"\n")
            print("Prontuario removido do topo com sucesso!")
    except Exception as e:
        print(f"Erro: {e}")
    print("Deseja remover outro prontuario? SIM - NAO")
    resp = input()
    if resp == "SIM":
        remover_prontuario()
    else:
        print("Voltando ao menu")

def atualizar_prontuario():
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        id_antigo = input("Digite o ID do prontuario a ser atualizado: ")
        encontrado = False
        for p in pilha_prontuarios:
            if p["id"] == id_antigo:
                paciente_novo = input("Digite o novo nome do paciente: ")
                procedimento_novo = input("Digite o novo procedimento: ")
                p["paciente"] = paciente_novo
                p["procedimento"] = procedimento_novo
                with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
                    for f in fila_pacientes:
                        arquivo.write("FILA|"+f["id"]+"|"+f["nome"]+"|"+f["prioridade"]+"\n")
                    for p2 in pilha_prontuarios:
                        arquivo.write("PILHA|"+p2["id"]+"|"+p2["paciente"]+"|"+p2["procedimento"]+"\n")
                    for l in pacientes_internados:
                        arquivo.write("LISTA|"+l["id"]+"|"+l["nome"]+"|"+l["leito"]+"|"+l["status"]+"\n")
                print("Prontuario atualizado com sucesso!")
                encontrado = True
                break
        if not encontrado:
            print("Prontuario não encontrado!")
    except Exception as e:
        print(f"Erro: {e}")
    print("Deseja atualizar outro prontuario? SIM - NAO")
    resp = input()
    if resp == "SIM":
        atualizar_prontuario()
    else:
        print("Voltando ao menu")

def mostrar_pacientes():
    pos = 1
    for paciente in pacientes_internados:
        print("Paciente: "+paciente["nome"]+" ----- ID: "+paciente["id"]+" ----- Leito: "+paciente["leito"]+" ----- Status: "+paciente["status"]+" ----- Posicao: "+str(pos))
        pos+=1

def cadastrar_paciente():
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        nome = input("Digite o nome do paciente: ")
        leito = input("Digite o leito: ")
        status = input("Digite o status (Estavel ou Observacao): ")
        if nome == "" or leito == "" or status == "":
            print("Preencha todos os campos!")
        else:
            global id_lista
            id_lista += 1
            pacientes_internados.append({"id": str(id_lista), "nome": nome, "leito": leito, "status": status})
            with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
                for f in fila_pacientes:
                    arquivo.write("FILA|"+f["id"]+"|"+f["nome"]+"|"+f["prioridade"]+"\n")
                for p in pilha_prontuarios:
                    arquivo.write("PILHA|"+p["id"]+"|"+p["paciente"]+"|"+p["procedimento"]+"\n")
                for l in pacientes_internados:
                    arquivo.write("LISTA|"+l["id"]+"|"+l["nome"]+"|"+l["leito"]+"|"+l["status"]+"\n")
            print("Paciente cadastrado com sucesso!")
    except Exception as e:
        print(f"Erro: {e}")
    print("Deseja cadastrar outro paciente? SIM - NAO")
    resp = input()
    if resp == "SIM":
        cadastrar_paciente()
    else:
        print("Voltando ao menu")

def remover_paciente_lista():
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        nome = input("Digite o nome do paciente a ser removido: ")
        encontrado = False
        for p in pacientes_internados:
            if p["nome"] == nome:
                pacientes_internados.remove(p)
                with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
                    for f in fila_pacientes:
                        arquivo.write("FILA|"+f["id"]+"|"+f["nome"]+"|"+f["prioridade"]+"\n")
                    for p2 in pilha_prontuarios:
                        arquivo.write("PILHA|"+p2["id"]+"|"+p2["paciente"]+"|"+p2["procedimento"]+"\n")
                    for l in pacientes_internados:
                        arquivo.write("LISTA|"+l["id"]+"|"+l["nome"]+"|"+l["leito"]+"|"+l["status"]+"\n")
                print("Paciente removido com sucesso!")
                encontrado = True
                break
        if not encontrado:
            print("Paciente não encontrado!")
    except Exception as e:
        print(f"Erro: {e}")
    print("Deseja remover outro paciente? SIM - NAO")
    resp = input()
    if resp == "SIM":
        remover_paciente_lista()
    else:
        print("Voltando ao menu")

def atualizar_paciente_lista():
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        nome = input("Digite o nome do paciente a ser atualizado: ")
        encontrado = False
        for p in pacientes_internados:
            if p["nome"] == nome:
                novo_leito = input("Digite o novo leito: ")
                novo_status = input("Digite o novo status: ")
                p["leito"] = novo_leito
                p["status"] = novo_status
                with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
                    for f in fila_pacientes:
                        arquivo.write("FILA|"+f["id"]+"|"+f["nome"]+"|"+f["prioridade"]+"\n")
                    for p2 in pilha_prontuarios:
                        arquivo.write("PILHA|"+p2["id"]+"|"+p2["paciente"]+"|"+p2["procedimento"]+"\n")
                    for l in pacientes_internados:
                        arquivo.write("LISTA|"+l["id"]+"|"+l["nome"]+"|"+l["leito"]+"|"+l["status"]+"\n")
                print("Paciente atualizado com sucesso!")
                encontrado = True
                break
        if not encontrado:
            print("Paciente não encontrado!")
    except Exception as e:
        print(f"Erro: {e}")
    print("Deseja atualizar outro paciente? SIM - NAO")
    resp = input()
    if resp == "SIM":
        atualizar_paciente_lista()
    else:
        print("Voltando ao menu")

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print("======================")
    print("(1) - Controle de Atendimentos")
    print("(2) - Controle de Prontuarios")
    print("(3) - Controle de Pacientes")
    print("(4) - Controle de Especialidades")
    print("(5) - Sair")
    print("======================")

    try:
        r = int(input("Digite uma opção: "))

        if r == 1:
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("===============Controle de Atendimentos=================")
                print("(1) - Inserir paciente na fila")
                print("(2) - Remover paciente da fila")
                print("(3) - Atualizar paciente da fila")
                print("(4) - Consultar fila de pacientes")
                print("(5) - Voltar")
                print("================================")

                try:
                    op = int(input("Digite uma opção: "))

                    if op == 5:
                        break
                    elif op == 1:
                        adicionar_paciente()
                    elif op == 2:
                        remover_paciente()
                    elif op == 3:
                        atualizar_paciente()
                    elif op == 4:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        mostrar_fila()
                        input("\nPressione ENTER para continuar...")
                    else:
                        print("Digite uma opção válida!")
                        input("\nPressione ENTER para continuar...")

                except ValueError:
                    print("Digite apenas números!")
                    input("\nPressione ENTER para continuar...")

        elif r == 2:
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("===============Controle de Prontuarios=================")
                print("(1) - Inserir prontuario")
                print("(2) - Remover prontuario")
                print("(3) - Atualizar prontuario")
                print("(4) - Consultar prontuarios")
                print("(5) - Voltar")
                print("================================")

                try:
                    op = int(input("Digite uma opção: "))

                    if op == 5:
                        break
                    elif op == 1:
                        adicionar_prontuario()
                    elif op == 2:
                        remover_prontuario()
                    elif op == 3:
                        atualizar_prontuario()
                    elif op == 4:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        mostrar_prontuarios()
                        input("\nPressione ENTER para continuar...")
                    else:
                        print("Digite uma opção válida!")
                        input("\nPressione ENTER para continuar...")

                except ValueError:
                    print("Digite apenas números!")
                    input("\nPressione ENTER para continuar...")

        elif r == 3:
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("===============Controle de Pacientes=================")
                print("(1) - Cadastrar Paciente")
                print("(2) - Remover Paciente")
                print("(3) - Atualizar Paciente")
                print("(4) - Consultar Pacientes")
                print("(5) - Voltar")
                print("================================")

                try:
                    op = int(input("Digite uma opção: "))

                    if op == 5:
                        break
                    elif op == 1:
                        cadastrar_paciente()
                    elif op == 2:
                        remover_paciente_lista()
                    elif op == 3:
                        atualizar_paciente_lista()
                    elif op == 4:
                        os.system('cls' if os.name == 'nt' else 'clear')
                        mostrar_pacientes()
                        input("\nPressione ENTER para continuar...")
                    else:
                        print("Digite uma opção válida!")
                        input("\nPressione ENTER para continuar...")

                except ValueError:
                    print("Digite apenas números!")
                    input("\nPressione ENTER para continuar...")

        elif r == 4:
            while True:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("===============Controle de Especialidades=================")
                print("(1) - Cadastrar Especialidade")
                print("(2) - Remover Especialidade")
                print("(3) - Atualizar Especialidade")
                print("(4) - Consultar Especialidades")
                print("(5) - Voltar")
                print("================================")

                try:
                    op = int(input("Digite uma opção: "))

                    if op == 5:
                        break
                    elif op in (1, 2, 3, 4):
                        print("Opção selecionada:", op)
                        input("\nPressione ENTER para continuar...")
                    else:
                        print("Digite uma opção válida!")
                        input("\nPressione ENTER para continuar...")

                except ValueError:
                    print("Digite apenas números!")
                    input("\nPressione ENTER para continuar...")

        elif r == 5:
            print("Encerrando o programa...")
            break

        else:
            print("Digite uma opção válida!")
            input("\nPressione ENTER para continuar...")

    except ValueError:
        print("Digite apenas números!")
        input("\nPressione ENTER para continuar...")