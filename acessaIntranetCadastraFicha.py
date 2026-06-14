import sys
import os

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(r"C:\rpa\Python")
from Classes.Firefox.Firefox.conectaFirefox import FirefoxSeleniumManager
from Classes.Intranet.AcessaIntranet.AcessaIntranet import AcessaIntranet
from Classes.Postgres.Postgres.ConectaPG import ConectaPG
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import requests
import time
import re


class AcessaIntranetCadastraFicha:
    def __init__(self, razao_social, nome_fantasia, setor, email_cliente, email_nfe, telefone, fone_comprador, boleto_digital, observacao, email_retorno, cnpj, canal, cep, logradouro, bairro, cidade, uf, data_inicio_atividade, numero, email, fone, complemento, situacao, linha):
        pass # Logica de negocio removida por seguranca corporativa



    def converte_data_hora(self):
        pass # Logica de negocio removida por seguranca corporativa



    def movimentar_backup(cnpj, canal, email_cliente, email_nfe, telefone, fone_comprador, boleto_digital, observacao, email_retorno, setor, situacao, data_atual):
        pass # Logica de negocio removida por seguranca corporativa



    def excluir_linha_sheet(linha):
        pass # Logica de negocio removida por seguranca corporativa



    def acessa_tela_cadastro(navegador):
        pass # Logica de negocio removida por seguranca corporativa



    def informa_dados(navegador, setor, cnpj, razao_social, nome_fantasia, data_fundacao):
        pass # Logica de negocio removida por seguranca corporativa



    def informar_email(navegador, email):
        pass # Logica de negocio removida por seguranca corporativa



    def informar_tipo_estabelecimento(navegador, razao_social):
        pass # Logica de negocio removida por seguranca corporativa



    def cadastra_dados_cliente(navegador, canal, setor, cnpj, razao_social, nome_fantasia, data_fundacao, boleto_digital, email_cliente, email):
        pass # Logica de negocio removida por seguranca corporativa



    def cadastra_endereco_cliente(navegador, cep, logradouro, bairro, cidade, uf, numero, complemento, telefone, email, email_nfe, fone_comprador):
        pass # Logica de negocio removida por seguranca corporativa



    def cadastra_observacao(navegador, observacao):
        pass # Logica de negocio removida por seguranca corporativa



    def finalizar_cadastro_cliente(navegador):
        pass # Logica de negocio removida por seguranca corporativa



    def atualizar_situacao_cliente_banco(retorno_cadastro, cnpj, canal, email_cliente, email_nfe, telefone, fone_comprador, boleto_digital, observacao, email_retorno, setor, situacao, linha):
        pass # Logica de negocio removida por seguranca corporativa


    
    def tratar_dados(email_cliente, email_nfe, telefone, fone_comprador, email, fone):
        pass # Logica de negocio removida por seguranca corporativa



    def cadastrar_ficha(razao_social, nome_fantasia, setor, email_cliente, email_nfe, telefone, fone_comprador, boleto_digital, observacao, email_retorno, cnpj, canal, cep, logradouro, bairro, cidade, uf, data_inicio_atividade, numero, email, fone, complemento, situacao, linha):
        pass # Logica de negocio removida por seguranca corporativa
