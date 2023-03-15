<a name="readme-top"></a>

# **SuperStore Simple ETL Pipeline LocalHost**
<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#project-background">Project Background</a>
    </li>
    <li><a href="#extracting-data-using-kagglapi">Extracting Data Using Kaggle API</a></li>
    <li><a href="#Looking-at-dataframe">Looking at DataFrame</a></li>
    <li>
      <a href="#development-roadmap">Development Roadmap</a>
      <ul>
        <li><a href="#data-modelling-%2D-dimension-&-fact-tables-">Data Modelling - Dimension & Fact Tables</a></li>
        <li><a href="#designing-database-schema-%2D-data-normalisation-">Designing Database - Data Normalisation</a></li>
        <li><a href="#database-schema-%2D-final-database-schema-">Database Schema - Final Database Schema</a></li>
        </ul>
      </li>
    <li><a href="#docker-compose-%2D-Docker-compose-">Docker-compose</a></li>  
    <li><a href="python-scripts-&-tests">Python Scripts & Tests</a>
      <ul>
       <li><a href="#Turing-csv-into-df">Turning CSV into DF</a></li>
       <li><a href="#cleansing-data">Cleansing Data</a></li>
       <li><a href="#transforming-data">Transforming Data</a></li>
       <li><a href="#results-of-tests">Results of Tests</a></li>
       <li><a href="#running-queries">Running Queries</a></li>
       <li><a href="#loading-dimensional-data">Loading Dimensional Data</a></li>
       <li><a href="#loading-fact-data">Loading Fact Data</a></li>
       </ul>
      </li>
    <li><a href="#main-script-to-run-pipeline">Main Script to run Pipeline</a></li>
    <li><a href="#visualise-in-adminer">Visualise In Adminer</a></li>
    <li><a href="#Summary">Summary</a></li>
  </ol>
</details>

<!-- PROJECT BACKGROUND -->
## **Project Background**
We'll be walking through the process of building an ETL (Extract, Transform, Load) pipeline using Python, Docker, and PostgreSQL. This will include setting up a local environment for development and testing, as well as discussing best practices for ETL pipeline design. We'll also dive into the concept of data normalization and show you how to create a DB schema using the star method.
## **Extracting Data Using Kaggle API**
```python
file_download = "bravehart101/sample-supermarket-dataset/SampleSuperstore.csv"
kaggle.api.dataset_download_file(dataset=file_download,file_name='SampleSuperstore.csv',path='../data/zip')
```
```python
with ZipFile('../data/zip/SampleSuperstore.csv.zip','r') as file:
        file.extractall('../data/')
        print("unzipped file")
```
We can now put all these steps into a function to make it easier to call and run
```python
import os
def extract_kaggle_api():
    file_exist = os.path.exists('../data/SampleSuperstore.csv')
    if not file_exist:

        print("collecting data from kaggle api")
        file_download = "bravehart101/sample-supermarket-dataset/SampleSuperstore.csv"
        kaggle.api.dataset_download_file(dataset=file_download,file_name='SampleSuperstore.csv',path='../data/zip')
        print("successfully downloaded dataset")
        with ZipFile('../data/zip/SampleSuperstore.csv.zip','r') as file:
            file.extractall('../data/')
        print("unzipped file")
    print("file already exist")
```
## **Looking at DataFrame**
   - **DataFrame** 
        | Ship Mode | Segmenmt | Country | City | State | Postal Code | Region | Category | Sub-Category | Sales | Quantity | Discount | Profit | 
        | ----------- | ----------- |----------- | ----------- |----------- |----------- |----------- |----------- |----------- |----------- |----------- |----------- |----------- |
        | Second Class | Corporate | United States | Los Angeles | California | 90036 | West | Office Supplies | Labels | 14.6200 | 2 | 0.00 | 6.871 |
        | Standard Class | Consumer | United States | Henderson | Kentucky | 42420 | South | Furniture | Bookcases | 261.960 | 2 | 0.00 | 41.91 |
When looking at the data you can see there are many duplicate values inside the data frame. To remove all duplicate data we will need to normalise the data.

So I decided to create dimension tables for shipmode to sub_category columns as seen above there are duplicates in all of those columns. 
To visualise how approached this is seen below where each column has been normalised and finally a sales fact table

## **Development Roadmap**
### Data Modelling - Dimension & Fact Tables
Kimball
In Kimball's data modelling approach, data is divided into two main types of tables: fact tables and dimension tables, which are organized in a star schema. The fact table stores quantitative, factual, and event-related data that is immutable since it relates to events. Thus, the fact table is append-only and should be at the lowest possible granularity. Fact tables are typically narrow and long, meaning they have few columns and many rows representing events.

The second type of table in a Kimball data model is a dimension table, which provides reference data, attributes, and relational context for the events stored in the fact table. Dimension tables are shorter and wider than fact tables and are denormalized, allowing for duplicate data. When joined with a fact table, dimensions can provide details on the "what," "where," and "when" of events.
The star schema represents the data model of the business, with the fact table at the centre, surrounded by relevant dimensions. Compared to highly normalized data models, the star schema requires fewer joins, resulting in faster query performance. Additionally, the star schema is easier for business users to understand and use.

It is important to note that the star schema should not be based on a particular report. Instead, it should capture the essential facts and attributes of the business and be flexible enough to answer critical questions. Reports can be modelled downstream in a data mart or directly in a business intelligence tool.

*Reference: Fundamentals of Data Engineering Plan and Build Robust Data Systems*
### Designing Database - Data Normalisation
- **shipmodes Table**
    | ship_mode_id | ship_mode |
    | ----------- | ----------- |
    | 1 | Standard Class |
    | 2 | Second Class |
    | 3 | First Class |
    | 4 | Same Day |

 - **segments Table**
    | segments_id | segments |
    | ----------- | ----------- |
    | 1 | Consumer |
    | 2 | Corporate |
    | 3 | Home Office |
   

 - **country Table**
    | country _id | country |
    | ----------- | ----------- |
    | 1 | United States |


 - **city Table**
    | city_id | city |
    | ----------- | ----------- |
    | 1 | Henderson |
    | 2 | Los Angeles |
    | 3 | Concord |
    | 4 | Seattle | 

 - **state Table**
    | state_id | state |
    | ----------- | ----------- |
    | 1 | Kentucky |
    | 2 | California |
    | 3 | Florida |
    | 4 | Pennsylvania | 

  - **regions Table**
    | reigion_id | region |
    | ----------- | ----------- |
    | 1 | South |
    | 2 | West |
    | 3 | East |
    | 4 | North |

 - **category Table**
    | category _id | category  |
    | ----------- | ----------- |
    | 1 | Furniture |
    | 2 | Office Supplies |
    | 3 | Technology |


 - **sub-category Table**
    | sub-category_id | sub-category |
    | ----------- | ----------- |
    | 1 | Bookcases |
    | 2 | Chairs |
    | 3 | Labels |
    | 4 | Tables | 

   

### Database Schema - Final Database Schema 
![image](https://user-images.githubusercontent.com/52333702/225302318-df36dc5b-0797-48c4-ab30-a4b9f85f3b5f.png)



## **Docker-compose**
```yaml
version: "3.1"
services:
  db:
    image: postgres
    container_name: super_store
    restart: always
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: pass
      POSTGRES_DB: postgres
      
    ports:
      - 5432:5432
    volumes:
      -  ./demo_db:/var/lib/postgresql/data
  adminer:
    image: adminer
    container_name: adminer_container_demo
    restart: always
    ports:
      - 8080:8080
volumes:
  demo_db: 
```
## **Python Scripts & Tests**
### Turning CSV into DF
```python
# Happy Path 
def test_csv_into_df():
    file_path = "../data/SampleSuperstore.csv"
    assert type(turn_into_df(file_path)) == pd.DataFrame
# Unhappy Path
def test_file_missing():
    file_path = "../data/no.csv"
    assert type(turn_into_df(file_path)) == FileNotFoundError

def test_file_no_data():
    file_path = '../data/no_data.csv'
    assert type(turn_into_df(file_path)) == pd.errors.EmptyDataError

def turn_into_df(file_path):
    """turning csv file into DF"""
    try:
        df = pd.read_csv(file_path)
        print("File Successfully turned into a DF")
        return df 
    except FileNotFoundError as error:
        print(f"There is No file at {file_path}")
        return error
    except pd.errors.EmptyDataError as empty_data_error:
        print(f"There is No data in {file_path}")
        return empty_data_error

```
### Cleansing Data 
```python
def test_drop_columns():
    # creating test df
    test_df = df 
    # create test drop list
    test_to_drop= ["Quantity","Discount","Postal Code"]
    # call function
    result_df = drop_columns(test_df,test_to_drop)
    # check that result dataframe has expected values
    expected_df = clean_df
    assert_frame_equal(result_df,expected_df)

def drop_columns(df,to_drop):
    """removing unwatnted columns"""
    try:
        df = df.drop(columns=to_drop)
        return df
    except AssertionError as error:
        print(error)
```
### Transforming Data
```python
def test_unique_value_df():
    # create a dataframe with some data
    test_df = df
    # call the function with a valid column name
    test_col_name = 'Ship Mode'
    test_new_col_name = 'ship_mode'
    result = unique_value_df(test_df, test_col_name, test_new_col_name)
    # check that the result dataframe has the expected values
    expected_values = df_ship_mode
    assert_frame_equal(result, expected_values)

def unique_value_df(dataframe,col,column_name):
    """Creating Df with only unique values to avoid duplication"""
    try:
        new_list=dataframe[col].unique().tolist()
        new_df = pd.DataFrame({column_name:new_list})
        return new_df
    except KeyError as error:
        print("Unique Dataframe not made")
        print(error)

```
### Results of Tests

![image](https://user-images.githubusercontent.com/52333702/225459449-9ac92f04-724c-4c0d-b950-0abd30bcaf12.png)

### Loading Dimensional Data
```python
def run_query(conn, query):
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        print(f"Successfully ran query")
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Following query failed {query}")
        print(error)
```
### Loading Dimensional Data
```python

def insert_values_in_table(cursor, df, table_name):
    cols = ", ".join(df.columns)
    asterisk = ", ".join(["%s"] * len(df.columns))
    query = (
        f"INSERT INTO {table_name}({cols}) VALUES ({asterisk}) "
    )
    for index, row in df.iterrows():
        values = tuple(row)
        cursor.execute(query, values)
    conn.commit()
    return

```
### Loading Fact Data 
```python

def load_sales_to_db(cursor, df,insert_query):
    # create connection
    tuples = [tuple(x) for x in df.to_numpy()]

    try:
        cursor.executemany(
            insert_query,
            tuples
        )
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        return
```
## **Main Script to run Pipeline**
```python

# connecting to database 
conn = psycopg2.connect(
database="super_store",
host="localhost",
user="postgres",
password="pass"
)
print("connected to Database")

# Function which runs postgres querries 
def run_query(conn, query):
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        print(f"Successfully ran query")
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Following query failed {query}")
        print(error)

# function which loads values to dimension tables 
def insert_values_in_table(cursor, df, table_name):
    cols = ", ".join(df.columns)
    asterisk = ", ".join(["%s"] * len(df.columns))
    query = (
        f"INSERT INTO {table_name}({cols}) VALUES ({asterisk}) "
    )
    for index, row in df.iterrows():
        values = tuple(row)
        cursor.execute(query, values)
    conn.commit()
    return

#function loads data to the fact table 
def load_sales_to_db(cursor, df,insert_query):
    # create connection
    tuples = [tuple(x) for x in df.to_numpy()]

    try:
        cursor.executemany(
            insert_query,
            tuples
        )
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error: %s" % error)
        return
    
# main function which runs the whole ETL process 
def main():

    run_query(conn,shipping_table)
    run_query(conn,region_table)
    run_query(conn,segment_table)
    run_query(conn,city_table)
    run_query(conn,category_table)
    run_query(conn,sub_category_table)
    run_query(conn,country_table)
    run_query(conn,state_table)
    run_query(conn,sales_fact)
    print("all queries have been run successfully")
    cursor = conn.cursor()
    print("Cursor is made")
    insert_values_in_table(cursor,df_ship_mode,'ship_mode')
    insert_values_in_table(cursor,df_region,'regions')
    insert_values_in_table(cursor,df_segment,'segments')
    insert_values_in_table(cursor,df_city,'citys')
    insert_values_in_table(cursor,df_category,'category')
    insert_values_in_table(cursor,df_sub_category,'sub_category')
    insert_values_in_table(cursor,df_country,'country')
    insert_values_in_table(cursor,df_state,'states')

    load_sales_to_db(cursor,clean_df,insert_fact_table)
    print("all data has been ingested")
    conn.close()

if __name__ == "__main__":
    main()
```
## **Visualise In Adminer**
When going onto localhost :8080 you can see that all the data has successfully been loaded into the Database. Seen Below is the fact sales table with all the FK columns from the dimension tables. All highlighted so when clicking on a field, it will show in the dimensional table what is is representing seen below.
## **Summary**
In this mini-project, we demonstrate how to extract data from Kaggle using its API and normalize it for data modelling. By applying Test-Driven Development (TDD) principles, we ensure the reliability and accuracy of our data cleansing and transformation process. To load the transformed data into a database locally, we leverage Docker and Postgres, which allows us to scale our data operations as needed.

My project showcases how data extraction and normalization are critical components of any data processing pipeline, and highlights the importance of TDD in ensuring data quality. By deploying our solution locally, we demonstrate how Docker and Postgres enable efficient management of data operations. In a follow-up blog, I will show how to take this process to the cloud and utilize Apache Airflow for further automation and scalability.
