import matplotlib.pyplot as plt

def plot_sales(data):
    """Plot sales over time."""
    plt.figure(figsize=(8,5))
    plt.plot(data["Date"], data["Sales"], marker="o")
    plt.title("Sales Over Time")
    plt.xlabel("Date")
    plt.ylabel("Sales ($)")
    plt.grid(True)
    plt.show()