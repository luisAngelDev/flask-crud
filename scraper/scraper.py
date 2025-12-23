from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time


URL = "https://opm-digemid.minsa.gob.pe/#/consulta-producto"


def scraper_medicamento(nombre_producto: str):

    options = webdriver.ChromeOptions()
    options.add_argument("--headless")        # sin abrir navegador
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    resultados = []

    try:
       driver.get(URL)
       
       wait = WebDriverWait(driver, 20)
       
       input_busqueda = wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "input[type='text']")
                )
            )
       input_busqueda.clear()
       input_busqueda.send_keys(nombre_producto)
       input_busqueda.send_keys(Keys.ENTER)

       
    finally:
        driver.quit()

    return resultados