import pandas as pd
from random import randint, choice
from datetime import datetime, timedelta
from pathlib import Path

def generate_sample_data(output_path: Path, rows: int = 100):
    products = ['Notebook', 'Pen', 'Pencil', 'Monitor', 'Keyboard']
    categories = {
        'Notebook': 'Stationery',
        'Pen': 'Stationery',
        'Pencil': 'Stationery',
        'Monitor': 'Electronics',
        'Keyboard': 'Electronics'
    }
    regions = ['North', 'South', 'West', 'East']
    start_date = datetime(2023, 1, 1)

    data = []
    for _ in range(rows):
        prod = choice(products)
        row = {
            'Date': start_date + timedelta(days=randint(0, 60)),
            'Product': prod,
            'Category': categories[prod],
            'Region': choice(regions),
            'Quantity': randint(1, 10),
            'Price': randint(100, 500) if prod in ['Monitor', 'Keyboard'] else randint(20, 100),
        }
        data.append(row)

    df = pd.DataFrame(data)
    df.to_excel(output_path, index=False)
    print(f"✅ Простые данные для тестов готовы: {output_path}")

if __name__ == "__main__":
    output_file = Path(__file__).parent.parent / 'data' / 'sales_sample.xlsx'
    output_file.parent.mkdir(parents=True, exist_ok=True)
    generate_sample_data(output_file)