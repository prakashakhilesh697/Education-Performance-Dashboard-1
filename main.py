from data_loader import load_data, get_basic_info
from cleaning import drop_duplicates, fill_missing
from feature_engineering import drop_columns, encode_categorical
from visualization import pairplot_numeric, correlation_heatmap

def main():
    path = 'your_dataset.csv'  # Replace with your actual dataset path
    df = load_data(path)
    if df.empty:
        return
    
    get_basic_info(df)

    # Cleaning
    df = drop_duplicates(df)
    df = fill_missing(df, method='ffill')

    # Feature Engineering
    df = drop_columns(df, ['unnecessary_column'])
    df = encode_categorical(df)

    # Visualizations
    pairplot_numeric(df)
    correlation_heatmap(df)

if __name__ == "__main__":
    main()
