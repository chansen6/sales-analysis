from loader import load_sales_data, export_report
from stats import calculate_stats
from visualize import plot_sales

def main():
    sales_data = load_sales_data("data/sales_data.csv")

    stats = calculate_stats(sales_data)

    print("\n Sales Report")
    for k, v in stats.items():
        print(f"{k}: {v}")

    # Export stats to CSV (with timestamp)
    export_report(stats)

    # Plot sales (if column exists)
    plot_sales(sales_data)

if __name__ == "__main__":
    main()
