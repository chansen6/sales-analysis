import matplotlib.pyplot as plt

def plot_sales(df):
    """Plot sales over time if Date column exists"""
    if "Date" not in df.columns or "Sales" not in df.columns:
        print("⚠️ Cannot plot: missing Date or Sales column")
        return

    df.plot(x="Date", y="Sales", kind="line", marker="o", title="Sales Over Time")
    plt.xlabel("Date")
    plt.ylabel("Sales")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
