def calculate_stats(df):
    """Calculate summary statistics from sales data"""

    # pick the column you want to analyze
    sales = df["Total Revenue"]

    total = sales.sum()
    avg = sales.mean()
    high = sales.max()
    low = sales.min()
    variance = round(sales.var(), 2)
    std_dev = round(sales.std(), 2)

    return {
        "Total Revenue": total,
        "Average Revenue": round(avg, 2),
        "Highest Revenue": high,
        "Lowest Revenue": low,
        "Variance": variance,
        "Standard Deviation": std_dev
    }
