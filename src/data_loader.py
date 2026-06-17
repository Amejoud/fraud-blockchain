import pandas as pd
import os

def load_data():
    file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'transactions.csv')
    print(f"جاري تحميل الملف: {file_path}")
    return pd.read_csv(file_path)