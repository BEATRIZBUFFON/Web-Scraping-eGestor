from selenium import webdriver 
from selenium.webdriver.common.keys import Keys #chaves
from selenium.webdriver.common.by import By #encontrar algo na página html
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC #ExpectedCondition
# aguardar a ocorrência em determinada condição antes de prosseguir com o código
import pandas as pd #manipulação e tratamento dos dados extraídos
import re #caracteres nao alfanumericos e prefixos

# inicializa o driver do Selenium
driver = webdriver.Chrome()

# abre a página do rdstation
driver.get('https://www.exactsales.com.br/prelogin.html')

# encontra a partir do isnpecionar onde está o email e add o email
email_input = driver.find_element(by='xpath', value='//*[@id="email"]')
email_input.send_keys('emailpessoal@empresa.com.br')

avancar_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, '/html/body/div[1]/div/div[4]/div/button'))
)
avancar_button.click()

# encontra a partir do inspecionar o local da senha e add a senha
password_input = driver.find_element(by='xpath', value='//*[@id="Password"]')
password_input.send_keys('suasenha')

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

elements1 = WebDriverWait(driver, 30).until(
    EC.presence_of_all_elements_located((By.XPATH, '//*[@id="desempenhoPreVendedoresDataTable"]/tbody/tr[1]'))
)
elements2 = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, '//*[@id="desempenhoPreVendedoresDataTable"]/tbody/tr[2]'))
)
elements3 = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, '//*[@id="desempenhoPreVendedoresDataTable"]/tbody/tr[3]'))
)
elements4 = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, '//*[@id="desempenhoPreVendedoresDataTable"]/tbody/tr[4]'))
)
elements5 = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, '//*[@id="desempenhoPreVendedoresDataTable"]/tbody/tr[5]'))
)
elements6 = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, '//*[@id="desempenhoPreVendedoresDataTable"]/tbody/tr[6]'))
)
elements7 = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, '//*[@id="desempenhoPreVendedoresDataTable"]/tbody/tr[7]'))
)
elements8 = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, '//*[@id="desempenhoPreVendedoresDataTable"]/tbody/tr[8]'))
)
elements9 = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, '//*[@id="desempenhoPreVendedoresDataTable"]/tbody/tr[9]'))
)
elements10 = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, '//*[@id="desempenhoPreVendedoresDataTable"]/tbody/tr[10]'))
)
elements11 = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, '//*[@id="desempenhoPreVendedoresDataTable"]/tbody/tr[11]'))
)
elements12 = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, '//*[@id="desempenhoPreVendedoresDataTable"]/tbody/tr[12]'))
)
elements13 = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, '//*[@id="desempenhoPreVendedoresDataTable"]/tbody/tr[13]'))
)
elements14 = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, '//*[@id="desempenhoPreVendedoresDataTable"]/tbody/tr[14]'))
)
elements15 = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, '//*[@id="desempenhoPreVendedoresDataTable"]/tbody/tr[15]'))
)
elements16 = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, '//*[@id="desempenhoPreVendedoresDataTable"]/tbody/tr[16]'))
)
elements17 = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, '//*[@id="desempenhoPreVendedoresDataTable"]/tbody/tr[17]'))
)
elements18 = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, '//*[@id="desempenhoPreVendedoresDataTable"]/tbody/tr[18]'))
)
elements19 = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, '//*[@id="desempenhoPreVendedoresDataTable"]/tbody/tr[19]'))
)
elements20 = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, '//*[@id="desempenhoPreVendedoresDataTable"]/tbody/tr[20]'))
)
elements21 = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, '//*[@id="desempenhoPreVendedoresDataTable"]/tbody/tr[21]'))
)
elements22 = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, '//*[@id="desempenhoPreVendedoresDataTable"]/tbody/tr[22]'))
)
elements23 = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, '//*[@id="desempenhoPreVendedoresDataTable"]/tbody/tr[23]'))
)
elements24 = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, '//*[@id="desempenhoPreVendedoresDataTable"]/tbody/tr[24]'))
)
elements25 = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, '//*[@id="desempenhoPreVendedoresDataTable"]/tbody/tr[25]'))
)
elements26 = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, '//*[@id="desempenhoPreVendedoresDataTable"]/tbody/tr[26]'))
)
elements27 = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, '//*[@id="desempenhoPreVendedoresDataTable"]/tbody/tr[27]'))
)
elements28 = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, '//*[@id="desempenhoPreVendedoresDataTable"]/tbody/tr[28]'))
)
elements29 = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, '//*[@id="desempenhoPreVendedoresDataTable"]/tbody/tr[29]'))
)
elements30 = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, '//*[@id="desempenhoPreVendedoresDataTable"]/tbody/tr[30]'))
)
elements31 = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, '//*[@id="desempenhoPreVendedoresDataTable"]/tbody/tr[31]'))
)
elements32 = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, '//*[@id="desempenhoPreVendedoresDataTable"]/tbody/tr[32]'))
)
elements33 = WebDriverWait(driver, 5).until(
    EC.presence_of_all_elements_located((By.XPATH, '//*[@id="desempenhoPreVendedoresDataTable"]/tbody/tr[33]'))
)
elements34 = WebDriverWait(driver, 5).until(
    EC.presence_of_all_elements_located((By.XPATH, '//*[@id="desempenhoPreVendedoresDataTable"]/tbody/tr[34]'))
)
elements35 = WebDriverWait(driver, 5).until(
    EC.presence_of_all_elements_located((By.XPATH, '//*[@id="desempenhoPreVendedoresDataTable"]/tbody/tr[35]'))
)
elements36 = WebDriverWait(driver, 5).until(
    EC.presence_of_all_elements_located((By.XPATH, '//*[@id="desempenhoPreVendedoresDataTable"]/tbody/tr[36]'))
)
elements37 = WebDriverWait(driver, 5).until(
    EC.presence_of_all_elements_located((By.XPATH, '//*[@id="desempenhoPreVendedoresDataTable"]/tbody/tr[37]'))
)
elements38 = WebDriverWait(driver, 5).until(
    EC.presence_of_all_elements_located((By.XPATH, '//*[@id="desempenhoPreVendedoresDataTable"]/tbody/tr[38]'))
)
elements39 = WebDriverWait(driver, 5).until(
    EC.presence_of_all_elements_located((By.XPATH, '//*[@id="desempenhoPreVendedoresDataTable"]/tbody/tr[39]'))
)
elements40 = WebDriverWait(driver, 5).until(
    EC.presence_of_all_elements_located((By.XPATH, '//*[@id="desempenhoPreVendedoresDataTable"]/tbody/tr[40]'))
)

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

# definição dos prefixos
prefixos = ['Ca', 'Gu', 'Li', 'Na', 'Fer', 'Rod', 'Al', 'We']

# função para remover prefixos no ínicio do nome com a biblioteca re
def remover_prefixo(nome):
    padrao = r'^(' + '|'.join(prefixos) + r')\s'
    return re.sub(padrao, '', nome)

df['nome'] = df['nome'].apply(remover_prefixo)
df_spotter = df
print(df_spotter)
