import psycopg2
from src.csv_df import df_ship_mode
from src.csv_df import df_region
from src.csv_df import df_segment
from src.csv_df import df_city
from src.csv_df import df_category
from src.csv_df import df_country
from src.csv_df import df_sub_category
from src.csv_df import df_state
from src.csv_df import clean_df
from SQL_queries.postgre_queries import insert_fact_table
from SQL_queries.postgre_queries import shipping_table
from SQL_queries.postgre_queries import region_table
from SQL_queries.postgre_queries import segment_table
from SQL_queries.postgre_queries import city_table
from SQL_queries.postgre_queries import category_table
from SQL_queries.postgre_queries import sub_category_table
from SQL_queries.postgre_queries import country_table
from SQL_queries.postgre_queries import state_table
from SQL_queries.postgre_queries import sales_fact
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