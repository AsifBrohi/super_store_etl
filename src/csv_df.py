import pandas as pd


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

file_path = 'data/SampleSuperstore.csv'
df = turn_into_df(file_path)

def drop_columns(df,to_drop):
    """removing unwatnted columns"""
    try:
        df = df.drop(columns=to_drop)
        return df
    except AssertionError as error:
        print(error)

to_drop= ["Discount","Postal Code","Quantity"]
clean_df= drop_columns(df,to_drop)


def unique_value_df(dataframe,col,column_name):
    """Creating Df with only unique values to avoid duplication"""
    try:
        new_list=dataframe[col].unique().tolist()
        new_df = pd.DataFrame({column_name:new_list})
        return new_df
    except KeyError as error:
        print("Unique Dataframe not made")
        print(error)




df_ship_mode = unique_value_df(df,'Ship Mode','ship_mode')
df_segment = unique_value_df(df,'Segment','segment')
df_country = unique_value_df(df,'Country','country')
df_city = unique_value_df(df,'City','city')
df_state = unique_value_df(df,'State','state')
df_region = unique_value_df(df,'Region','region')
df_category = unique_value_df(df,'Category','category')
df_sub_category = unique_value_df(df,'Sub-Category','sub_category')


