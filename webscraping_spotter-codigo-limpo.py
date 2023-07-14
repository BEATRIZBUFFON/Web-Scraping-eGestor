from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
import re

# inicializa o driver do Selenium
driver = webdriver.Chrome()

# abre a página do rdstation
driver.get('https://www.exactsales.com.br/prelogin.html')

# encontra a partir do isnpecionar onde está o email e add o email
email_input = driver.find_element(by='xpath', value='//*[@id="email"]')
email_input.send_keys('beatriz.buffon@zipline.com.br')

avancar_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '/html/body/div[1]/div/div[4]/div/button'))
)
avancar_button.click()

# encontra a partir do inspecionar o local da senha e add a senha
password_input = driver.find_element(by='xpath', value='//*[@id="Password"]')
password_input.send_keys('8JSF6O07')

# simula pressionamento da tecla enter para enviar as informações
password_input.send_keys(Keys.RETURN)


primeiro_botao = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="page-content-wrapper"]/div/div[1]/div/div[2]/div/div[1]/div[1]/div[2]'))
)
primeiro_botao.click()

# Aguarde o segundo botão ficar clicável
segundo_botao = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '/html/body/div[8]/div[3]/ul/li[3]'))
)
segundo_botao.click()


elements = []

# cria um for e loop range para cada elementosx é para juntar os itens em uma única lista:

for i in range(1, 35):
    xpath = '//*[@id="desempenhoPreVendedoresDataTable"]/tbody/tr[{}]'.format(i)
    element = WebDriverWait(driver, 30).until(
        EC.visibility_of_all_elements_located((By.XPATH, xpath))
    )
    elements.append(element)

# cria uma lista vazia
spotter = []
# cria um for e loop range para cada elementosx é para juntar os itens em uma única lista:

for i in range(1, 35):
    elements = locals()["elements" + str(i)]
    for element in elements:                                                                                                                                                                                                                                    
        numero = element.text
        spotter.append(numero)

# cria uma lista vazia
dados = []

for elemento in spotter:
    # seleciona somente os itens que estão entre '\n'
    partes = elemento.split('\n')
    print(partes)
    nome = partes[0]
    print(nome)
    numeros = []
    for part in partes[1:]:
        if part.isdigit():
            numeros.append(int(part))
    dados.append([nome] + numeros)

# criação das colunas
colunas = ['nome', 'cadastro', 'aplicacao_filtro2', 'agendamentos', 'feedbacks', 'vendas',
           'tempo_ligacao', 'reagendamentos', 'cancelamentos']

# passar para dataframe
df = pd.DataFrame(dados, columns=colunas)

# seleção de somente algumas colunas
df = df[['nome', 'agendamentos', 'vendas']]

# identifica com True e False se há duplicações
duplicadas = df.duplicated(subset='nome', keep=False)

# remove a primeira duplicação
df = df[~(duplicadas & duplicadas.shift())]

# cria uma função para verificar se no nome possui qualquer caractere nao alfanumerico já definido pela biblioteca re (^\W*)
# se ouver é para substituir com ''


def limpar_nome(nome):
    padrao = r'^\W*'
    return re.sub(padrao, '', nome)


# aplica a função na coluna nome
df['nome'] = df['nome'].apply(limpar_nome)

prefixos = ['Ca', 'Gu', 'Li', 'Na', 'Fer', 'Rod', 'Al', 'We']

# função para remover prefixos no ínicio do nome com a biblioteca re


def remover_prefixo(nome):
    padrao = r'^(' + '|'.join(prefixos) + r')\s'
    return re.sub(padrao, '', nome)


df['nome'] = df['nome'].apply(remover_prefixo)

df_spotter = df

print(df_spotter)
