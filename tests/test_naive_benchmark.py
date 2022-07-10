from ts.naive_benchmark import naive_benchmark
from ts.missing_data import fill_missing_dates
from pandas._testing import makeTimeDataFrame
import pytest

df = makeTimeDataFrame()
df.drop(["C", "D"], axis=1, inplace=True)
df2 = fill_missing_dates(df)


def test_output_length():
    assert len(naive_benchmark(df, "A", 3)) == 2
    assert len(naive_benchmark(df, "B", 7)) == 2


def test_input_type_handling():
    with pytest.raises(TypeError):
        naive_benchmark("Generic String", "A", 7)
    with pytest.raises(TypeError):
        naive_benchmark(df, "A", "Generic String")
    with pytest.raises(ValueError):
        naive_benchmark(df, "A", 0)
    with pytest.raises(ValueError):
        naive_benchmark(df, "A", -1)


def test_default_window():
    assert naive_benchmark(df, "A", 7) == naive_benchmark(df, "A")
    assert naive_benchmark(df, "B", 7) == naive_benchmark(df, "B")


def test_overall_mean():
    assert (
        naive_benchmark(df, "A", 7)[0]
        == ((df.iloc[-7:, 0] - df.iloc[:-7, 0].mean()) ** 2).mean() ** 0.5
    )
    assert (
        naive_benchmark(df, "B", 3)[0]
        == ((df.iloc[-3:, 1] - df.iloc[:-3, 1].mean()) ** 2).mean() ** 0.5
    )


def test_daily_mean():
    assert round(naive_benchmark(df, "A", 1)[1], 8) == round(
        abs(df2.iloc[4::7, 0].iloc[:-1].mean() - df.iloc[-1][0]), 8
    )
    assert round(naive_benchmark(df, "B", 1)[1], 8) == round(
        abs(df2.iloc[4::7, 1].iloc[:-1].mean() - df.iloc[-1][1]), 8
    )
