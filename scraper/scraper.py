from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time


URL = "https://opm-digemid.minsa.gob.pe/#/consulta-producto"


def obtener_medicamento(
        producto: str,
        departamento_value: str = "15",  # ejemplo: Lima
        provincia_value: str = None,
        distrito_value: str = None 
        ):
    
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")              # sin abrir navegador
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    resultados = []





if __name__ == "__main__":
    data = obtener_medicamento("paracetamol")
    for d in data[:3]:
        print(d)