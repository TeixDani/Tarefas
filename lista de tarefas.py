class Lista:
    def __init__(self,nomeT):
        self.nomeT = nomeT


    def __str__(self):
        return f"{self.nomeT}"
tarefas = []

def menu():
    print(f"╭────────────────────────.★..─╮"f"\n│         Menu De Tarefas       \n│ \n│ 1 - Cadastrar Tarefa\n│ 2 - Listar Tarefas\n│ 3 - Remover Tarefa/Concluir \n│ 0 - Sair"f"\n╰─..★.────────────────────────╯")

def cadastrar():
    nomeT      = input("*Cite a Tarefa: "            )
    tarefa    = Lista(nomeT)
    tarefas.append(tarefa)
    print ("Tarefa cadastrada com sucesso!!")



def listar():
    if not tarefas:
        print("Nenhuma Tarefa Cadastrada")
        return
    print("\nLista de Tarefas: ")
    for tarefa in tarefas:
        print(tarefa)

def remover():
    psq = input("Informe a Tarefa Para Remover/Concluir: ")
    for tarefa in tarefas:
        if tarefa.nomeT == psq:
           tarefas.remove(tarefa)
           print("Tarefa Removida ou Concluida")
        return
    print ("Tarefa não encontrada!")





while True:
        menu()
        print("╭┈──────────────────┈╮")
        opcao = input("│Escolha a opção: ")
        print("╰┈──────────────────┈╯")


        if   opcao == "1":
             cadastrar()
        elif opcao == "2":
             listar()
        elif opcao == "3":
            remover()
        elif opcao == "0":
            print("Encerrando...")
            break

