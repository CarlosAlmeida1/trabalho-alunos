# Programa 2 - usando a função print()

from dataclasses import dataclass
from enum import Enum, auto

class CategoriaAluno(Enum):
    '''
    Representa as categorias de um aluno na universidade.
    '''
    GRADUACAO = auto()
    POS_GRADUACAO = auto()
    ENSINO_MEDIO_CAP = auto()
    INSTITUDO_DE_LINGUAS_ILG = auto()



@dataclass
class Aluno:
    """Representa os dados de um aluno em uma disciplina"""

    ra: int
    nome: str
    media: float
    frequencia: float
    categoria: CategoriaAluno

def escolher_categoria() -> CategoriaAluno:
    while True:
        print("1 - GRADUACAO")
        print("2 - POS_GRADUACAO")
        print("3 - ENSINO_MEDIO_CAP")
        print("4 - INSTITUDO_DE_LINGUAS_ILG")

        opcao = int(input("Escolha a categoria: "))

        if opcao == 1:
            return CategoriaAluno.GRADUACAO
        elif opcao == 2:
            return CategoriaAluno.POS_GRADUACAO
        elif opcao == 3:
            return CategoriaAluno.ENSINO_MEDIO_CAP
        elif opcao == 4:
            return CategoriaAluno.INSTITUDO_DE_LINGUAS_ILG

        print("Escolha inválida!")

def adicionar_aluno() -> Aluno:
    '''
    Insere um *aluno* em uma lista de alunos.
    '''
    ra = int(input("RA: "))
    nome = input('Nome: ')
    media: float = float(input('Media: '))
    frequencia: float = float(input('Frequencia: '))
    categoria = escolher_categoria()

    return Aluno(ra, nome, media, frequencia, categoria)

def inserir_aluno(alunos: list[Aluno], aluno: Aluno) -> None:
    """
    Insere um aluno na lista de *aluno* na lista de *alunos* por ordem alfabética.
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

    i = len(alunos) - 1

    while i > 0 and alunos[i - 1].nome > alunos[i].nome:
        alunos[i], alunos[i - 1] = alunos[i - 1], alunos[i]
        i -= 1


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

def avg_geral_categoria(alunos: list[Aluno], categoria: CategoriaAluno) -> float:
    """
    Calcula a média por *categoria* da lista de *alunos*.

    >>> alunos = [
    ...     Aluno(1, 'Joao', 8.0, 70.0, CategoriaAluno.GRADUACAO),
    ...     Aluno(2, 'Maria', 6.0, 80.0, CategoriaAluno.GRADUACAO),
    ...     Aluno(3, 'Jose', 9.0, 90.0, CategoriaAluno.POS_GRADUACAO),
    ... ]
    >>> avg_geral_categoria(alunos, CategoriaAluno.GRADUACAO)
    7.0

    >>> alunos = [
    ...     Aluno(1, 'Joao', 8.0, 70.0, CategoriaAluno.GRADUACAO),
    ...     Aluno(2, 'Maria', 6.0, 80.0, CategoriaAluno.GRADUACAO),
    ...     Aluno(3, 'Jose', 9.0, 90.0, CategoriaAluno.POS_GRADUACAO),
    ... ]
    >>> avg_geral_categoria(alunos, CategoriaAluno.POS_GRADUACAO)
    9.0

    """
    soma: float = 0.0
    quantidade: float = 0.0

    for aluno in alunos:
        if aluno.categoria == categoria:
            soma += aluno.media
            quantidade += 1

    if quantidade == 0:
        return 0

    return soma / quantidade

def alunos_acima_media_categoria(alunos : list[Aluno], categoria: CategoriaAluno) -> list[Aluno]:
    '''
    Retorna uma lista com os *alunos* da *categoria* informada
    que possuem média acima da média geral da categoria.

    >>> alunos = [
    ...     Aluno(1, 'Joao', 8.0, 70.0, CategoriaAluno.GRADUACAO),
    ...     Aluno(2, 'Maria', 6.0, 80.0, CategoriaAluno.GRADUACAO),
    ...     Aluno(3, 'Jose', 9.0, 90.0, CategoriaAluno.GRADUACAO)
    ... ]
    >>> resultado = alunos_acima_media_categoria(
    ...     alunos,
    ...     CategoriaAluno.GRADUACAO
    ... )
    >>> [aluno.nome for aluno in resultado]
    ['Joao', 'Jose']
    '''

    media_categoria = avg_geral_categoria(alunos, categoria)

    resultado: list[Aluno] = []

    for aluno in alunos:
        if aluno.categoria == categoria and aluno.media > media_categoria:
            resultado.append(aluno)

    return resultado


def main() -> None:
    alunos: list[Aluno] = []

    ## Menu
    sair: bool = False
    while not sair:
        print(f"1 - Inserir Aluno\n2 - Imprime Lista\n3 - Média por categoria\n4 - Alunos Acima da Média da Categoria\n5 - Sair")
        escolha = int(input("Escolha: "))
        if escolha == 1:
            # Entrada de dados - cria uma lista de alunos
            aluno = adicionar_aluno()
            inserir_aluno(alunos, aluno)
        elif escolha == 2:
            # processamento/saída
            imprime_lista(alunos)
        elif escolha == 3:
            # média dos alunos por categoria
            categoria = escolher_categoria()
            media = avg_geral_categoria(alunos, categoria)
            print(f"A média da categoria {categoria.name} é {media:.2f}")
        elif escolha == 4:
            categoria = escolher_categoria()
            resultado = alunos_acima_media_categoria(alunos, categoria)
            if len(resultado) == 0:
                print("Nenhum aluno encontrado")
            else:
                imprime_lista(resultado)
        elif escolha == 5:
            sair = True
        else:
            print("Escolha invalida!")

main()
