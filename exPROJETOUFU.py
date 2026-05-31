from time import sleep
import json
from enum import Enum

# Enumeração dos tipos de ativos

class TipoAtivo(Enum):
    SERVIDOR = 1
    NOTEBOOK = 2
    ROTEADOR = 3
    APLICACAO_WEB = 4

def mostrar_tipo(codigo):
    if codigo == TipoAtivo.SERVIDOR.value:
        return 'Servidor'
    elif codigo == TipoAtivo.NOTEBOOK.value:
        return 'Notebook'
    elif codigo == TipoAtivo.ROTEADOR.value:
        return 'Roteador'
    elif codigo == TipoAtivo.APLICACAO_WEB.value:
        return 'Aplicação Web'
    else:
        return 'Tipo desconhecido'

# Salva os dados dos ativos em arquivo JSON

def salvar_dados():
    with open('ativos.json', 'w', encoding='utf-8') as arquivo:
        json.dump(ativos, arquivo, ensure_ascii=False, indent=4)

def carregar_dados():
    try:
        with open('ativos.json', 'r', encoding='utf-8') as arquivo:
            dados = json.load(arquivo)

            ativos_convertidos = {}

            for id_ativo, informacoes in dados.items():
                ativos_convertidos[int(id_ativo)] = informacoes

            return ativos_convertidos

    except FileNotFoundError:
        return {}

ativos = carregar_dados()


escolha = 0

while escolha != 8:
    print('-' * 20)
    print('INVENTÁRIO DE TI')
    print('-' * 20)

    print('''O que deseja fazer:
          [1] Cadastrar ativo
          [2] Buscar ativo
          [3] Atualizar ativo
          [4] Remover ativo
          [5] Adicionar vulnerabilidades
          [6] Ver vulnerabilidades
          [7] Listar ativos
          [8] Encerrar programa''')
    try:
        escolha = int(input('Por favor, informe aqui a sua escolha: '))
    except:
        print('Opção inválida! Digite apenas números.')
        sleep(2)
        continue


    if escolha == 1:

        try:
            id_ativo = int(input('Informe o ID do ativo: '))
        except:
            print('ID inválido! Digite apenas números.')
            sleep(2)
            continue

        nome = input('Nome do ativo: ')
        responsavel = input('Responsável: ')
        setor = input('Setor: ')

        print('''
        [1] Servidor
        [2] Notebook
        [3] Roteador
        [4] Aplicação Web
        ''')

        tipo = int(input('Escolha o tipo do ativo: '))

        ativos[id_ativo] = {
            'nome': nome,
            'responsável': responsavel,
            'setor': setor,
            'tipo': tipo,
            'vulnerabilidades': []
        }

        salvar_dados()

        print('Ativo cadastrado com sucesso!')

    elif escolha == 2:

        try:
            tipo_busca = int(input('''

    [1] Buscar por ID
    [2] Buscar por nome

    Escolha: '''))
        except:
            print('Opção inválida! Digite apenas números.')
            sleep(2)
            continue

        if tipo_busca == 1:

            try:
                id_busca = int(input('Informe o ID do ativo: '))
            except:
                print('ID inválido! Digite apenas números.')
                sleep(2)
                continue

            if id_busca in ativos:
                print('Nome:', ativos[id_busca]['nome'])
                print('Responsável:', ativos[id_busca]['responsável'])
                print('Setor:', ativos[id_busca]['setor'])

            else:
                print('Ativo não encontrado!')

        elif tipo_busca == 2:

            nome_busca = input('Informe o nome do ativo: ')
            encontrado = False

            for id_ativo, dados in ativos.items():

                if dados['nome'] == nome_busca:
                    print('ID:', id_ativo)
                    print('Nome:', dados['nome'])
                    print('Responsável:', dados['responsável'])
                    print('Setor:', dados['setor'])

                    encontrado = True

            if not encontrado:
                print('Ativo não encontrado!')

        else:
            print('Opção de busca inválida!')



    elif escolha == 3:

        try:

            id_update = int(input('Informe o ID do ativo: '))
        except:
            print('ID inválido! Informe apenas números.')
            sleep(2)
            continue

        if id_update in ativos:

            novo_nome = input('Novo nome: ')
            novo_responsavel = input('Novo Responsável: ')
            novo_setor = input('Novo Setor: ')

            ativos[id_update]['nome'] = novo_nome
            ativos[id_update]['responsável'] = novo_responsavel
            ativos[id_update]['setor'] = novo_setor

            salvar_dados()

            print('Ativo atualizado com sucesso!')

        else:
            print('Ativo não encontrado!')

    elif escolha == 4:

        try:

            id_delete = int(input('Informe o ID do ativo: '))
        except:
            print('ID inválido! Informe apenas números.')
            sleep(2)
            continue

        if id_delete in ativos:

            del ativos[id_delete]

            salvar_dados()

            print('Ativo removido com sucesso!')

        else:
            print('Ativo não encontrado!')

    elif escolha == 5:

        try:

            id_vulnerabilidade = int(input('Informe o ID do ativo: '))
        except:
            print('ID inválido! Informe apenas números.')
            sleep(2)
            continue

        if id_vulnerabilidade in ativos:

            descricao = input('Descrição da vulnerabilidade: ')
            categoria = input('Categoria/Tipo: ')
            severidade = input('Severidade: ')
            status = input('Status de tratamento: ')

            vulnerabilidade = {
                'descricao': descricao,
                'categoria': categoria,
                'severidade': severidade,
                'status': status
            }

            ativos[id_vulnerabilidade]['vulnerabilidades'].append(vulnerabilidade)

            salvar_dados()

            print('Vulnerabilidade adicionada com sucesso!')

        else:

            print('Ativo inexistente!')

    elif escolha == 6:

        try:

            id_vulnerabilidade = int(input('Informe o ID do ativo: '))
        except:
            print('ID inválido! Informe apenas números.')
            sleep(2)
            continue

        if id_vulnerabilidade in ativos:

            vulnerabilidades = ativos[id_vulnerabilidade]['vulnerabilidades']

            if len(vulnerabilidades) == 0:

                print('Este ativo não possui vulnerabilidades registradas!')

            else:

                for vulnerabilidade in vulnerabilidades:

                    print('\nDescrição:', vulnerabilidade['descricao'])
                    print('Categoria:', vulnerabilidade['categoria'])
                    print('Severidade:', vulnerabilidade['severidade'])
                    print('Status:', vulnerabilidade['status'])

        else:

            print('Ativo inexistente!')


    elif escolha == 7:

        for id_ativo, dados in ativos.items():

            print('\nID:', id_ativo)
            print('Nome:', dados['nome'])
            print('Responsável:', dados['responsável'])
            print('Setor:', dados['setor'])
            print('Tipo:', mostrar_tipo(dados.get('tipo', 0)))

    elif escolha == 8:

        print('Fim do programa. Volte sempre!')