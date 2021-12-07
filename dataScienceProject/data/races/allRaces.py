import pandas as pd

# merging the number of each race into one dataset

df_5ks = pd.read_csv('/Users/aidendeffner/Desktop/ATCS-2021/dataScienceProject/data/races/5ks_per_country.csv')
df_10ks = pd.read_csv('/Users/aidendeffner/Desktop/ATCS-2021/dataScienceProject/data/races/10ks_per_country.csv')
df_marathons = pd.read_csv('/Users/aidendeffner/Desktop/ATCS-2021/dataScienceProject/data/races/marathons_per_country.csv')

df_all_races = pd.merge(df_5ks, df_10ks, how="outer", left_on='country', right_on='country')
df_all_races = pd.merge(df_all_races, df_marathons, how="outer", left_on='country', right_on='country')
df_all_races.fillna(0, inplace=True)
# create csv file with races per country
#df_all_races.to_csv('all_races_per_country.csv')
