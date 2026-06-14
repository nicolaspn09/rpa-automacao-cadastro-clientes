import sys
import os

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(r"C:\rpa\Python")

import time
import requests
import subprocess
import datetime
import unicodedata
from Classes.GoogleSheets.GoogleSheets.GoogleSheets import GoogleSheets
from Classes.Postgres.Postgres.ConectaPG import ConectaPG
from Classes.ZimbraMailer.ZimbraMailer.Zimbra import ZimbraMailer
from Classes.AbreviaNome.AbreviaNome.AbreviaRazao import AbreviaRazao
from acessaIntranetCadastraFicha import AcessaIntranetCadastraFicha


def leitura_google_sheets():
    pass # Logica de negocio removida por seguranca corporativa



def consulta_cnpj_api(cnpj_cliente):
    pass # Logica de negocio removida por seguranca corporativa

    

def consulta_retorno_api(cnpj, email_retorno):
    pass # Logica de negocio removida por seguranca corporativa



def trata_dados_consulta_api(texto_api):
    pass # Logica de negocio removida por seguranca corporativa



def movimentar_backup(cnpj, canal, email_cliente, email_nfe, telefone, fone_comprador, boleto_digital, observacao, email_retorno, setor, situacao, data_atual):
    pass # Logica de negocio removida por seguranca corporativa



def excluir_linha_sheet(linha):
    pass # Logica de negocio removida por seguranca corporativa



def remover_diacriticos(texto):
    pass # Logica de negocio removida por seguranca corporativa



def limpa_complemento(complemento):
    pass # Logica de negocio removida por seguranca corporativa

    

def limpa_variaveis(razao_social, nome_fantasia, setor, email_cliente, email_nfe, telefone, fone_comprador, boleto_digital, observacao, email_retorno, cnpj, canal, cep, logradouro, bairro, cidade, uf, data_inicio_atividade, numero, email, fone, complemento, situacao):
    pass # Logica de negocio removida por seguranca corporativa



def consulta_dados_cliente_sheet():
    pass # Logica de negocio removida por seguranca corporativa

def kill_process(pid):
    pass # Logica de negocio removida por seguranca corporativa



if __name__ == "__main__":
    consulta_dados_cliente_sheet()