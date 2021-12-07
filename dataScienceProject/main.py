import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('data/final_data.csv')
medals_5k = df['5k_medals']
medals_10k = df['10k_medals']
medals_marathon = df['marathon_medals']

elev = df['elev_ft']
temp = df['tempF']
df['temp_to_elev'] = df['tempF']/df['elev_ft']
df['temp_times_elev'] = df['tempF']*df['elev_ft']

# Pie plots of medals per country
colors = sns.color_palette('pastel')[0:5]
nonzero_m = df[df['marathon_medals'] != 0]
nonzero_5k = df[df['5k_medals'] != 0]
nonzero_10k = df[df['10k_medals'] != 0]
total = pd.DataFrame()
total['country'] = df['country']
total['total_medals'] = df['5k_medals']+df['10k_medals']+df['marathon_medals']
print(total)
plt.pie(nonzero_5k['5k_medals'], colors=colors, labels=nonzero_5k['country'], autopct=lambda p: '{:.0f}'.format(p * nonzero_5k.shape[0]/29.2),normalize=True)
plt.title('5,000 Meter Medals by Country')
plt.tight_layout()
plt.show()

plt.pie(nonzero_10k['10k_medals'], colors = colors, labels=nonzero_10k['country'], autopct=lambda p: '{:.0f}'.format(p * nonzero_10k.shape[0]/22.3),normalize=True)
plt.title('10,000 Meter Medals by Country')
plt.tight_layout()
plt.show()

plt.pie(nonzero_m['marathon_medals'], colors = colors, labels=nonzero_m['country'], autopct=lambda p: '{:.0f}'.format(p * nonzero_m.shape[0]/32.6),normalize=True)
plt.title('Marathon Medals by Country')
plt.tight_layout()
plt.show()

# total medals per country
plt.pie(total['total_medals'], colors = colors, labels=total['country'], autopct=lambda p: '{:.0f}'.format(p * total.shape[0]/14.6),normalize=True)
plt.title('Total Medals by Country')
plt.tight_layout()
plt.show()

# medals vs population
plt.scatter(df['pop'], total['total_medals'])
plt.title('Total Medals vs. Population')
plt.xlabel('Population (in billions)')
plt.ylabel('Total Medals')
plt.grid(alpha=0.3)
plt.minorticks_on()
plt.show()
plt.scatter(df['pop'], df['5k_medals'])
plt.scatter(df['pop'], df['10k_medals'])
plt.scatter(df['pop'], df['marathon_medals'])
plt.title('Medals (All Events) vs. Population')
plt.xlabel('Population (in billions)')
plt.ylabel('Medals')
races = ['5,000 Meters', '10,000 Meters', 'Marathon']
plt.legend(races)
plt.grid(alpha=0.3)
plt.minorticks_on()
plt.show()
# correlation
#print(total['total_medals'].corr(df['pop']))

# medals per person
#plt.pie(nonzero_5k['5k_medals_per_person'], colors = colors, labels=nonzero_5k['country'], normalize=True)
#plt.title('5,000 Meter Medals')
#plt.tight_layout()
#plt.show()
#plt.pie(nonzero_10k['10k_medals_per_person'], colors = colors, labels=nonzero_10k['country'], normalize=True)
#plt.title('10,000 Meter Medals')
#plt.tight_layout()
#plt.show()
#plt.pie(nonzero_m['marathon_medals_per_person'], colors = colors, labels=nonzero_m['country'], normalize=True)
#plt.title('Marathon Medals')
#plt.tight_layout()
#plt.show()

# weight vs medals
plt.scatter(df['weight_kg'], df['5k_medals'])
plt.scatter(df['weight_kg'], df['10k_medals'])
plt.scatter(df['weight_kg'], df['marathon_medals'])
plt.xlabel('Average Weight of Country (kg)')
plt.ylabel('Medals')
plt.title('Medals (All Events) vs. Weight')
plt.legend(races)
plt.grid(alpha=0.3)
plt.minorticks_on()
plt.show()
plt.scatter(df['weight_kg'], total['total_medals'])
plt.title('Total Medals vs. Weight')
plt.xlabel('Average Weight of Country (kg)')
plt.ylabel('Total Medals')
plt.grid(alpha=0.3)
plt.minorticks_on()
plt.show()

# medals vs number of racing events
plt.scatter(df['num_5ks'], df['5k_medals'])
plt.scatter(df['num_10ks'], df['10k_medals'])
plt.scatter(df['num_marathons'], df['marathon_medals'])
plt.title('Medals (All Events) vs. Number of Racing Events (All Events)')
plt.xlabel('Number of Races')
plt.ylabel('Medals')
plt.legend(races)
plt.grid(alpha=0.3)
plt.minorticks_on()
plt.show()

plt.scatter(df['num_5ks'] + df['num_10ks'] + df['num_marathons'], total['total_medals'])
plt.title('Total Medals vs. Total Number of Racing Events')
plt.xlabel('Total Number of Races')
plt.ylabel('Total Medals')
plt.grid(alpha=0.3)
plt.minorticks_on()
plt.show()
# correlation
#print(total['total_medals'].corr(df['num_5ks'] + df['num_10ks'] + df['num_marathons']))

# medals vs elevation
plt.scatter(df['elev_ft'], df['5k_medals'])
plt.scatter(df['elev_ft'], df['10k_medals'])
plt.scatter(df['elev_ft'], df['marathon_medals'])
plt.title('Medals (All Events) vs. Elevation')
plt.xlabel('Elevation (ft)')
plt.ylabel('Medals')
plt.legend(races)
plt.grid(alpha=0.3)
plt.minorticks_on()
plt.show()
plt.scatter(df['elev_ft'], total['total_medals'])
plt.title('Total Medals vs. Elevation')
plt.xlabel('Elevation (ft)')
plt.ylabel('Total Medals')
plt.grid(alpha=0.3)
plt.minorticks_on()
plt.show()

# average temperature vs medals
plt.scatter(df['tempF'], df['5k_medals'])
plt.scatter(df['tempF'], df['10k_medals'])
plt.scatter(df['tempF'], df['marathon_medals'])
plt.title('Medals (All Events) vs. Average Temperature')
plt.xlabel('Average Temperature (F)')
plt.ylabel('Medals')
plt.legend(races)
plt.grid(alpha=0.3)
plt.minorticks_on()
plt.show()
plt.scatter(df['tempF'], total['total_medals'])
plt.title('Total Medals vs. Average Temperature')
plt.xlabel('Average Temperature (F)')
plt.ylabel('Total Medals')
plt.grid(alpha=0.3)
plt.minorticks_on()
plt.show()

# medals vs gdp
plt.scatter(df['gdpPerCapita'], df['5k_medals'])
plt.scatter(df['gdpPerCapita'], df['10k_medals'])
plt.scatter(df['gdpPerCapita'], df['marathon_medals'])
plt.title('Medals (All Events) vs. GDP Per Capita')
plt.xlabel('GDP Per Capita')
plt.ylabel('Medals')
plt.legend(races)
plt.grid(alpha=0.3)
plt.minorticks_on()
plt.show()

plt.scatter(df['gdpPerCapita'], total['total_medals'])
plt.title('Total Medals vs. GDP Per Capita')
plt.xlabel('GDP Per Capita')
plt.ylabel('Total Medals')
plt.grid(alpha=0.3)
plt.minorticks_on()
plt.show()

# medals vs temp divided by elevation
plt.scatter(df['temp_to_elev'], df['5k_medals'])
plt.scatter(df['temp_to_elev'], df['10k_medals'])
plt.scatter(df['temp_to_elev'], df['marathon_medals'])
plt.title('Medals (All Events) vs. Temperature/Elevation')
plt.xlabel('Temperature (F) Divided by Elevation (ft)')
plt.ylabel('Medals')
plt.legend(races)
plt.grid(alpha=0.3)
plt.minorticks_on()
plt.show()

plt.scatter(df['temp_to_elev'], total['total_medals'])
plt.title('Total Medals vs. Temperature/Elevation')
plt.xlabel('Temperature (F) Divided by Elevation (ft)')
plt.ylabel('Total Medals')
plt.grid(alpha=0.3)
plt.minorticks_on()
plt.show()
