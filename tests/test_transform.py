from src.csv_df import df
from pandas.testing import assert_frame_equal
from src.csv_df import unique_value_df
from src.csv_df import df_ship_mode
from src.csv_df import df_segment
from src.csv_df import df_country
from src.csv_df import df_city
from src.csv_df import df_state
from src.csv_df import df_region
from src.csv_df import df_category
from src.csv_df import df_sub_category

def test_unique_value_shipmode():
    # create a dataframe with some data
    test_df = df
    
    # call the function with a valid column name
    test_col_name = 'Ship Mode'
    test_new_col_name = 'ship_mode'
    result = unique_value_df(test_df, test_col_name, test_new_col_name)
    
    # check that the result dataframe has the expected values
    expected_values = df_ship_mode
    assert_frame_equal(result, expected_values)

def test_unique_value_segment():
    # create a dataframe with some data
    test_df = df
    
    # call the function with a valid column name
    test_col_name = 'Segment'
    test_new_col_name = 'segment'
    result = unique_value_df(test_df, test_col_name, test_new_col_name)
    
    # check that the result dataframe has the expected values
    expected_values = df_segment
    assert_frame_equal(result, expected_values)

def test_unique_value_country():
    # create a dataframe with some data
    test_df = df
    
    # call the function with a valid column name
    test_col_name = 'Country'
    test_new_col_name = 'country'
    result = unique_value_df(test_df, test_col_name, test_new_col_name)
    
    # check that the result dataframe has the expected values
    expected_values = df_country
    assert_frame_equal(result, expected_values)

def test_unique_value_city():
    # create a dataframe with some data
    test_df = df
    
    # call the function with a valid column name
    test_col_name = 'City'
    test_new_col_name = 'city'
    result = unique_value_df(test_df, test_col_name, test_new_col_name)
    
    # check that the result dataframe has the expected values
    expected_values = df_city
    assert_frame_equal(result, expected_values)

def test_unique_value_state():
    # create a dataframe with some data
    test_df = df
    
    # call the function with a valid column name
    test_col_name = 'State'
    test_new_col_name = 'state'
    result = unique_value_df(test_df, test_col_name, test_new_col_name)
    
    # check that the result dataframe has the expected values
    expected_values = df_state
    assert_frame_equal(result, expected_values)

def test_unique_value_region():
    # create a dataframe with some data
    test_df = df
    
    # call the function with a valid column name
    test_col_name = 'Region'
    test_new_col_name = 'region'
    result = unique_value_df(test_df, test_col_name, test_new_col_name)
    
    # check that the result dataframe has the expected values
    expected_values = df_region
    assert_frame_equal(result, expected_values)

def test_unique_value_category():
    # create a dataframe with some data
    test_df = df
    
    # call the function with a valid column name
    test_col_name = 'Category'
    test_new_col_name = 'category'
    result = unique_value_df(test_df, test_col_name, test_new_col_name)
    
    # check that the result dataframe has the expected values
    expected_values = df_category
    assert_frame_equal(result, expected_values)

def test_unique_value_sub_category():
    # create a dataframe with some data
    test_df = df
    
    # call the function with a valid column name
    test_col_name = 'Sub-Category'
    test_new_col_name = 'sub_category'
    result = unique_value_df(test_df, test_col_name, test_new_col_name)
    
    # check that the result dataframe has the expected values
    expected_values = df_sub_category
    assert_frame_equal(result, expected_values)
