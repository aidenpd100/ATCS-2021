import pandas as pd

# final construction and filtering of dataset

df_all_races = pd.read_csv('./races/all_races_per_country.csv')
df_elevations = pd.read_csv('elevations.csv')
df_elevations.drop(['capital', 'elev_m'], axis=1, inplace=True)
df_temps = pd.read_csv('temps.csv')
df_temps.drop('tempC', axis=1, inplace=True)
df_medals = pd.read_csv('olympics data/total_country_medals.csv')
df_pop_and_gdp = pd.read_csv('gdp_and_pop.csv')
df_pop_and_gdp.drop(['rank','imfGDP','unGDP'], axis=1, inplace=True)
df_weight = pd.read_csv('weight/weight.csv')
df_weight = df_weight.iloc[:,[0,1]]
df_weight.drop([0,1,2], inplace=True)
df_weight.rename(columns={"Unnamed: 0": "country", "2016": "weight_kg"}, inplace=True)
df_weight.reset_index(drop=True, inplace=True)
df_weight['weight_kg'] = df_weight['weight_kg'].str.slice(0, 4)

# merging all data into one final dataset
df_final = pd.merge(df_medals, df_all_races, how="inner", on='country')
df_final = pd.merge(df_final, df_elevations, how="inner", on='country')
df_final = pd.merge(df_final, df_temps, how="inner", on='country')
df_final = pd.merge(df_final, df_pop_and_gdp, how="inner", on='country')
df_final = pd.merge(df_final, df_weight, how="inner", on='country')
df_final['5k_medals_per_person'] = df_final['5k_medals'] / df_final['pop']
df_final['10k_medals_per_person'] = df_final['10k_medals'] / df_final['pop']
df_final['marathon_medals_per_person'] = df_final['marathon_medals'] / df_final['pop']
df_final.drop('Unnamed: 0', axis=1, inplace=True)
# create final csv file
#df_final.to_csv('final_data.csv')