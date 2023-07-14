from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

# inicializa o driver do Selenium 
driver = webdriver.Chrome()

# abre a página do rdstation
driver.get('http://blaster.zipline.com.br/implementacoes/')

# encontra a partir do isnpecionar onde está o email e add o email
email_input = driver.find_element(by='xpath', value='//*[@id="login_user"]')
email_input.send_keys('BeatrizBuffon')

# encontra a partir do inspecionar o local da senha e add a senha
password_input = driver.find_element(by='xpath', value='//*[@id="login_pass"]')
password_input.send_keys('Pizza2121@')

# encontra o botão de 'enter' para acessar e clica
avancar_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="login_btnIn"]'))
)
avancar_button.click()


# percorre elementos que possuem o XPATH passado e encontra os alementos
elements = WebDriverWait(driver, 20).until(
    EC.presence_of_all_elements_located((By.XPATH, '//*[@id="divLista"]/table/tfoot/tr'))
)

# cria uma lista vazia
implementacao = []
# para cada elemento que percorre elements ele add na lista vazia com o 'append'
for element in elements:
    numero = element.text
    implementacao.append(numero)
    print(implementacao)

# o split vai separar o conteúdo da lista e selecionar somente a partir do 3º item da lista
numeros = implementacao[0].split()[3:]

# criação de um dicionário com as colunas especefícas para cada item da lista 'numeros'
dados = {
    'concluidas': int(numeros[0]),
    'reagendadas': int(numeros[1]),
    'nao_quer': int(numeros[2]),
    'no_show': int(numeros[3]),
    'em_andamento': int(numeros[4]),
    'cliente_contatara': int(numeros[5]),
    'concluidas_agrupado': int(numeros[6])
}
 
# cria o dataframe
df = pd.DataFrame(dados, index=[0])

print(df)