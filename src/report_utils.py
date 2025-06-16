import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

REQUIRED_COLUMNS = {'Product', 'Quantity', 'Price'}

# загрузка excel файла с проверкой структуры таблицы
def load_sales_data(filepath: Path):
    df = pd.read_excel(filepath)
    
    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise ValueError(f"Excel файл не содержит нужных колонок: {', '.join(missing)}")
    
    df['Total'] = df['Quantity'] * df['Price']
    return df

# топ 5 товаров по выручке
def get_top_products(df: pd.DataFrame, top_n: int = 5):
    return df.groupby('Product')['Total'].sum().nlargest(top_n)

# построение графика
def plot_top_products(top: pd.Series, output_path: Path):
    plt.figure(figsize=(8, 5))
    top.plot(kind='bar', color='skyblue', title='Top Products by Revenue')
    plt.ylabel('Revenue (₽)')
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()

# вывод в консоль
def print_summary(df: pd.DataFrame, top: pd.Series):
    print(f"Общая выручка: {df['Total'].sum():,.2f} руб")
    print("\nТоп товаров по выручке:")
    print(top)