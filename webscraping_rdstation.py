from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

# inicializa o driver do Selenium 
driver = webdriver.Chrome()

# abre a página do rdstation
driver.get('https://app.rdstation.com.br/dashboard')

# encontra a partir do isnpecionar onde está o email e add o email
email_input = driver.find_element(by='xpath', value='//*[@id="email"]')
email_input.send_keys('emailpessoal@empresa.com.br')

# encontra a partir do inspecionar o local da senha e add a senha
password_input = driver.find_element(by='xpath', value='//*[@id="password"]')
password_input.send_keys('suasenha')

# simula pressionamento da tecla enter para enviar as informações
password_input.send_keys(Keys.RETURN)

# esperar determinadas condições por um período de tempo -> 10 segundos
wait = WebDriverWait(driver, 10)


# aguarda encontrar elemento com classe CSS "data-block-value" esteja presente na página

# função WebDriverWait = esperar por determinadas condições antes de prosseguir com a execução do código
# condição presence_of_element_located = espera até que o elemento esteja presente no DOM (modelo de objeto de documento) da página.
# "data-block-value" encontrado, o objeto element conterá uma referência a esse elemento na página

elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "data-block-value"))
)

# cria uma lista vazia para armanezar 
rdstation = []
for element in elements:
    numero = element.text
    rdstation.append(numero)
    print(rdstation)

login_form = driver.find_element(By.XPATH, '//*[@id="rdsm-dashboard"]/div/div[1]/section[1]/div/div[3]/span')
novos_leads = login_form.text
print(novos_leads)

rdstation = [float(numero) for numero in rdstation]
novos_leads = novos_leads[:5].split()[:5]

dados = {
    'visitantes': (rdstation[0]),
    'leads': (rdstation[1]),
    'vendas': (rdstation[2]),
    'novos_leads': (novos_leads[0])
}
# cria o dataframe e printa ele
df = pd.DataFrame(dados, index=[0])
print(df)
