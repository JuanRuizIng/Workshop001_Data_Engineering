# Workshop #1: Data Engineer <img src="https://github.com/user-attachments/assets/e50b269a-fd97-4ec3-a1e9-e9629cef94ae" alt="Data Icon" width="30px"/>

Realized by **Juan Andrés Ruiz Muñoz** ([@JuanRuizIng](https://github.com/JuanRuizIng)).

## Overview ✨

In this workshop we use randomly generated data on candidates stored in a CSV. With this data we run loading, cleaning and transformation processes to find interesting insights using the following tools:

* Python ➜ [Download site](https://www.python.org/downloads/)
* Jupyter Notebook ➜ [VS Code tool for using notebooks](https://youtu.be/ZYat1is07VI?si=BMHUgk7XrJQksTkt)
* PostgreSQL ➜ [Download site](https://www.postgresql.org/download/)
* Power BI (Desktop version) ➜ [Download site](https://www.microsoft.com/es-es/power-platform/products/power-bi/desktop)

The libraries needed for Python are

* Pandas
* Matplotlib
* Seaborn
* SQLAlchemy

These libraries are included in the Poetry project config file (*pyproject.toml*). The step-by-step installation will be described later.

## Dataset Information <img src="https://github.com/user-attachments/assets/5fa5298c-e359-4ef1-976d-b6132e8bda9a" alt="Dataset" width="30px"/>


The dataset used (*candidates.csv*) has 50,000 rows and 10 columns describing each candidate registered for the recruitment process. 
This dataset is further transformed to be better processed by the visual analysis tool.
Initially, the column names of the dataset and their respective Dtype are:

* First Name ➜ Object
* Last Name ➜ Object
* Email ➜ Object
* Country ➜ Object
* Application Date ➜ Timestamp without time zone
* YOE (years of experience) ➜ Integer
* Seniority ➜ Object
* Technology ➜ Object
* Code Challenge Score ➜ Integer
* Technical Interview Score ➜ Integer

### Clone the repository

Execute the following command to clone the repository:

```bash
  git clone https://github.com/JuanRuizIng/Workshop001_Data_Engineering.git
```

### Credentials variables

> From now on, the steps will be done in VS Code.

To establish the connection to the database, we use a module called *database* from the *function/database* package. In this Python script we call a file where our JSON credentials are stored, this is how we will create this file:

1. We create a directory named ***credentials*** inside our cloned repository.

2. There we create a file called ***credential.json***.

3. In that file we declare 5 credential variables:
   ```json
   {
    "username":"DB_USERNAME",
    "password":"DB_PASSWORD",
    "host":"DB_HOST",
    "port":"DB_PORT",
    "database":"DB_NAME"
   }
   ```

#### Example of the process

   ```json
   {
    "username":"postgres",
    "password":"root",
    "host":"localhost",
    "port":5432,
    "database":"candidate"
   }
   ```

### Installing the dependencies with *Poetry*

> To install Poetry follow `pip install poetry`.

In the repository terminal:

1. Enter the Poetry shell with `poetry shell`.

2. Once the virtual environment is created, execute `poetry install` to install the dependencies.

### Set candidates.csv

Place candidates.csv inside the data/raw folder

![image](https://github.com/user-attachments/assets/e05d41e9-895b-47d4-941c-1f835f71b2d5)

### Running the code

1. We execute "main.py"

2. To view the EDA process, we execute the 2 notebooks following the next order. You can run it just pressing the "Execute All" button:

   1. *EDA_raw.ipynb*
   2. *EDA_cleaned.ipynb*
  
Remember to choose **the appropriate Python kernel** when running the notebook and **install the *ipykernel*** to support Jupyter notebooks in VS Code with the poetry virtual environment.

### Connecting the database with Power BI

1. Open Power BI Desktop and create a new dashboard. Select the *Get data* option - be sure you choose the "PostgreSQL Database" option.

![Power BI](https://github.com/user-attachments/assets/a53ef992-d5b9-468e-b227-94e72179a591)


2. Insert the PostgreSQL Server and Database Name.

![image](https://github.com/user-attachments/assets/ebe02754-44e8-498c-891f-e1a0038d351d)


3. Fill in the following fields with your credentials.

![image](https://github.com/user-attachments/assets/18748b7f-7d5c-4c21-891a-70e77dd21d69)


4. If you manage to connect to the database the following tables will appear:

![image](https://github.com/user-attachments/assets/296845e6-689a-4758-9444-99ef2aa6cc66)


5. Choose the candidates_cleaned table and start making your own visualizations!

![image](https://github.com/user-attachments/assets/2133216d-5d4e-462d-b475-82a6f3a42be0)


## Thank you! 💩🐍

Law 7, The 48 Laws of Power - Robert Greene
