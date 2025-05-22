import pandas as pd

def load_data(filepath):
    """
    Load data from CSV file.
    """
    try:
        df = pd.read_csv(filepath)
        print(f"Data loaded successfully with shape: {df.shape}")
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return pd.DataFrame()

def get_basic_info(df):
    """
    Print basic information about the dataset.
    """
    print("First 5 rows:")
    print(df.head())
    print("
Info:")
    print(df.info())
    print("
Missing values:")
    print(df.isnull().sum())

def get_column_types(df):
    """
    Return column types.
    """
    return df.dtypes

def save_cleaned_data(df, path):
    """
    Save cleaned dataset to new CSV file.
    """
    df.to_csv(path, index=False)
    print(f"Cleaned data saved to {path}")

def rename_columns(df, columns_dict):
    """
    Rename columns using a provided dictionary.
    """
    return df.rename(columns=columns_dict)

def sample_data(df, n=5):
    """
    Return a sample of the data.
    """
    return df.sample(n)

def shape_of_data(df):
    """
    Print shape of the dataset.
    """
    print("Data Shape:", df.shape)
