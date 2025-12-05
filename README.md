# web con metricas y contadores



## Vista previa
![Vista previa]

## Características

- API REST construida con Flask
- Endpoint /scrape conectado a un módulo externo de scraping
- Endpoint /status para ver estado y salud del servicio
- Arquitectura modular (carpeta scraper/)
- Preparado para escalar a más endpoints
- Proyecto simple y entendible para practicar microservicios


## 🛠️ Tecnologías utilizadas

- Python 3.10+
- Flask
- Requests
- BeautifulSoup (bs4)
- Git + GitHub

## ⚙️ Instalación

Clonar el repositorio:

git clone https://github.com/tu_usuario/tu_repo.git
cd tu_repo


Crear y activar un entorno virtual:

python -m venv venv
source venv/bin/activate       # Linux/Mac
venv\Scripts\activate          # Windows


Instalar dependencias:

pip install -r requirements.txt


Ejecutar el proyecto:

python app.py


## 📂 Estructura del proyecto

```bash
mi_microservicio/
│
├── app.py
├── requirements.txt
│
├── scraper/
│   ├── __init__.py
│   └── scraper.py
│
└── data/
    └── ejemplo.json
```

## 👨‍💻 Autor

**Luis Ramos**  
[GitHub: @luisAngelDev](https://github.com/luisAngelDev) 

## 📄 Licencia
Este proyecto está bajo la Licencia MIT - consulta el archivo [LICENSE](./LICENSE) para más detalles.
