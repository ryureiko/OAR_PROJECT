import pandas as pd
import json

url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vR65QfL_G-1ZFoL1GWCuuJ11LJpj0rruC-6eoJLVIgFB0ldeXpm5pLF9Oag0SuGo8rczIZaVQ11nIWQ/pub?gid=1198489169&single=true&output=csv'

df = pd.read_csv(url, delimiter=',')

# Обработка данных
df['num_economactivepopulation_all'] = df['num_economactivepopulation_all'].str.replace(',', '.').astype(float)
df['year'] = df['year'].astype(int)

# Преобразование остальных числовых колонок
numerical_columns = [
    'employed_num_all', 'unemployed_num_all', 'eactivity_lvl', 'employment_lvl', 'unemployment_lvl',
    'dis_unagegroup_to20', 'dis_unagegroup_20-29', 'dis_unagegroup_30-39', 'dis_unagegroup_40-49',
    'dis_unagegroup_50-59', 'dis_unagegroup_60older', 'dis_emagegroup_to20', 'dis_emagegroup_20-29',
    'dis_emagegroup_30-39', 'dis_emagegroup_40-49', 'dis_emagegroup_50-59', 'dis_emagegroup_60older',
    'num_unagegroup_to20', 'num_unagegroup_20-29', 'num_unagegroup_30-39', 'num_unagegroup_40-49',
    'num_unagegroup_50-59', 'num_unagegroup_60older', 'num_emagegroup_to20', 'num_emagegroup_20-29',
    'num_emagegroup_30-39', 'num_emagegroup_40-49', 'num_emagegroup_50-59', 'num_emagegroup_60older'
]

for column in numerical_columns:
    df[column] = df[column].str.replace(',', '.').astype(float)

df_region = pd.read_csv('data/dataset_data.csv',
                sep=',', decimal=',', )

# Загрузка географических данных (GeoJSON для карты России)
with open('data/russia copy.geojson', 'r', encoding='UTF-8') as response:
    counties = json.load(response)