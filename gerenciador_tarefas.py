from print_colorido import print_color

tarefas = []

def adicionar_tarefa():
    while True:
        tarefa_nova = input("\nDigite a tarefa ou digite 'esc' para voltar: ").strip()

        if tarefa_nova.lower() == "esc":
            return

        if not tarefa_nova:
            print_color("red", "Tarefa inválida, tente novamente")
            continue

        tarefas.append(tarefa_nova)
        print_color("green", "Tarefa adicionada!")
        return

def visualizar_tarefas(modo="show"):
    if not tarefas:
        print_color("yellow", "\nNenhuma tarefa cadastrada.")
        return

    if modo == "remove":
        print("\nEscolha qual tarefa remover (número) ou digite 'esc' para voltar:")
    else:
        print("\nTarefas:")

    for index, tarefa in enumerate(tarefas, start=1):
        print(f"{index}. {tarefa}")

def remover_tarefa():
    if not tarefas:
        print_color("yellow", "Não há tarefas para remover.")
        return

    while True:
        visualizar_tarefas("remove")
        tarefa_remover = input(">> ").strip()

        if tarefa_remover.lower() == "esc":
            return

        # remover por número
        try:
            idx = int(tarefa_remover)
            if 1 <= idx <= len(tarefas):
                tarefas.pop(idx - 1)
                print_color("green", "\nTarefa removida!")
                return
            else:
                print_color("red", "Número fora da lista, tente novamente")
                continue
        except ValueError:
            print_color("red", "Entrada inválida, digite o número da tarefa ou 'esc'")

def menu():
    opcoes_menu = ["Adicionar tarefa", "Visualizar tarefas", "Remover tarefa", "Sair"]

    while True:
        print("\nMenu:")
        for i, item in enumerate(opcoes_menu, start=1):
            print(f"{i}. {item}")

        opcao = input("Escolha uma opção: ").strip()

        # aceita 'esc' como sair também (opcional)
        if opcao.lower() == "esc":
            return

        try:
            op = int(opcao)
        except ValueError:
            print_color("red", "Opção inválida, tente novamente")
            continue

        if op == 1:
            adicionar_tarefa()
        elif op == 2:
            visualizar_tarefas()
        elif op == 3:
            remover_tarefa()
        elif op == 4:
            return
        else:
            print_color("red", "Opção inválida, tente novamente")

if __name__ == "__main__":
    menu()