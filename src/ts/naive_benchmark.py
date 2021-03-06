import pandas as pd


def naive_benchmark(df: pd.DataFrame, y: str, window: int = 7):
    """Calculates RMSE for using simple averages.

    Longer description goes here.

    Args:
        df: A pandas DataFrame with a Date index.
        y: String. Name of the column to forecast.
        window: Int. Size of the test window to be held-out from training and
            used to calculate the RMSE.

    Returns:
        A tuple containing the RMSE using an overall average and a day-specific
        average.
    
    Raises:
        TypeError: df isn't a DataFrame or window isn't convertable to an int.
        ValueError: window is less than 1.
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("df must be a pandas DataFrame")
    try:
        window = int(window)
    except ValueError:
        raise TypeError("window must be convertable to int")
    if window < 1:
        raise ValueError("window must be at least 1")

    temp_df = df[[y]].copy()
    temp_df["DayofWeek"] = temp_df.index.dayofweek
    train = temp_df[:-window]
    test = temp_df[-window:]

    # Calculate mean of training data, overall and by day of week
    overall_mean = train[0:700].loc[:, y].mean()
    daily_mean = train.groupby("DayofWeek").mean().rename({y: "Daily_Mean"}, axis=1)

    # Join the daily predictions on
    test = test.join(daily_mean, on="DayofWeek")

    # Calculate RMSE
    Overall_RMSE = (((test[y] - overall_mean) ** 2).mean()) ** 0.5
    Daily_RMSE = (((test[y] - test["Daily_Mean"]) ** 2).mean()) ** 0.5
    return Overall_RMSE, Daily_RMSE
