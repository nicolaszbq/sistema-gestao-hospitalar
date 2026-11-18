from collections import deque
import os

#Controle de Atendimentos funções
fila_pacientes = deque()
def mostrar_fila():
    pos = 1
    for paciente in fila_pacientes:
        print("Paciente: "+paciente + " ----- Posição: "+ str(pos))
        pos+=1

def adicionar_paciente():
    os.system('cls' if os.name == 'nt' else 'clear')

    try:
        paciente = input("Digite o nome do paciente: ")
        if paciente == "":
            print("Nome invalido! O nome nao pode ser vazio!")
    except Exception as e:
        print(f"Erro: {e}")
    print("Paciente adiconado na fila com sucesso!")
    fila_pacientes.append(paciente)
    print("Deseja adicionar outro paciente? SIM - NAO")
    resp = input()
    if resp == "SIM":
        adicionar_paciente()
    else:
        print("Voltando ao menu")

def remover_paciente():
    os.system('cls' if os.name == 'nt' else 'clear')

    try:
        paciente = input("Digite o nome do paciente a ser removido: ")
        if paciente in fila_pacientes:
            fila_pacientes.remove(paciente)
            print("Paciente removido da fila com sucesso!")
        else:
            print("Paciente não encontrado na fila!")
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
        if paciente_antigo in fila_pacientes:
            paciente_novo = input("Digite o novo nome do paciente: ")
            index = fila_pacientes.index(paciente_antigo)
            fila_pacientes[index] = paciente_novo
            print("Paciente atualizado com sucesso!")
        else:
            print("Paciente não encontrado na fila!")
    except Exception as e:
        print(f"Erro: {e}")
    print("Deseja atualizar outro paciente? SIM - NAO")
    resp = input()
    if resp == "SIM":
        atualizar_paciente()
    else:
        print("Voltando ao menu")


#Controle de Prontuarios funções

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
                    elif op in (1, 2, 3, 4):
                        print("Opção selecionada:", op)
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
                    elif op in (1, 2, 3, 4):
                        print("Opção selecionada:", op)
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
                    elif op in (1, 2, 3, 4):
                        print("Opção selecionada:", op)
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