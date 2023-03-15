from src.csv_df import df
from src.csv_df import drop_columns
from src.csv_df import clean_df
from pandas.testing import assert_frame_equal

#happy path for dropping columns
def test_drop_columns():
    test_df = df 
    test_to_drop= ["Quantity","Discount","Postal Code"]
    result_df = drop_columns(test_df,test_to_drop)
    expected_df = clean_df
    assert_frame_equal(result_df,expected_df)
