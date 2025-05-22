import pandas as pd
import numpy as np

def drop_duplicates(df):
    before = df.shape[0]
    df = df.drop_duplicates()
    after = df.shape[0]
    print(f"Dropped {before - after} duplicate rows.")
    return df

def fill_missing(df, method='ffill'):
    """
    Fill missing values using the specified method.
    """
    return df.fillna(method=method)

def drop_missing(df):
    """
    Drop rows with any missing values.
    """
    return df.dropna()

def detect_missing(df):
    """
    Return columns with missing data.
    """
    return df.isnull().sum()

def replace_values(df, column, to_replace, value):
    """
    Replace specific values in a column.
    """
    df[column] = df[column].replace(to_replace, value)
    return df

def convert_types(df, column, dtype):
    """
    Convert column to specified type.
    """
    df[column] = df[column].astype(dtype)
    return df

def remove_outliers_iqr(df, column):
    """
    Remove outliers using IQR method.
    """
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    before = df.shape[0]
    df = df[(df[column] >= Q1 - 1.5 * IQR) & (df[column] <= Q3 + 1.5 * IQR)]
    after = df.shape[0]
    print(f"Removed {before - after} outliers from {column}.")
    return df
