import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

DATASETS_DIR = os.path.join(os.path.dirname(__file__), '..', 'datasets')
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'outputs')
PLOTS_DIR = os.path.join(OUTPUT_DIR, 'plots')

dataset_name = 'Tabela_04_Pop_resid_por_cor_ou_raca_e_pessoas_indigenas_2022_MU.xlsx'
DATASET_FILE = os.path.join(DATASETS_DIR, dataset_name)

df = pd.read_excel(DATASET_FILE, skiprows=8)

# Check for NaN values
def check_for_nan_values(df):
    nan_cells = df.isna()

    for column in nan_cells.columns:
        for index, value in nan_cells[column].items():
            if value:
                print(f'Row {index} in column {column} is a NaN.')

new_columns_names = ["municipio", "codigo", "total", "branca", "preta", "amarela", "parda", "indigena",
                     "nao_informada", "branca_P", "preta_P", "amarela_P", "parda_P", "indigena_P", "A", "P"]
df.columns = new_columns_names
df.drop(columns=["A", "P"], inplace=True)

for column in df.columns:
    if column != "municipio" and "_P" not in column:
        df[column] = df[column].apply(lambda x: str(x).replace(" ", ""))
        df[column] = pd.to_numeric(df[column], errors='coerce')
        df[column] = df[column].fillna(0)
        df[column] = df[column].astype(int)
    elif "_P" in column:
        df[column] = df[column].apply(lambda x: str(x).replace(",", "."))
        df[column] = pd.to_numeric(df[column], errors='coerce')
        df[column] = df[column].fillna(0)
        df[column] = df[column].astype(float)
        df[column] = df[column].apply(lambda x: (x / 100))

codigo_to_uf = { "12": "AC", "27": "AL", "16": "AP", "13": "AM", "29": "BA", "23": "CE", "53": "DF", "32": "ES",
                "52": "GO", "21": "MA", "51": "MT", "50": "MS", "31": "MG", "15": "PA", "25": "PB", "41": "PR",
                "26": "PE", "22": "PI", "33": "RJ", "24": "RN", "43": "RS", "11": "RO", "14": "RR", "42": "SC",
                "35": "SP", "28": "SE", "17": "TO"}

df["UF"] = (df["codigo"].apply(lambda x: str(x)[:2])).map(codigo_to_uf)

check_for_nan_values(df)

df = df.drop(index=df.index[-1])

print(df.head())

df.to_csv(os.path.join(DATASETS_DIR, "p_Tabela_04_Pop_resid_por_cor_ou_raca_e_pessoas_indigenas_2022_MU.csv"), index=False)
