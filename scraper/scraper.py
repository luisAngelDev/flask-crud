import requests
from bs4 import BeautifulSoup

def obtener_datos():
    """

    """

    url = "https://ejemplo.com"

    try:
        # 1. Hacer la petición
        response = requests.get(url, timeout=10)

        # 2. Validar estado
        response.raise_for_status()

    except requests.exceptions.RequestException as e:
        # Si falla la conexión
        return {
            "error": "No se pudo obtener la página",
            "detalles": str(e)
        }

    # 3. Parsear HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # 4. Extraer datos
    #    Aquí solo dejo un ejemplo genérico
    titulo = soup.title.text.strip() if soup.title else None

    # 5. Construir la respuesta JSON
    datos = {
        "titulo_pagina": titulo,
        "mensaje": "Scraping funcionando. Aquí irán los datos reales."
    }

    return datos



URL = "https://opm-digemid.minsa.gob.pe/#/consulta-producto"


def scrape_medicamento(nombre_producto: str):
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

       
    finally:
        driver.quit()

    return resultados