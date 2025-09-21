import numpy as np

def calculate_stats(df):
    """Calculate summary statistics from sales data"""
    sales = df["Sales"]  # assumes your CSV has a "Sales" column

    total = sales.sum()
    avg = sales.mean()
    high = sales.max()
    low = sales.min()
    variance = round(sales.var(), 2)
    std_dev = round(sales.std(), 2)

    return {
        "Total Sales": total,
        "Average Sale": round(avg, 2),
        "Highest Sale": high,
        "Lowest Sale": low,
        "Variance": variance,
        "Standard Deviation": std_dev
    }
