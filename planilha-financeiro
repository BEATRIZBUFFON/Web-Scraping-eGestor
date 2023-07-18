import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

# Define o escopo das permissões para acesso à API do Google Sheets:
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets", "https://www.googleapis.com/auth/drive"]

# carrega as credenciais da conta de serviço (Service Account) do Google Sheets a partir de um arquivo JSON
credentials = ServiceAccountCredentials.from_json_keyfile_name('/home/ramal630/Downloads/primeiro-projeto-393117-bb2be8d9a67e.json', scope)

# autoriza o cliente usando as credenciais
client = gspread.authorize(credentials)

# abre a planilha do Google Sheets com base no ID da planilha
spreadsheet = client.open_by_key('1z3DApiYXcqcOkY4vvdkh6wpekDhpmqXaDPECpiDUJRc')

# obtém uma determinada planilha da planilha aberta
sheet = spreadsheet.get_worksheet(0)

# obtém todos os valores da planilha como uma lista de listas
values = sheet.get_all_values()

# seleciona da segunda lista em diante
sublistas_selecionadas = values[2:]

# cria um df vazio
df = pd.DataFrame()

for sublista in sublistas_selecionadas: # percorre a lista
    if len(sublista) > 0: # verifica se a lista não ta vazia
        nome_coluna = sublista[0] # armazena a primeira posição da lista
        valores_coluna = sublista[1:] # posições subsequente são consideradas os valores da coluna e armazenadas na lista
        df[nome_coluna] = valores_coluna # add uma nova coluna com os dados anteriores

# criação de listas seleciona apenas o primeiro em diante dos elementos da lista
lista1 = sublistas_selecionadas[0]
lista2 = sublistas_selecionadas[1]
lista3 = sublistas_selecionadas[2]
lista4 = sublistas_selecionadas[3]
lista5 = sublistas_selecionadas[4]
lista6 = sublistas_selecionadas[5]
lista7 = sublistas_selecionadas[6]
lista8 = sublistas_selecionadas[7]
lista9 = sublistas_selecionadas[8]

# seleciona na lista apenas os elenetos dentro da lista de tal valor adiante
lista8 = lista8[9:14]
lista9 = lista9[1:3]

# cria uma lista com todas as listas para aplicar um tratamento geral
listas = [lista1, lista2, lista3, lista4, lista5, lista6, lista7]
listas_resultantes = []

for lista in listas: # para cada lista
    primeiros_elementos = lista[0:4] # selecionar apenas o elemento 0 ao 4
    segundos_elementos = lista[9:14]  # selecionar apenas o elemento 9 ao 14

    listas_resultantes.append(primeiros_elementos) # junta os elementos em uma lista
    listas_resultantes.append(segundos_elementos) # junta os elementos em uma lista

# criação do dataframe de retenção
# passa o nome da coluna e a lista respectiva
df_retencao = pd.DataFrame({'Solicitações': listas_resultantes[0],
                   'Cancelados': listas_resultantes[2],
                   'Revertidos': listas_resultantes[4],
                   'MRR Revertido': listas_resultantes[6],
                   'MRR Cancelado': listas_resultantes[8],
                   'MRR revertido HS': listas_resultantes[10],
                   '% de reversão': listas_resultantes[12]})
# selecionar apenas da primeira linha em diante no df
df_retencao = df_retencao.iloc[1:]
# definição dos nomes 
nomes = ['Mirela', 'Luiz', 'Gabriel']
# criação de um coluna com os respectivos nomes
df_retencao.insert(0, 'Nome', nomes)

colunas_monetarias = ['MRR Revertido', 'MRR Cancelado', 'MRR revertido HS']
for coluna in colunas_monetarias:
    df_retencao[coluna] = df_retencao[coluna].replace({'R\$': ''}, regex=True)

# Remover o símbolo "%" da coluna que contém valores percentuais
df_retencao['% de reversão'] = df_retencao['% de reversão'].replace({'%': ''}, regex=True)

# criação do dataframe do financeiro
df_financeiro = pd.DataFrame({'Renovaram': listas_resultantes[1],
                   'Não Renovaram': listas_resultantes[3],
                   'MRR Renovado': listas_resultantes[5],
                   'MRR renovado com Downsell': listas_resultantes[7],
                   'MRR não renovado': listas_resultantes[9],
                   'MRR certificados vendidos': listas_resultantes[11],
                   'Negociações pagas - Em MRR': listas_resultantes[13],
                   'Negociações não pagas - Em MRR': lista8})

# selecionar apenas da primeira linha em diante no df
df_financeiro = df_financeiro.iloc[1:]
# definição dos nomes
nomes = ['Sara', 'Alexia', 'Vitinho']
# criação de um coluna com os respectivos nomes
df_financeiro.insert(0, 'Nome', nomes)

'MRR Renovado',
colunas_monetarias2 = ['MRR renovado com Downsell', 'MRR não renovado',
                       'MRR certificados vendidos', 'Negociações pagas - Em MRR',
                       'Negociações não pagas - Em MRR']

for coluna in colunas_monetarias2:
    df_financeiro[coluna] = df_financeiro[coluna].replace({'R\$': ''}, regex=True)

#### importante:
print(df_financeiro)
print(df_retencao)
print(lista9)

