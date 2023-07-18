from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import re


# inicializa o driver do Selenium 
driver = webdriver.Chrome()

# abre a página do rdstation
driver.get('http://zipline.fattura.com.br/corrida/')

user_input = driver.find_element(by='xpath', value='//*[@id="loginfat"]')
user_input.send_keys('beatrizbuffon')

# encontra a partir do inspecionar o local da senha e add a senha
password_input = driver.find_element(by='xpath', value='//*[@id="senhafat"]')
password_input.send_keys('Pizza2121@')


# encontra o botão de 'enter' para acessar e clica
avancar_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="botaoentrar"]'))
)
avancar_button.click()

# espera o redirecionamento e obtém a URL atual
WebDriverWait(driver, 10).until(EC.url_changes(driver.current_url))
current_url = driver.current_url

# verifica se a URL atual é a página inicial
if current_url == 'https://zipline.fattura.com.br/inicio/':
    # Redireciona manualmente para a URL desejada
    driver.get('http://zipline.fattura.com.br/corrida/')  # Insira a URL desejada aqui

avancar_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/a'))
)
avancar_button.click()


# percorre elementos que possuem o XPATH passado e encontra os alementos
elements = WebDriverWait(driver, 20).until(
    EC.presence_of_all_elements_located((By.XPATH, '/html/body/table[2]/tbody'))
)

##################3 extração dos dados ######################
# cria uma lista vazia
fattura = []
# para cada elemento que percorre elements ele add na lista vazia com o 'append'
for element in elements:
    numero = element.text
    fattura.append(numero)
    print(fattura)

linhas = []
for elemento in fattura: # itera em cada elemento em fattura (lista)
    linhas.extend(elemento.split('\n')) # divide o elemento em várias linhas a ṕartir do caractere \n 
    # que acontece a quebra de linha
    # linhas = lista final com todas as linhas extraídas

# percorre as linhas usando o intervalo definido em 7 pois é a quantidade de variáveis que possuimos para observar em 
# cada funcionário
linhas2 = [linhas[i:i+7] for i in range(0, len(linhas), 7)]

# linhas[i:i+7] = sublista com elementos da posição i até a i + 7 da lista
# determinação do intervalo: range(0, len(linhas), 7)
# em que i começa em 0, aumenta em 7 a cada iteração e para quando atingir o comprimento total da lista pelo 'len'

# definição das colunas do dataframe
colunas = ['nome', 'crescimento', 'saida_nos_6meses', 'saida_apos_6meses', 'total_potencia_receita', 'planos', 'pontuacao']
# criação do dataframe passando como paramêtro dentro as colunas
df = pd.DataFrame(columns=colunas)


for lista in linhas2: # para cada lista da lista2 definida anteriormente
    if len(lista) == len(colunas): # verfifica se o número de elementos da lista é o mesmo da coluna
        df.loc[len(df)] = lista # se for então ele adiciona essa lista ao dataframe 
        # loc = acessa a última linha do df e adiciona a 'lista' como uma nova linha
    else: # se a verificação de elementos na lista e colunas for diferente
        df.loc[len(df)] = [''] * len(colunas) # então preenche com valores vazios 

print(df) # visualiza o df

#################### tratamento do df #########################

# extrair informações após os dois pontos (:) e o caractere (❦)
def extrair_info(coluna):
    return coluna.str.extract(r':\s*(.*?)\s*❦')

colunas_extrair = ['crescimento', 'saida_nos_6meses', 'saida_apos_6meses']
for coluna in colunas_extrair:
    df[coluna] = extrair_info(df[coluna])

# extrair informações após os dois pontos (:) e o caractere (❦)
def extrair_info(coluna):
    return coluna.str.extract(r':\s*(.*)')

colunas_extrair = ['planos', 'pontuacao', 'total_potencia_receita']
for coluna in colunas_extrair:
    df[coluna] = extrair_info(df[coluna])


# remover numeros e caracteres da coluna nome 
colunas_nome = ['nome']

def limpar_numeros_caracteres(df, colunas):
    for coluna in colunas:
        # r'\d' = qualquer dígito numérico.
        df[coluna] = df[coluna].str.replace(r'\d', '', regex=True)
        # r'\W' = qualquer caractere não alfanumérico.
        df[coluna] = df[coluna].str.replace(r'\W', '', regex=True)

limpar_numeros_caracteres(df, colunas_nome)

# separando os nomes
def split_nome(df, coluna):
    df[coluna] = df[coluna].str.replace(r'([a-z])([A-Z])', r'\1 \2', regex=True)

coluna_nome = 'nome'
split_nome(df, coluna_nome)

# ################### setores válidos ####################

# função de setor, em que está cada pessoa e seu respectivo setor
def atribuir_setor(row):
    if row ['nome'] in ['Marcia BL', 'Vanessa Ortiz', 'Gian Borba', 'Felipe Trindade Fiorini'
                        'Giovanni Zanela', 'Camila Wrasse', 'Eduarda Fragoso', 'Ana Ramos',
                        'Renata', 'Frederico Vargas', 'Gui Netto', 'Naiane Bock', 'Andressa Ely', 'Gabriele Motta']:
        return 'Trials'
    elif row['nome'] in ['Lilian Palmeira', 'Alisson']:
        return 'NfeMais'
    elif row['nome'] in ['Wellington Reis', 'Jennifer Dallanora', 'Matheus Mesquita']:
        return 'Canais IB'
    elif row['nome'] in ['Rodrigo Santos', 'Patrícia Lima', 'Kello Ethur', 'Beatriz Saueressig Kowas',
                         'Patricia Melo', 'Alan Alves', 'Fernando P']:
         return 'Canais OB'
    elif row['nome'] in ['Pedro Murilo Leal da Silva', 'Ana Beatriz', 'Yuri Martins', 'Priscila Trindade',
                         'Suelen Lopes', 'Aline Garcia', 'Fernando P']:
         return 'Farmers'
    elif row['nome'] in ['Luis Henrique Barcellos', 'Sara Palmeira', 'Luiz Otavio', 'Mirela Magnago',
                         'Alexia Branquier', 'Gabriel Martins']:
         return 'Financeiro'
    elif row['nome'] in ['Vinicius LA', 'Deivison AE', 'Éverton MG', 'Joseph Kaus'
                        'Zipline', 'Anderson dos Santos Lima', 'Jeferson Kasper', 'Raíssa Tolfo',
                        'Pedro Escobar', 'Victor Alves', 'Priscila Soldera', 'Nicolas Santos', 'Ricardo Golzer',
                        'Gabriele Motta', 'Juliana', 'Kayane Crestani', 'Juliane Rocha', 'Fernanda Toebe'
                        'Victor Souza', 'Eduarda', 'Jefferson Veiga Pinho de Oliveira', 'João Ribeiro',
                        'Dionathan Dalton da Silva Martins', 'Beatriz Buffon', 'Alan Carvalho', 'Kelli Scotti',
                        'Douglas Teixeira Fabricio', 'Rodolfo Wagner Lucho', 'Paola Bortoloto', 'Adilson Lopes', 'Louise Sobrosa']:
         return 'Administrativo'
df['setor'] = df.apply(atribuir_setor, axis=1) #atribui a função na coluna setor no dataframe

setores_validos = ['Trials', 'NfeMais', 'Canais IB', 'Canais OB', 'Farmers', 'Financeiro'] #seleciona os setores válidos
df = df[df['setor'].isin(setores_validos)]  #filtra somente os valores definidos na lista anterior

print(df)
