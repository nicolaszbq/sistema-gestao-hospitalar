#Eu so importei isso para usar a fila
from collections import deque
#Aqui, esse import e apenas para limpar o terminal, para ficar mais bonito
import os


def pegar_no_filho(no, valor):
    if no is None:
        return None

    if no.nome.lower() == valor.lower():
        return no

    for sub in no.subcategorias:
        if sub.nome.lower() == valor.lower():
            return sub
    return None

ARQUIVO = "dados_sistema.txt"

class No:
    def __init__(self, nome):
        self.nome = nome
        self.subcategorias = []


def salvar_dados():
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        for f in fila_pacientes:
            arquivo.write("FILA|"+f["id"]+"|"+f["nome"]+"|"+f["prioridade"]+"\n")
        for p in pilha_prontuarios:
            arquivo.write("PILHA|"+p["id"]+"|"+p["paciente"]+"|"+p["procedimento"]+"\n")
        for l in pacientes_internados:
            arquivo.write("LISTA|"+l["id"]+"|"+l["nome"]+"|"+l["leito"]+"|"+l["status"]+"\n")
        for esp_no in arvore_clinica_geral.subcategorias:
            for caso_no in esp_no.subcategorias:
                arquivo.write("ARVORE|"+arvore_clinica_geral.nome+"|"+esp_no.nome+"|"+caso_no.nome+"\n")

fila_pacientes = deque()
pilha_prontuarios = []
pacientes_internados = []
arvore_clinica_geral = No("Clinica Geral")

id_lista = 99
id_fila = 204
id_pilha_num = 888

def carregar_dados():
    print("Carregando dados...")
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
                print("Carregando listas...")
                pacientes_internados.append({"id": partes[1], "nome": partes[2], "leito": partes[3], "status": partes[4]})
                num = int(partes[1])
                if num > id_lista:
                    id_lista = num
            elif tipo == "FILA" and len(partes) == 4:
                print("Carregando filas...")
                fila_pacientes.append({"id": partes[1], "nome": partes[2], "prioridade": partes[3]})
                num = int(partes[1])
                if num > id_fila:
                    id_fila = num
            elif tipo == "PILHA" and len(partes) == 4:
                print("Carregando pilhas...")
                pilha_prontuarios.append({"id": partes[1], "paciente": partes[2], "procedimento": partes[3]})
                num = int(partes[1].split("-")[1])
                if num > id_pilha_num:
                    id_pilha_num = num
            elif tipo == "ARVORE" and len(partes) == 4:
                especialidade_nome = partes[2]
                caso_nome = partes[3]
                esp_no = pegar_no_filho(arvore_clinica_geral, especialidade_nome)
                if esp_no is None:
                    esp_no = No(especialidade_nome)
                    arvore_clinica_geral.subcategorias.append(esp_no)
                caso_no = pegar_no_filho(esp_no, caso_nome)
                if caso_no is None:
                    esp_no.subcategorias.append(No(caso_nome))

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
            salvar_dados()
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
            salvar_dados()
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
                salvar_dados()
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
    os.system('cls' if os.name == 'nt' else 'clear')
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
            salvar_dados()
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
            salvar_dados()
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
                salvar_dados()
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
    os.system('cls' if os.name == 'nt' else 'clear')
    pos = 1
    for paciente in pacientes_internados:
        print("Paciente: "+paciente["nome"]+" ----- ID: "+paciente["id"]+" ----- Leito: "+paciente["leito"]+" ----- Status: "+paciente["status"]+" ----- Posicao: "+str(pos))
        pos+=1
    input("\nPressione ENTER para continuar...")

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
            salvar_dados()
            print("Paciente cadastrado com sucesso!")
    except Exception as e:
        print(f"Erro: {e}")
    print("Deseja cadastrar outro paciente? SIM - NAO")
    resp = input().upper().strip()
    if resp == "SIM":
        cadastrar_paciente()
    else:
        input("\nPressione ENTER para continuar...")

def remover_paciente_lista():
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        nome = input("Digite o nome do paciente a ser removido: ")
        encontrado = False
        for p in pacientes_internados:
            if p["nome"] == nome:
                pacientes_internados.remove(p)
                salvar_dados()
                print("Paciente removido com sucesso!")
                encontrado = True
                break
        if not encontrado:
            print("Paciente não encontrado!")
    except Exception as e:
        print(f"Erro: {e}")
    print("Deseja remover outro paciente? SIM - NAO")
    resp = input().upper().strip()
    if resp == "SIM":
        remover_paciente_lista()
    else:
        input("\nPressione ENTER para continuar...")

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
                salvar_dados()
                print("Paciente atualizado com sucesso!")
                encontrado = True
                break
        if not encontrado:
            print("Paciente não encontrado!")
    except Exception as e:
        print(f"Erro: {e}")
    print("Deseja atualizar outro paciente? SIM - NAO")
    resp = input().upper().strip()
    if resp == "SIM":
        atualizar_paciente_lista()
    else:
        input("\nPressione ENTER para continuar...")

#Controle de especialidades
def mostrar_especialidades():
    os.system('cls' if os.name == 'nt' else 'clear')
    if len(arvore_clinica_geral.subcategorias) == 0:
        print("Nenhum dado na arvore!")
        input("\nPressione ENTER para continuar...")
        return
    print(arvore_clinica_geral.nome)
    for sub in arvore_clinica_geral.subcategorias:
        print("----" + sub.nome)
        for ins in sub.subcategorias:
            print("     -" + ins.nome)
    input("\nPressione ENTER para continuar...")

def verificar_existencia_especialidade(no, valor):
    if no is None:
        return False
    if no.nome.lower() == valor.lower():
        return True
    for sub in no.subcategorias:
        if verificar_existencia_especialidade(sub, valor):
            return True
    return False

def cadastrar_especialidade():
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        nome = input("Digite o nome da especialidade (subcategoria)").strip()
        if not nome:
            print("O nome não pode ser vazio!")
            return
        
        if verificar_existencia_especialidade(arvore_clinica_geral, nome):
            print("A especialidade ja existe!")
            return
        else:
            sub = No(nome)
            arvore_clinica_geral.subcategorias.append(sub)
            print("Especialidadae cadastrada com sucesso!")
            salvar_dados()
            input("\nPressione ENTER para continuar...")
    except Exception as e:
        print(f"Erro: {e}")

def cadastrar_tipo_caso():
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        esp = input("Digite o nome da especialidade a ser inserida! \n").strip()

        if not esp:
            print("A especialidade nao pode estar vazia!")
            return
        
        if verificar_existencia_especialidade(arvore_clinica_geral, esp):
            caso = input("Digite o tipo de caso:\n").strip()
            if not caso:
                print("O caso nao pode estar vazio!")
                return
            
            no = pegar_no_filho(arvore_clinica_geral, esp)

            if verificar_existencia_especialidade(no, caso):
                print("Esse caso ja existe!")
                return
            
            no.subcategorias.append(No(caso))    
            print("Caso adicionado com sucesso!")
            salvar_dados()
            input("\nPressione ENTER para continuar...")
        else:
            print("Essa especialidade nao existe!")
    except Exception as e:
        print(f"Erro: {e}")

def atualizar_especialidade():
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        esp = input("Digite o nome da especialidade: \n").strip()
        if not esp:
            print("A especialidade nao pode estar vazia!")
            return
        if verificar_existencia_especialidade(arvore_clinica_geral,esp):
            esp_antiga = pegar_no_filho(arvore_clinica_geral, esp)
            novo_nome = input("Digite o novo nome: \n").strip()
            if not novo_nome:
                print("O novo nome nao pode estar vazio!")
                return
            esp_antiga.nome = novo_nome
            print("Especialidade Atualizada com sucesso!")
            salvar_dados()
            input("\nPressione ENTER para continuar...")
        else:
            print("Essa especialidade nao existe!")
            return
    except Exception as e:
        print(f"Erro: {e}")
       
def atualizar_caso():
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        esp = input("Digite o nome da especialidade: \n").strip()
        if not esp:
            print("A especialidade nao pode estar vazia!")
            return
        if verificar_existencia_especialidade(arvore_clinica_geral,esp):
            caso_antigo_nome = input("Digite o nome do codigo a ser alterado: \n").strip()
            if not caso_antigo_nome:
                print("O caso nao pode estar vazio")
                return
            especialidade_pai = pegar_no_filho(arvore_clinica_geral, esp)
            if verificar_existencia_especialidade(especialidade_pai, caso_antigo_nome):
                caso_antigo = pegar_no_filho(especialidade_pai, caso_antigo_nome)

                novo_nome = input("Digite o novo nome: \n").strip()
                if not novo_nome:
                    print("O novo nome nao pode estar vazio!")
                    return
                if verificar_existencia_especialidade(especialidade_pai, novo_nome):
                    print("Este caso ja existe!")
                    return
                caso_antigo.nome = novo_nome
                print("Caso atualizado com sucesso!")
                salvar_dados()
                input("\nPressione ENTER para continuar...")
            else:
                print("Este caso nao existe!")
                return
        else:
            print("Essa especialidade nao existe!")
            return
    except Exception as e:
        print(f"Erro: {e}") 

def remover_especialidade():
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        esp = input("Digite o nome da especialidade: \n").strip()
        if not esp:
            print("A especialidade nao pode estar vazia!")
            return
        especialidade_antiga_no = pegar_no_filho(arvore_clinica_geral, esp)
        
        if especialidade_antiga_no is None or especialidade_antiga_no == arvore_clinica_geral:
            print("Essa especialidade nao existe!")
            return
        
        resp = input("Tem certeza que deseja remover a especialidade? Isso removera todos os casos junto. S - N").upper().strip()
        if resp not in ["S", "N"]:
            print("Voce deve digitar S ou N!")
            return
        if resp == "N":
            print("Operacao cancelada!")
            return
        print("Apagando casos...")
        especialidade_antiga_no.subcategorias.clear()
        print("Removendo especialidade...")
        arvore_clinica_geral.subcategorias.remove(especialidade_antiga_no)
        print("Especialidade removida com sucesso!")
        salvar_dados()
        input("\nPressione ENTER para continuar...")
        
    except Exception as e:
        print(f"Erro: {e}")

def remover_caso():
    os.system('cls' if os.name == 'nt' else 'clear')
    try:
        esp = input("Digite o nome da especialidade:\n").strip()
        if not esp:
            print("A especialidade nao pode estar vazia!")
            return
        esp_no = pegar_no_filho(arvore_clinica_geral, esp)
        if esp_no is None or esp_no == arvore_clinica_geral:
            print("Essa especialidade nao existe!")
            return
        caso = input("Digite o nome do caso a ser removido:\n").strip()
        if not caso:
            print("O nome do caso nao pode estar vazio!")
            return
        caso_no = pegar_no_filho(esp_no, caso)
        if caso_no is None or caso_no == esp_no:
            print("Esse caso nao existe!")
            return
        resp = input("Voce realmente deseja remover este caso? S - N: ").upper().strip()
        if resp not in ["S", "N"]:
            print("Voce deve digitar S ou N!")
            return
        if resp == "N":
            print("Operacao cancelada!")
            return
        print("Removendo caso...")
        esp_no.subcategorias.remove(caso_no)
        print("Caso removido com sucesso!")
        salvar_dados()
        input("\nPressione ENTER para continuar...")
    except Exception as e:
        print(f"Erro: {e}")

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
                print("(5) - Cadastrar Caso")
                print("(6) - Remover Caso")
                print("(7) - Atualizar Caso")
                print("(8) - Voltar")
                print("================================")

                try:
                    op = int(input("Digite uma opção: "))

                    if op == 8:
                        break
                    elif op == 1:
                        cadastrar_especialidade()
                    elif op == 2:
                        remover_especialidade()
                    elif op == 3:
                        atualizar_especialidade()
                    elif op == 4:
                        mostrar_especialidades()
                    elif op == 5:
                        cadastrar_tipo_caso()
                    elif op == 6:
                        remover_caso()
                    elif op == 7:
                        atualizar_caso()
                except Exception as e:
                    print(f"Error: {e}")

        elif r == 5:
            print("Encerrando o programa...")
            break

        else:
            print("Digite uma opção válida!")
            input("\nPressione ENTER para continuar...")

    except ValueError:
        print("Digite apenas números!")
        input("\nPressione ENTER para continuar...")