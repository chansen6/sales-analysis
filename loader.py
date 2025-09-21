import pandas as pd
import os
from datetime import datetime

def load_sales_data(filepath):
    return pd.read_csv(filepath)

def export_report(stats, output_dir="data/reports"):
    os.makedirs(output_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = os.path.join(output_dir, f"stats_{timestamp}.csv")