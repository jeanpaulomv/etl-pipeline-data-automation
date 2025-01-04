# ETL Pipeline: Data Automation

## 📋 Project Description

This project implements a fully automated ETL (Extraction, Transformation and Loading) pipeline, designed to facilitate the integration of data from multiple sources in an efficient and accurate manner. This pipeline allows data to be prepared and moved for analysis in databases, ensuring flexibility and scalability in information management.

The modular design of the project allows new extraction and loading cases to be added as needed, making it easily adaptable to different data sources and target databases.

The stages of the ETL process are detailed below:

1. **Extraction**: Capture and read data from a variety of sources, including CSV files, APIs, and external databases.
2. **Transform**: Performs data cleansing, formatting and enrichment, ensuring it is ready for analysis or storage.
3. **Load**: Insert the transformed data into a target database (for example, PostgreSQL or MySQL) for easy querying and analysis.

## 🧑‍💻 ETL Project Structure

```plaintext
etl_automation/
├── config/
│   └── db_config.yaml        # Configuration file to store credentials and connection details to databases (PostgreSQL, MySQL).
│
├── data/
│   └── sample_data.csv       # Sample data in .csv format for automation testing.
│
├── etl_pipeline.py           # Main Python code that performs the Extraction, Transformation and Loading functions.
├── README.md                 # Documentation file explaining the project and its use.
└── requirements.txt          # Libraries required to run the ETL pipeline.
```

## 🛠️ Tools and Libraries

- **Python**: For scripting.
- **SQLAlchemy**: Database connections.
- **Pandas**: Data manipulation.
- **PyYAML**: Reading settings.

## ⚙️ Configuration

1. Clone the repository:

   ```plaintext
   git clone https://github.com/tu_usuario/etl_automation.git
   ```

2. Install dependencies:

   ```plaintext
   pip install -r requirements.txt
   ```

3. Configura las credenciales en config/db_config.yaml.

## ⌛ Execution

- Run the ETL pipeline:

  ```bash
  python etl_pipeline.py
  ```

## 🫂 Contributions

> **💡 Feel free to contribute to this repository or use it as a basis for your own ETL projects. Your input and creativity are welcome!**

<!-- Connect With Me -->

## ✉️ Contact

<a href="https://www.linkedin.com/in/jeanpaulomv/"><img src="https://img.shields.io/badge/jeanpaulomv-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" height="30"></a>
<a href="https://www.datascienceportfol.io/jeanpaulomv"><img src="https://img.shields.io/badge/Portfolio-255E63?style=for-the-badge&logo=About.me&logoColor=white" alt="Portfolio" height="30"></a>
