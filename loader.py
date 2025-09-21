import os
import pandas as pd
from datetime import datetime

def load_sales_data(filename):
    """Load CSV into a pandas DataFrame"""
    return pd.read_csv(filename)

def export_report(stats, filename=None):
    """Save stats into data/ folder with timestamp"""
    os.makedirs("data", exist_ok=True)

    if filename is None:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"data/sales_report_{timestamp}.csv"

    # Convert dictionary → DataFrame → CSV
    df = pd.DataFrame(list(stats.items()), columns=["Metric", "Value"])
    df.to_csv(filename, index=False)

    print(f" Report saved to {filename}")
