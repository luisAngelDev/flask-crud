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

        # Select: Departamento
        select_departamento = Select(
            wait.until(
                EC.presence_of_element_located(
                    (By.NAME, "codigoDepartamento")
                )
            )
        )
        select_departamento.select_by_value(departamento_value)

        # Select: distrito
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


        # Botón Buscar
        btn_buscar = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(text(),'Buscar')]")
            )
        )
        btn_buscar.click()
        

        # Esperar tabla resultados
        wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "table tbody tr")
            )
        )

        time.sleep(2)

        filas = driver.find_elements(By.CSS_SELECTOR, "table tbody tr")

        for fila in filas:
            columnas = fila.find_elements(By.TAG_NAME, "td")
            if len(columnas) < 6:
                continue

            resultados.append({
                "producto": columnas[0].text.strip(),
                "registro_sanitario": columnas[1].text.strip(),
                "titular": columnas[2].text.strip(),
                "forma_farmaceutica": columnas[3].text.strip(),
                "estado": columnas[4].text.strip(),
                "fecha_vencimiento": columnas[5].text.strip(),
            })

    finally:
        driver.quit()
    return resultados


if __name__ == "__main__":
    data = obtener_medicamento("paracetamol")
    for d in data[:3]:
        print(d)