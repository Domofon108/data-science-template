import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def eda_summary(df):
    """Prints basic information about the dataset."""
    print(df.info())
    print(df.describe())

def plot_distribution(df, column):
    """Plots a histogram for a specified column."""
    sns.histplot(df[column], bins=30)
    plt.show()

