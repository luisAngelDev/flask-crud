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
    #options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    resultados = []

    driver.get(BASE_URL)
    wait = WebDriverWait(driver, 20)

    try:

        btn_cerrar = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((
            By.XPATH,
            "//button[contains(text(),'Cerrar')]"
            ))
        )
        btn_cerrar.click()
        print("MODAL CERRADO")



        # esperar que Angular termine de renderizar
        wait.until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        print("PASE EL WAIT UNTIL")

        #input del producto
        input_producto = wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "ng-autocomplete input[type='text']")
            )
        )

        driver.execute_script("arguments[0].scrollIntoView(true);", input_producto)
        time.sleep(1)
        driver.execute_script("arguments[0].focus();", input_producto)

        print("INPUT PRODUCTO ENCONTRADO")

        input_producto.clear()
        for c in producto:
            input_producto.send_keys(c)
            time.sleep(0.05)

        print("PASE EL ENVIO DE PRODUCTO AL AUTOCOMPLETE")

        # esperar opciones
        """ opciones = wait.until(
            EC.visibility_of_all_elements_located(
                (By.CSS_SELECTOR, ".ng-dropdown-panel .ng-option")
            )
        )

        driver.execute_script("arguments[0].click();", opciones[0]) """
        print("PRODUCTO SELECCIONADO")



        # SELECT DEPARTAMENTO
        # -----------------------------
        select_departamento = Select(
            wait.until(
                EC.element_to_be_clickable(
                    (By.NAME, "codigoDepartamento")
                )
            )
        )

        # por value (recomendado)
        select_departamento.select_by_value(departamento_value)
        print(f"DEPARTAMENTO SELECCIONADO: {departamento_value}")




        # ESPERAR PROVINCIAS
        # -----------------------------
        wait.until(
            lambda d: len(
                Select(d.find_element(By.NAME, "codigoProvincia")).options
            ) > 1
        )

        select_provincia = Select(
            driver.find_element(By.NAME, "codigoProvincia")
        )

        # 01 es provincia Lima
        provincia_value = provincia_value or "01"
        select_provincia.select_by_value(provincia_value)
        print(f"PROVINCIA SELECCIONADA: {provincia_value}")


        # -----------------------------
        # ESPERAR DISTRITOS
        # -----------------------------
        wait.until(
            lambda d: len(
                Select(d.find_element(By.NAME, "codigoDistrito")).options
            ) > 1
        )

        select_distrito = Select(
            driver.find_element(By.NAME, "codigoDistrito")
        )

        # seeleccionar por texto visible
        distrito_texto = "LIMA"   # Cercado de Lima

        for option in select_distrito.options:
            if distrito_texto in option.text.upper():
                option.click()
                print(f"DISTRITO SELECCIONADO: {option.text}")
                break
        else:
            raise Exception("Distrito no encontrado")


         # Botón Buscar
        btn_buscar = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[.//text()[contains(.,'Buscar')]]")
            )
        )

        driver.execute_script("arguments[0].scrollIntoView(true);", btn_buscar)
        time.sleep(0.5)
        driver.execute_script("arguments[0].click();", btn_buscar)

        print("CLICK EN BOTÓN BUSCAR")


        print("ESPERANDO FILAS...")

        
        # DEBUG: imprimir HTML actual
        html = driver.page_source
        print("LONGITUD HTML:", len(html))

        # buscar si existe la palabra table
        print("EXISTE <table> ?", "<table" in html)

        # buscar si existe tbody
        print("EXISTE <tbody> ?", "<tbody" in html)

        # buscar si existe tr
        print("EXISTE <tr> ?", "<tr" in html)

        wait.until(
            lambda d: d.execute_script("return document.readyState") == "complete"
        )
        wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "div.table-responsive")
            )
        )

        """ filas = driver.find_elements(By.CSS_SELECTOR, "div.table-responsive table tbody tr")
        print("FILAS:", len(filas))

        print("TABLA YA TIENE RESULTADOS")

        # EXTRAER FILAS
        filas = driver.find_elements(By.CSS_SELECTOR, "table tbody tr")

        resultados = [] """

        # for fila in filas:
        #     columnas = fila.find_elements(By.TAG_NAME, "td")

        #     if len(columnas) < 7:
        #         continue

        #     resultados.append({
        #         "producto": columnas[0].text.strip(),
        #         "registro": columnas[1].text.strip(),
        #         "titular": columnas[2].text.strip(),
        #         "forma": columnas[3].text.strip(),
        #         "estado": columnas[4].text.strip(),
        #         "vencimiento": columnas[5].text.strip(),
        #         "fabricante": columnas[6].text.strip(),
        #     })

        # print("RESULTADOS EXTRAÍDOS:", len(resultados))

        # wait.until(
        #     EC.any_of(
        #         lambda d: len(d.find_elements(By.CSS_SELECTOR, "table tbody tr")) > 0,
        #         EC.presence_of_element_located(
        #             (By.XPATH, "//*[contains(text(),'No se encontraron')]")
        #         )
        #     )
        # )
                
        
        
    finally:
        driver.quit()
    return resultados


if __name__ == "__main__":
    data = obtener_medicamento("PARACETAMOL 1000mg Tableta - Capsula", "15","01","LIMA")
    for d in data[:3]:
        print(d)