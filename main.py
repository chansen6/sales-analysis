from sales-analysis.loader import load_sales_data, export_report
from sales-analysis.stats import calculate_stats
from sales-analysis.visualize import plot_sales

def main():
    data = load_sales_data("data/sales_data.csv")
    stats = calculate_stats(data)
    export_report(stats)
    plot_sales(data)

if __name__ == "__main__":
    main()