import matplotlib.pyplot as plt
import seaborn as sns

def pairplot_numeric(df):
    """
    Create a seaborn pairplot of numerical columns.
    """
    sns.pairplot(df.select_dtypes(include='number'))
    plt.show()

def histogram(df, column):
    """
    Plot histogram of a column.
    """
    plt.figure(figsize=(8, 5))
    sns.histplot(df[column], kde=True)
    plt.title(f"Histogram of {column}")
    plt.show()

def correlation_heatmap(df):
    """
    Display a correlation heatmap.
    """
    plt.figure(figsize=(10, 8))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
    plt.title("Correlation Heatmap")
    plt.show()

def boxplot(df, column):
    """
    Display boxplot for a specific column.
    """
    plt.figure(figsize=(6, 4))
    sns.boxplot(x=df[column])
    plt.title(f"Boxplot of {column}")
    plt.show()

def scatter_plot(df, x_col, y_col):
    """
    Scatter plot between two columns.
    """
    plt.figure(figsize=(6, 4))
    sns.scatterplot(x=df[x_col], y=df[y_col])
    plt.title(f"{y_col} vs {x_col}")
    plt.show()
