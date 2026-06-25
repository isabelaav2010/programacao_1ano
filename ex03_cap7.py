#Crie um programa que permita:
  #Adicionar tarefas com descrição e status (pendente ou concluída).
  #Listar todas as tarefas.
  #Marcar uma tarefa como concluída.
  #Filtrar apenas as tarefas pendentes.
tarefas = [
    {"tarefa": "Cachorro", "descricao": "levar o cachorro para passear", "status": "pendente"},
    {"tarefa": "Jantar", "descricao": "fazer o jantar", "status": "concluída"}
]

while (True):
    opcao = int(input("[1] adicionar tarefa [2] Listar tarefa [3] Marcar como concluída: "))
    if opcao == 1:
        tarefa_adicionada = input("Crie uma tarefa:")
        descricao = input("Crie uma descrição para essa tarefa:")
        status = input("Essa tarefa foi concluída ou permanece pendente? [C - Concluída] ou [P - pendente]: ")

        tarefa = {'tarefa_adicionada': tarefa_adicionada, 'descricao': descricao, 'status': status}

        tarefas.append(tarefa)
    
    elif opcao == 2:
        for indice, tarefa in enumerate(tarefas):
            print(f"Lista de tarefas: {indice} - {tarefa['tarefa'], tarefa['descricao'], tarefa['status']}")

    elif opcao == 3:
        numero = int(input("Informe o número da tarefa: "))
        for indice, tarefa in enumerate(tarefas):
            if numero == indice:
                tarefas[numero]["status"] = "C"