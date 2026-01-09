from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time


BASE_URL = "https://opm-digemid.minsa.gob.pe/#/consulta-producto"


def obtener_medicamento(
        producto: str,
        departamento_value: str = "15",  # ejemplo: Lima
        provincia_value: str = None,
        distrito_value: str = None 
        ):
    
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    resultados = []

    try:
        driver.get(BASE_URL)
        wait = WebDriverWait(driver, 20)

        input_producto = wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "ng-autocomplete input")
            )
        )

        input_producto.clear()
        input_producto.send_keys(producto)

        # esperar lista autocomplete
        opciones = wait.until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, ".ng-dropdown-panel .ng-option")
            )
        )

        # seleccionar primera opción
        opciones[0].click()

        # =============================
        # Select: Departamento
        # =============================
        select_departamento = Select(
            wait.until(
                EC.presence_of_element_located(
                    (By.NAME, "codigoDepartamento")
                )
            )
        )
        select_departamento.select_by_value(departamento_value)

        # Select: Departamento
        if distrito_value:
            wait.until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, "select[name='codigoDistrito'] option")
                )
            )
            select_distrito = Select(
                driver.find_element(By.NAME, "codigoDistrito")
            )
            select_distrito.select_by_value(distrito_value)




    finally:
        driver.quit()
    return resultados





if __name__ == "__main__":
    data = obtener_medicamento("paracetamol")
    for d in data[:3]:
        print(d)