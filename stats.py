import pandas as pd

def calculate_stats(data):
    """Calculate basic sales statistics from DataFrame."""
    total = data["Sales"].sum()
    avg = data["Sales"].mean()
    high = data["Sales"].max()
    low = data["Sales"].min()
    variance = data["Sales"].var()
    std_dev = data["Sales"].std()

    return pd.DataFrame([{
        "Total": total,
        "Average": avg,
        "Highest": high,
        "Lowest": low,
        "Variance": variance,
        "Standard Deviation": std_dev
    }])