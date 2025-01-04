# Pipeline ETL: Automatización de Datos

## 📋 Descripción del Proyecto

Este proyecto implementa un pipeline de ETL (Extracción, Transformación y Carga) completamente automatizado, diseñado para facilitar la integración de datos desde múltiples fuentes de manera eficiente y precisa. Este pipeline permite preparar y mover datos para su análisis en bases de datos, garantizando flexibilidad y escalabilidad en el manejo de la información.

El diseño modular del proyecto permite agregar nuevos casos de extracción y carga según las necesidades, lo que lo hace fácilmente adaptable a diferentes fuentes de datos y bases de datos de destino.

A continuación, se detallan las etapas del proceso ETL:

1. **Extraction**: Captura y lee datos desde diversas fuentes, como archivos CSV, APIs y bases de datos externas.
2. **Transform**: Realiza limpieza, formateo y enriquecimiento de datos, asegurando que estén listos para análisis o almacenamiento.
3. **Load**: Inserta los datos transformados en una base de datos de destino (por ejemplo, PostgreSQL o MySQL) para facilitar consultas y análisis.

## 🧑‍💻 Estructura del Proyecto de ETL

```plaintext
etl_automation/
├── config/
│   └── db_config.yaml        # Archivo de configuración para almacenar credenciales y detalles de conexión a las bases de datos (PostgreSQL, MySQL).
│
├── data/
│   └── sample_data.csv       # Datos de ejemplo en formato .csv para la prueba de la automatización.
│
├── etl_pipeline.py           # Código principal de Python que realiza las funciones de Extracción, Transformación y Carga.
├── README.md                 # Archivo de documentación que explica el proyecto y su uso.
└── requirements.txt          # Librerías necesarias para ejecutar el pipeline de ETL.
```

## 🛠️ Herramientas y Librerías

- **Python**: Para scripting.
- **SQLAlchemy**: Conexiones a bases de datos.
- **Pandas**: Manipulación de datos.
- **PyYAML**: Lectura de configuraciones.

## ⚙️ Configuración

1. Clona el repositorio:

   ```plaintext
   git clone https://github.com/tu_usuario/etl_automation.git
   ```

2. Instala las dependencias:

   ```plaintext
   pip install -r requirements.txt
   ```

3. Configura las credenciales en config/db_config.yaml.

## ⌛ Ejecución

- Ejecuta el pipeline de ETL:

  ```bash
  python etl_pipeline.py
  ```

## 🫂 Contribuciones

> **💡 Siéntete libre de contribuir a este repositorio o utilizarlo como base para tus propios proyectos de ETL. ¡Tu aporte y creatividad son bienvenidos!**

<!-- Connect With Me -->

## ✉️ Contacto

<a href="https://www.linkedin.com/in/jeanpaulomv/"><img src="https://img.shields.io/badge/jeanpaulomv-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" height="30"></a>
<a href="https://www.datascienceportfol.io/jeanpaulomv"><img src="https://img.shields.io/badge/Portfolio-255E63?style=for-the-badge&logo=About.me&logoColor=white" alt="Portfolio" height="30"></a>
