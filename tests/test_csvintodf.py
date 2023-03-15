from src.csv_df import turn_into_df
import pandas as pd
from pandas.testing import assert_frame_equal

def test_csv_into_df():
    file_path = "data/SampleSuperstore.csv"
    assert type(turn_into_df(file_path)) == pd.DataFrame

def test_file_missing():
    file_path = "data/no.csv"
    assert type(turn_into_df(file_path)) == FileNotFoundError

def test_file_no_data():
    file_path = 'data/no_data.csv'
    assert type(turn_into_df(file_path)) == pd.errors.EmptyDataError



