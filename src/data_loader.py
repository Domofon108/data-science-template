import pandas as pd

def load_data(filepath):
    """Loads data into a Pandas DataFrame."""
    return pd.read_csv(filepath)

if __name__ == "__main__":
    df = load_data("../data/raw/dataset.csv")
    print(df.head())

