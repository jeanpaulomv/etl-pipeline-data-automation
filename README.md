# ETL Automation

Este proyecto presenta un pipeline de ETL (Extracción, Transformación y Carga) completamente automatizado, diseñado para facilitar la integración de datos desde múltiples fuentes de manera eficiente y precisa. Este ejemplo práctico es ideal para aprender y aplicar ETL en Python, ofreciendo una base sólida para proyectos de integración y análisis de datos.

## 📋 Descripción del Proyecto

Este pipeline sigue un proceso ETL completo para mover y preparar datos para su análisis en bases de datos, permitiendo así una mayor flexibilidad y escalabilidad en el manejo de la información. A continuación, se detalla cada etapa:

- **Extracción**: Obtiene datos desde diversas fuentes, como archivos .csv y bases de datos PostgreSQL y MySQL, asegurando que la información esté centralizada para su posterior procesamiento.
- **Transformación**: Realiza procesos de limpieza y estandarización de datos, que incluyen la eliminación de valores nulos y la corrección de formatos de fecha, a fin de garantizar la consistencia y precisión en los datos preparados.
- **Carga**: Exporta los datos ya transformados hacia bases de datos PostgreSQL o MySQL, donde estarán listos para su consulta y análisis. Este paso final asegura que los datos estén en un formato adecuado para su uso por herramientas de análisis o visualización.
  Este pipeline es adaptable y puede integrarse en flujos de trabajo de análisis de datos para automatizar la gestión de información y mejorar la eficiencia operativa.

## 🧑‍💻 Estructura del Proyecto de ETL

```plaintext
etl_automation/
├── config/
│   └── db_config.yaml
│
├── data/
│   └── sample_data.csv
│
├── etl_pipeline.py
├── README.md
└── requirements.txt
```

## 🗂️ Descripción de Archivos

1. **etl_pipeline.py**: Código principal de Python que realiza las funciones de Extracción, Transformación y Carga.
2. **config/db_config.yaml**: Archivo de configuración para almacenar credenciales y detalles de conexión a las bases de datos (PostgreSQL, MySQL).
3. **data/sample_data.csv**: Datos de ejemplo en formato `.csv` para la prueba de la automatización.
4. **requirements.txt**: Librerías necesarias para ejecutar el pipeline de ETL.

## 🛠️ Herramientas y Librerías

- **Python**: Para scripting.
- **SQLAlchemy**: Conexiones a bases de datos.
- **pandas**: Manipulación de datos.
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

## 🦿 Expansión

Este proyecto es adaptable. Agrega nuevos casos de extracción y carga según tus necesidades.

## 🫂 Contribuciones

Siéntete libre de contribuir a este repositorio o usarlo como base para proyectos de ETL.

<!-- Connect With Me -->

# ✉️ Contacto

<a href="https://www.linkedin.com/in/jeanpaulomv/"><img src="https://img.shields.io/badge/jeanpaulomv-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" height="30"></a>
<a href="https://www.datascienceportfol.io/jeanpaulomv"><img src="https://img.shields.io/badge/Portfolio-255E63?style=for-the-badge&logo=About.me&logoColor=white" alt="Portfolio" height="30"></a>
