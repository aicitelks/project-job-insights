from functools import lru_cache
import csv


@lru_cache
# A FUNÇÃO SERÁ CHAMADA PELO TESTE QUE VAI PASSAR O PARÂMETRO: um arquivo .csv
def read(path):
    # ESSE ARQUIVO É ABERTO E É DADO O ALIAS csvfile
    with open(path) as csvfile:
        # A FUNÇÃO DictReader TRANSFORMA O CONTEÚDO EM UM DICIONÁRIO
        # JÁ COM CHAVE: VALOR, ONDE O CABEÇALHO SERÁ A CHAVE
        file_reader = csv.DictReader(csvfile)
        list_all_rows = []
        for row in file_reader:
            # ADICIONO A MINHA VARIÁVEL CADA UMA DAS LINHAS DA "TABELA"
            list_all_rows.append(row)
    return list_all_rows
