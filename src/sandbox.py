import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

DATASETS_DIR = os.path.join(os.path.dirname(__file__), '..', 'datasets')
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), '..', 'outputs')
PLOTS_DIR = os.path.join(OUTPUT_DIR, 'plots')

dataset_name = 'p_Tabela_04_Pop_resid_por_cor_ou_raca_e_pessoas_indigenas_2022_MU.csv'
DATASET_FILE = os.path.join(DATASETS_DIR, dataset_name)

df = pd.read_csv(DATASET_FILE)