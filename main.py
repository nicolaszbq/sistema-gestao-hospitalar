from collections import deque
fila_pacientes = deque()
import os

def mostrar_fila():
    pos = 1
    for paciente in fila_pacientes:
        print("Paciente: "+paciente + " ----- Posição: "+ pos)
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


while(True):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("======================")
    print("(1) - Controle de Atendimentos")
    print("(2) - Controle de Prontuarios")
    print("(3) - Controle de Pacientes")
    print("(4) - Controle de Especialidades")
    print("(5) - Sair")
    print("======================")
    r = input("Digite uma opção\n")
    if r == 1:
        while (True):
            os.system('cls' if os.name == 'nt' else 'clear')
            print("================================")
            print("(1) - Inserir paciente na fila")
            print("(2) - Remover paciente da fila")
            print("(3) - Atualizar paciente da fila")
            print("(4) - Consultar fila de pacientes")
            print("(5) - Voltar")
            print("================================")
    elif r == 2:
        while (True):
            os.system('cls' if os.name == 'nt' else 'clear')
            print("================================")
            print("(1) - Inserir prontuario")
            print("(2) - Remover prontuario")
            print("(3) - Atualizar prontuario")
            print("(4) - Consultar prontuarios")
            print("(5) - Voltar")
            print("================================")
    elif r == 3:
        while (True):
            os.system('cls' if os.name == 'nt' else 'clear')
            print("================================")
            print("(1) - Cadastrar Paciente")
            print("(2) - Remover Paciente")
            print("(3) - Atualizar Paciente")
            print("(4) - Consultar Pacientes")
            print("(5) - Voltar")
            print("================================")
    elif r == 4:
        while (True):
            os.system('cls' if os.name == 'nt' else 'clear')
            print("================================")
            print("(1) - Cadastrar Especialidade")
            print("(2) - Remover Especialidade")
            print("(3) - Atualizar Especialidade")
            print("(4) - Consultar Especialidades")
            print("(5) - Voltar")
            print("================================")

    elif r == 5:
        break
    else:
        print("Digite uma opção valida!")