from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

service = Service()
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(service=service, options=options)

try:
    # 1) Abre a página
    driver.get("https://www.google.com")

    # 2) Espera o elemento existir e estar pronto para uso (clicável)
    wait = WebDriverWait(driver, 15)

    caixa_pesquisa = wait.until(
        EC.element_to_be_clickable((By.NAME, "q"))
    )

    # 3) Usa o elemento
    caixa_pesquisa.click()
    caixa_pesquisa.send_keys("Selenium WebDriverWait\n")

    # Exemplo: esperar o resultado aparecer (id do container principal)
    resultados = wait.until(
        EC.presence_of_element_located((By.ID, "search"))
    )

    print("Resultados carregados!")
finally:
    driver.quit()
