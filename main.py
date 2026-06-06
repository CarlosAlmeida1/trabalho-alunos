# Programa 2 - usando a função print()

from dataclasses import dataclass
from enum import Enum, auto

class CategoriaAluno(Enum):
    '''
    Representa as categorias de um aluno na universidade.
    '''
    GRADUACAO = auto(),
    POS_GRADUACAO = auto(),
    ENSINO_MEDIO_CAP = auto(),
    INSTITUDO_DE_LINGUAS_ILG = auto()



@dataclass
class Aluno:
    """Representa os dados de um aluno em uma disciplina"""

    ra: int
    nome: str
    media: float
    frequencia: float
    categoria: CategoriaAluno

def adicionar_aluno() -> Aluno:
    '''
    Insere um *aluno* em uma lista de alunos.
    '''
    ra = int(input("RA: "))
    nome = input('Nome: ')
    media: float = float(input('Media: '))
    frequencia: float = float(input('Frequencia: '))

    ## categoria
    valido = False
    while not valido:
        print(f"1 - GRADUACAO\n2 - POS_GRADUACAO\n3 - ENSINO_MEDIO_CAP\n4 - INSTITUDO_DE_LINGUAS_ILG")
        opcao = int((input("Escolha a opção de categoria:")))

        if opcao == 1:
            categoria = CategoriaAluno.GRADUACAO
            valido = True
        elif opcao == 2:
            categoria = CategoriaAluno.POS_GRADUACAO
            valido = True
        elif opcao == 3:
            categoria = CategoriaAluno.ENSINO_MEDIO_CAP
            valido = True
        elif opcao == 4:
            categoria = CategoriaAluno.INSTITUDO_DE_LINGUAS_ILG
            valido = True
        else:
            print("Escolha invalida!")


    return Aluno(ra, nome, media, frequencia, categoria)

def inserir_aluno(alunos: list[Aluno], aluno: Aluno) -> None:
    """
    Insere um aluno na lista de alunos.
    Ra: 100
    Nome: Joao
    Média: 8.0
    Frequencia: 70.0
    Categoria: INSTITUDO_DE_LINGUAS_ILG
    **
    Ra: 101
    Nome: José
    Média: 5.0
    Frequencia: 50.0
    Categoria: GRADUACAO
    **
    """
    for a in alunos:
        if a.ra == aluno.ra:
            print("Aluno já está cadastrado")
            return

    alunos.append(aluno)


def imprime_lista(alunos: list[Aluno]) -> None:
    """
    Imprime os dados dos alunos.

    >>> imprime_lista([
    ...     Aluno(1, 'Joao', 8.0, 70.0, CategoriaAluno.INSTITUDO_DE_LINGUAS_ILG),
    ...     Aluno(2, 'Jose', 5.0, 50.0, CategoriaAluno.GRADUACAO)
    ... ])
    RA: 1
    Nome: Joao
    Média: 8.0
    Frequencia: 70.0
    Categoria: INSTITUDO_DE_LINGUAS_ILG
    **
    RA: 2
    Nome: Jose
    Média: 5.0
    Frequencia: 50.0
    Categoria: GRADUACAO
    **
    """
    for aluno in alunos:
        print(f'RA: {aluno.ra}')
        print(f'Nome: {aluno.nome}')
        print(f'Média: {aluno.media}')
        print(f'Frequencia: {aluno.frequencia}')
        print(f'Categoria: {aluno.categoria.name}')
        print('**')

def main() -> None:
    alunos: list[Aluno] = []

    ## Menu
    sair: bool = False
    while not sair:
        print(f"1 - Inserir Aluno\n2 - Imprime Lista\n3 - Sair")
        escolha = int(input("Escolha: "))
        if escolha == 1:
            # Entrada de dados - cria uma lista de alunos
            aluno = adicionar_aluno()
            inserir_aluno(alunos, aluno)
        elif escolha == 2:
            # processamento/saída
            imprime_lista(alunos)
        elif escolha == 3:
            sair = True
        else:
            print("Escolha invalida!")

main()
