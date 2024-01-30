import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

DATASETS_DIR = os.path.join(os.path.dirname(__file__), '..', 'datasets')
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'outputs')
PLOTS_DIR = os.path.join(os.path.dirname(__file__), '..', 'plots')

dataset_name = 'p_Tabela_04_Pop_resid_por_cor_ou_raca_e_pessoas_indigenas_2022_MU.csv'
DATASET_FILE = os.path.join(DATASETS_DIR, dataset_name)

df = pd.read_csv(DATASET_FILE)

# Ethnicity population in Brazil per region

def plot_distribuicao_etnica_por_municipio(df):
    ufs = df['UF'].unique()

    for i, uf in enumerate(ufs):
        for municipio in df[df['UF'] == uf]['municipio'].unique():
            df_municipio = df[(df['UF'] == uf) & (df['municipio'] == municipio)].set_index('municipio')[['branca', 'indigena', 'preta', 'parda', 'amarela']]
            fig, ax = plt.subplots(figsize=(16, 16))
            ax.pie(df_municipio.iloc[0], labels=df_municipio.columns, autopct='%.2f%%', startangle=0)

            ax.set_title(f'Distribuição Étnica em {municipio}')
            plt.legend()

            if not os.path.exists(os.path.join(PLOTS_DIR, f'distribuicao_etnica_municipio/{uf}')):
                os.makedirs(os.path.join(PLOTS_DIR, f'distribuicao_etnica_municipio/{uf}'))

            plt.savefig(os.path.join(PLOTS_DIR, f'distribuicao_etnica_municipio/{uf}/{municipio}_distribuicao_etnica.png'))
            plt.close()


def plot_distribuicao_etnica_por_uf(df):
    ufs = df['UF'].unique()

    for i, uf in enumerate(ufs):
        df_uf = df[df['UF'] == uf].set_index('municipio')[['branca', 'indigena', 'preta', 'parda', 'amarela']]
        fig, ax = plt.subplots(figsize=(16, 16))
        ax.pie(df_uf.iloc[0], labels=df_uf.columns, autopct='%.2f%%', startangle=0)

        ax.set_title(f'Distribuição Étnica em {uf}')
        plt.legend()

        if not os.path.exists(os.path.join(PLOTS_DIR, 'distribuicao_etnica_UF')):
            os.makedirs(os.path.join(PLOTS_DIR, 'distribuicao_etnica_UF'))

        plt.savefig(os.path.join(PLOTS_DIR, f'distribuicao_etnica_UF/{uf}_distribuicao_etnica.png'))
        plt.close()


def plot_distribuicao_etnica_por_regiao(df):
    regioes = df['regiao'].unique()

    for i, regiao in enumerate(regioes):
        df_regiao = df[df['regiao'] == regiao].set_index('municipio')[['branca', 'indigena', 'preta', 'parda', 'amarela']]
        fig, ax = plt.subplots(figsize=(16, 16))
        ax.pie(df_regiao.iloc[0], labels=df_regiao.columns, autopct='%.2f%%', startangle=0)

        ax.set_title(f'Distribuição Étnica em {regiao}')
        plt.legend()

        if not os.path.exists(os.path.join(PLOTS_DIR, 'distribuicao_etnica_regiao')):
            os.makedirs(os.path.join(PLOTS_DIR, 'distribuicao_etnica_regiao'))

        plt.savefig(os.path.join(PLOTS_DIR, f'distribuicao_etnica_regiao/{regiao}_distribuicao_etnica.png'))
        plt.close()


plot_distribuicao_etnica_por_municipio(df)
plot_distribuicao_etnica_por_uf(df)
plot_distribuicao_etnica_por_regiao(df)
