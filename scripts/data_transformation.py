import pandas as pd

def normalize_column(data: pd.DataFrame, column: str) -> pd.DataFrame:
    """Normalize values of a numeric column."""
    data[column] = (data[column] - data[column].min()) / (data[column].max() - data[column].min())
    return data
