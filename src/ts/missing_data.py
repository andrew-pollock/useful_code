import pandas as pd


def fill_missing_dates(df: pd.DataFrame):
    """
    Adds an empty row for any date that's missing between the first and last
    date in the index.

    Args:
        df: A pandas DataFrame with a Date index.

    Returns:
        A pandas DataFrame with a Date index.
    """
    date_list = pd.date_range(min(df.index), max(df.index)).to_list()
    return df.reindex(date_list)


def impute_data(df: pd.DataFrame, col_to_fill: str):
    """Imputes missing data for a specified column.

    Fills any NA values in a specified column, using the average of the last and
    next value for that day of the week. It's possible for some NAs to still
    exist after this if there isn't enough data for that day of the week to fill
    in the gaps.

    Args:
        df: A pandas DataFrame with a Date index.
        col_to_fill: A string with the name of the column to impute.

    Returns:
        A pandas DataFrame with a Date index.
    """
    temp_df = df.copy()
    temp_df["DayOfWeek"] = temp_df.index.day_of_week
    temp_df["Rolling_Mean"] = (
        temp_df.groupby("DayOfWeek")[col_to_fill]
        .rolling(3, min_periods=2, center=True)
        .mean()
        .reset_index(0, drop=True)
    )
    temp_df[col_to_fill] = temp_df[col_to_fill].fillna(temp_df["Rolling_Mean"])
    return temp_df.iloc[:, :-2]
