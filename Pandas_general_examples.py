####Python pandas example script#####
####DataFrame object####
#####################################


import pandas as pd  ## "as pd" part optional
import pylab
from pandas import *
from pylab import *

names = read.csv('') ### read in as dataframe
fixed_df = pd.read_csv('../data/bikes.csv', sep=';', encoding='latin1', parse_dates=['Date'], dayfirst=True, index_col='Date')
fixed_df[:3]
names.head () / names.tail ()

#slice by row and column
names.ix [3:9, ['year', 'name']]
names ['sex'] == 'girl'
girl_names = names[names['sex'] == 'girl']
noise_complaints = complaints[complaints['Complaint Type'] == "Noise - Street/Sidewalk"]


mary = mary.ix[0:, ['year', 'prop']]  #'year', 'prop' are columns
mary = mary.set_index(['year'])

names['height'].plot(kind = 'bar')


#type in the dataframe name, gives out a summary
names['height']

complaints['complaint type'][:5]
complaints['Complaint Type'].value_counts()
complaints[is_noise & in_brooklyn][['Complaint Type', 'Borough', 'Created Date', 'Descriptor']][:10]
noise_complaints['Borough'].value_counts()

# pandas select columns by numbers
newdf = df[df.columns[2:4]]


berri_bikes['weekday'] = berri_bikes.index.weekday
weekday_counts = berri_bikes.groupby('weekday').aggregate(sum)

weekday_counts.index = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

weather_mar2012.columns = [s.replace(u'\xb0', '') for s in weather_mar2012.columns] ## replace

weather_mar2012 = weather_mar2012.dropna(axis=1, how='any')  ### axis = 1 to "dropna" means "drop columns, not rows"  ##'any' means "drop the column is any value is null


### concatenate
weather_2012 = pd.concat(data_by_month)
subse
### save the data
weather_2012.to_csv('../data/weather_2012.csv)


### clean-up messy data
na_values = ['NO CLUE', 'N/A', '0']
requests = pd.read_csv('../data/311-service-requests.csv', na_values=na_values, dtype={'Incident Zip': str})

### string manipulation
weather_description = weather_2012['Weather']
is_snowing = weather_description.str.contains('Snow')

stats = pd.concat([temperature, snowiness], axis=1) *********
rows_with_dashes = requests['Incident Zip'].str.contains('-').fillna(False)







