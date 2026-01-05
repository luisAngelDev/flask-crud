from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time


URL = "https://opm-digemid.minsa.gob.pe/#/consulta-producto"


def obtener_medicamento(nombre_producto: str):





if __name__ == "__main__":
    data = obtener_medicamento("paracetamol")
    for d in data[:3]:
        print(d)