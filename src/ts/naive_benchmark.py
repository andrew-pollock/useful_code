import pandas as pd


def naive_benchmark(df: pd.DataFrame, y: str, window: int = 7):

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
