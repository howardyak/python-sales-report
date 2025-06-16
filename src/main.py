from pathlib import Path
from report_utils import load_sales_data, get_top_products, plot_top_products, print_summary

DATA_PATH = Path(__file__).parent.parent / 'data' / 'sales_sample.xlsx'
OUTPUT_PATH = Path(__file__).parent.parent / 'output' / 'summary.png'

def main():
    df = load_sales_data(DATA_PATH)
    top = get_top_products(df)
    plot_top_products(top, OUTPUT_PATH)
    print_summary(df, top)

if __name__ == '__main__':
    main()