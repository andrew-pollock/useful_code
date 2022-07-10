from ts.missing_data import fill_missing_dates, impute_data
from pandas._testing import makeTimeDataFrame
import numpy as np
import math

df = makeTimeDataFrame()
no_fill_req = df.loc["2000-01-10":"2000-01-14"]
single_date = df.iloc[[0], :]


def test_fill_missing_dates():
    assert len(fill_missing_dates(df)) == 40
    assert len(fill_missing_dates(no_fill_req)) == len(no_fill_req)
    assert len(fill_missing_dates(single_date)) == 1


df = fill_missing_dates(df)
df.drop(["B", "C", "D"], axis=1, inplace=True)
df.loc[["2000-01-26", "2000-02-03", "2000-02-08"], "A"] = np.NaN


def test_impute_data():
    assert impute_data(df=df, col_to_fill="A").loc["2000-01-26", "A"].round(6) == df.loc[
        ["2000-01-19", "2000-02-02"], "A"
    ].mean().round(6)
    assert impute_data(df=df, col_to_fill="A").loc["2000-02-03", "A"].round(6) == df.loc[
        ["2000-01-27", "2000-02-10"], "A"
    ].mean().round(6)
    assert math.isnan(impute_data(df=df, col_to_fill="A").loc["2000-02-08", "A"])
