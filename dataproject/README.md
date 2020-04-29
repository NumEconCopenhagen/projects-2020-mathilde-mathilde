# Data analysis project

Our project is titled **Cross-country analysis of the Covid-19 outbreak** and is about how different countries are affected by the Covid-19 virus in terms of the number of confirmed cases, recovered cases and deaths.

The **results** of the project can be seen from running [dataproject.ipynb](dataproject.ipynb).

This **loades four datasets**:

1. WPP2019_TotalPopulationBySex.csv downloaded from https://population.un.org/wpp/Download/Standard/CSV/
2. time_series_covid19_confirmed_global.csv downloaded from 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
df_deaths = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv')
df_recovered = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv')
