import pandas as pd

# filtering all olympic data into one dataset with each
# country's total number of medals for the 5k, 10k, and marathon

df_all = pd.read_csv('/Users/aidendeffner/Desktop/cs/final project/data/olympics data/athlete_events.csv')
df_nations = pd.read_csv('/Users/aidendeffner/Desktop/cs/final project/data/olympics data/noc_regions.csv')
df_all.dropna(axis=0, inplace=True)
df_all.drop(["Name","Sex","Age","Height","Weight","Team","Games","Year","Season","City","Sport"], axis=1, inplace=True)

# drop every event but 5k, 10k, and marathon
df_long_distance = df_all[(df_all["Event"] == "Athletics Men's Marathon") |
                          (df_all["Event"] == "Athletics Women's Marathon") |
                          (df_all["Event"] == "Athletics Men's 10,000 metres") |
                          (df_all["Event"] == "Athletics Women's 10,000 metres") |
                          (df_all["Event"] == "Athletics Men's 5,000 metres") |
                          (df_all["Event"] == "Athletics Women's 5,000 metres")]

df_long_distance.reset_index(drop=True, inplace=True)
df_long_distance.drop(["ID", "Medal"], axis=1, inplace=True)

df_num_medals = df_long_distance.groupby(df_long_distance.columns.tolist(),as_index=False).size()
df_num_medals_f = pd.DataFrame()
df_num_medals_f['NOC'] = df_num_medals['NOC'].unique()

# 5k dataset
all_5ks_men = pd.DataFrame()
all_5ks_men['NOC'] = df_num_medals.loc[df_num_medals['Event'] == "Athletics Men's 5,000 metres", 'NOC']
all_5ks_men['num_5ks_men'] = df_num_medals.loc[df_num_medals['Event'] == "Athletics Men's 5,000 metres", 'size']
all_5ks_men.reset_index(drop=True,inplace=True)
all_5ks_women = pd.DataFrame()
all_5ks_women['NOC'] = df_num_medals.loc[df_num_medals['Event'] == "Athletics Women's 5,000 metres", 'NOC']
all_5ks_women['num_5ks_women'] = df_num_medals.loc[df_num_medals['Event'] == "Athletics Women's 5,000 metres", 'size']
all_5ks_women.reset_index(drop=True,inplace=True)
all_5ks = pd.DataFrame()
all_5ks = pd.merge(all_5ks_men, all_5ks_women, how='outer', on='NOC')
all_5ks.fillna(0,inplace=True)
all_5ks['5k_medals'] = all_5ks['num_5ks_men'] + all_5ks['num_5ks_women']
all_5ks.drop(['num_5ks_men', 'num_5ks_women'],inplace=True,axis=1)

# 10k dataset
all_10ks_men = pd.DataFrame()
all_10ks_men['NOC'] = df_num_medals.loc[df_num_medals['Event'] == "Athletics Men's 10,000 metres", 'NOC']
all_10ks_men['num_10ks_men'] = df_num_medals.loc[df_num_medals['Event'] == "Athletics Men's 10,000 metres", 'size']
all_10ks_men.reset_index(drop=True,inplace=True)
all_10ks_women = pd.DataFrame()
all_10ks_women['NOC'] = df_num_medals.loc[df_num_medals['Event'] == "Athletics Women's 10,000 metres", 'NOC']
all_10ks_women['num_10ks_women'] = df_num_medals.loc[df_num_medals['Event'] == "Athletics Women's 10,000 metres", 'size']
all_10ks_women.reset_index(drop=True,inplace=True)
all_10ks = pd.DataFrame()
all_10ks = pd.merge(all_10ks_men, all_10ks_women, how='outer', on='NOC')
all_10ks.fillna(0,inplace=True)
all_10ks['10k_medals'] = all_10ks['num_10ks_men'] + all_10ks['num_10ks_women']
all_10ks.drop(['num_10ks_men', 'num_10ks_women'],inplace=True,axis=1)

# marathon dataset
all_marathons_men = pd.DataFrame()
all_marathons_men['NOC'] = df_num_medals.loc[df_num_medals['Event'] == "Athletics Men's Marathon", 'NOC']
all_marathons_men['num_marathons_men'] = df_num_medals.loc[df_num_medals['Event'] == "Athletics Men's Marathon", 'size']
all_marathons_men.reset_index(drop=True,inplace=True)
all_marathons_women = pd.DataFrame()
all_marathons_women['NOC'] = df_num_medals.loc[df_num_medals['Event'] == "Athletics Women's Marathon", 'NOC']
all_marathons_women['num_marathons_women'] = df_num_medals.loc[df_num_medals['Event'] == "Athletics Women's Marathon", 'size']
all_marathons_women.reset_index(drop=True,inplace=True)
all_marathons = pd.DataFrame()
all_marathons = pd.merge(all_marathons_men, all_marathons_women, how='outer', on='NOC')
all_marathons.fillna(0,inplace=True)
all_marathons['marathon_medals'] = all_marathons['num_marathons_men'] + all_marathons['num_marathons_women']
all_marathons.drop(['num_marathons_men', 'num_marathons_women'],inplace=True,axis=1)

# merge 5k, 10k, and marathon datasets
df_num_medals_f = pd.merge(all_5ks, all_10ks, how='outer',on='NOC')
df_num_medals_f = pd.merge(df_num_medals_f, all_marathons, how='outer',on='NOC')
df_num_medals_f.fillna(0,inplace=True)
df_num_medals_f = df_num_medals_f.astype({'5k_medals':'int','10k_medals':'int','marathon_medals':'int'})

df_noc_regions = pd.read_csv('noc_regions.csv')
df_num_medals_f = pd.merge(df_num_medals_f, df_noc_regions, how='inner', on='NOC')
df_num_medals_f.drop(['NOC', 'notes'],axis=1,inplace=True)

df_num_medals_f.at[41, 'region'] = 'Yugoslavia'
df_num_medals_f = df_num_medals_f.groupby(['region']).sum()
# create new csv file will final medal data
#df_num_medals_f.to_csv('total_country_medals.csv')
