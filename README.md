# API REST con Flask y consulta con sraping

Proyecto construido con Flask que implementa una API diseñada para ejecutar tareas de scraping y devolver los datos procesados en formato JSON. 


## Vista previa
![Vista previa]

## Características

- API REST construida con Flask
- Endpoint /scrape conectado a un módulo externo de scraping
- Preparado para escalar a más endpoints


## 🛠️ Tecnologías utilizadas

- Python 3.10+
- Flask
- Requests
- BeautifulSoup (bs4)

## ⚙️ Instalación

Sigue estos pasos para correr el proyecto en tu máquina local:

1. Clona el repositorio:
   ```bash
   git clone https://github.com/luisAngelDev/flask-crud.git
   cd django-scraping
   ```

2. Crea y activa un entorno virtual:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Inicia el servidor:
   ```bash
   python app.py
   ```

5. Inicia el servidor:
   ```bash
   python scrapers.py
   ```



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
