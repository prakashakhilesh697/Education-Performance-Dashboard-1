import pandas as pd

def drop_columns(df, columns):
    """
    Drop specified columns.
    """
    df = df.drop(columns=columns, errors='ignore')
    return df

def encode_categorical(df):
    """
    Encode categorical features using one-hot encoding.
    """
    cat_cols = df.select_dtypes(include='object').columns
    return pd.get_dummies(df, columns=cat_cols, drop_first=True)

def create_interaction_terms(df):
    """
    Create new features based on interaction of existing features.
    """
    if 'feature1' in df.columns and 'feature2' in df.columns:
        df['interaction'] = df['feature1'] * df['feature2']
    return df

def bin_numerical(df, column, bins, labels):
    """
    Bin numerical column into categories.
    """
    df[f"{column}_binned"] = pd.cut(df[column], bins=bins, labels=labels)
    return df

def normalize_column(df, column):
    """
    Normalize a numerical column.
    """
    df[column] = (df[column] - df[column].min()) / (df[column].max() - df[column].min())
    return df

def scale_standard(df, column):
    """
    Standardize a numerical column.
    """
    df[column] = (df[column] - df[column].mean()) / df[column].std()
    return df
