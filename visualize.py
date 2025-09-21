import matplotlib.pyplot as plt

def plot_sales(df):


    plt.figure(figsize=(10,6))
    df.groupby('Region')['Total Revenue'].sum().plot(kind='bar')
    plt.title('Total Revenue by Region')
    plt.ylabel('Total Revenue ($)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    plt.savefig("reports/revenue_distribution.png")

    plt.figure(figsize=(10,6))
    df.groupby('Item Type')['Total Profit'].sum().plot(kind='bar')
    plt.title('Profit by Product Type')
    plt.ylabel('Total Profit ($)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    plt.savefig("data/profit_by_product.png")
   

