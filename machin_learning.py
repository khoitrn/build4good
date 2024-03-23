from pandas import read_csv
from scipy import stats
from matplotlib import pyplot as plt
import os 
from notion_client import Client
from pandas import read_csv
from scipy import stats

from matplotlib import pyplot as plt


columns = ['year', 'population', 'co2_including_luc', 'co2_including_luc_growth_prct', 'temperature_change_from_co2', "pacific_CSL", "atlantic_CSL"]
ds_year = read_csv("mle_climate.csv", names=columns, usecols = ['year'])
ds_pop = read_csv("mle_climate.csv", names=columns, usecols = ['population'])
ds_co2 = read_csv("mle_climate.csv", names=columns, usecols = ['co2_including_luc'])
ds_growth = read_csv("mle_climate.csv", names=columns, usecols = ['co2_including_luc_growth_prct'])
ds_temp = read_csv("mle_climate.csv", names=columns, usecols = ['temperature_change_from_co2'])
ds_pacific = read_csv("mle_climate.csv", names=columns, usecols = ['pacific_CSL'])
ds_atlantic = read_csv("mle_climate.csv", names=columns, usecols = ['atlantic_CSL'])

data1 = ds_year.head(11)
data2 = ds_pop.head(11)
data3 = ds_co2.head(11)
data4 = ds_growth.head(11)
data5 = ds_temp.head(11)
data6 = ds_pacific.head(11)
data7 = ds_atlantic.head(11)

year_list= data1["year"].tolist()
pop_list = data2["population"].tolist()
co2_list = data3["co2_including_luc"].tolist()
growth_list = data4["co2_including_luc_growth_prct"].tolist()
temp_list = data5["temperature_change_from_co2"].tolist()
pacific_list = data6["pacific_CSL"].tolist()
atlantic_list = data7["atlantic_CSL"].tolist()


def value(x):
  return slope * x + intercept


# Data 2: Population (Million Tonnes)
slope, intercept, r, p, std_err = stats.linregress(year_list, pop_list)
model2 = list(map(value,year_list))

plt.scatter(year_list, pop_list)
plt.plot(year_list, model2)
plt.xlabel('Year')
plt.ylabel('Population (Million Tonnes)')
plt.show()

# Data 3: CO2 including Land Use Change (Million Tonnes)
slope, intercept, r, p, std_err = stats.linregress(year_list, co2_list)
model3 = list(map(value,year_list))

plt.scatter(year_list, co2_list)
plt.plot(year_list, model3)
plt.xlabel('Year')
plt.ylabel('CO2 with Land Use Change (Million Tonnes)')
plt.show()

# Data 4: CO2 including Land Use Change Growth Percentage (Million Tonnes)
slope, intercept, r, p, std_err = stats.linregress(year_list, growth_list)
model4 = list(map(value,year_list))

plt.scatter(year_list, growth_list)
plt.plot(year_list, model4)
plt.xlabel('Year')
plt.ylabel('CO2 with Land Use Change Growth Percentage (Million Tonnes)')
plt.show()


# Data 5: Temperature Change from CO2 (Celsius)
slope, intercept, r, p, std_err = stats.linregress(year_list, temp_list)
model5 = list(map(value,year_list))

plt.scatter(year_list, temp_list)
plt.plot(year_list, model5)
plt.xlabel('Year')
plt.ylabel('Temperature Change from CO2 (Celsius)')
plt.show()

# Data 6: Pacific Ocean - Change in Mean Sea Level (mm)
plt.bar(year_list, pacific_list)
plt.xlabel('Year')
plt.ylabel('Pacific Ocean: Change in Mean Sea Level (mm)')
plt.show()

# Data 7: Atlantic Ocean - Change in Mean Sea Level (mm)
plt.bar(year_list, atlantic_list)
plt.xlabel('Year')
plt.ylabel('Atlantic Ocean: Change in Mean Sea Level (mm)')
plt.show()



def save_and_upload_plot(data, title, file_name):
    # ... Your plotting logic ...
    plt.savefig(file_name) 

    # Image Upload (Replace with your preferred method)
    with open(file_name, 'rb') as image_file:
        file_object = notion.upload_file(image_file) 
    return file_object["url"]  

# Notion Setup
notion = Client(auth=os.environ["NOTION_API_KEY"]) 
page_id = "your_page_id"

# Generate Images & Update Notion
pop_image_url = save_and_upload_plot(pop_list, "Population (Million Tonnes)", "population.png")
co2_image_url = save_and_upload_plot(co2_list, "CO2 with Land Use Change (Million Tonnes)", "co2.png")
# ... Generate and upload other plots 

# Embed Images into Notion Page
notion.blocks.children.append(page_id, children=[
    {  # Population Section
        "object": "block",
        "type": "image",
        "image": {
            "type": "external",
            "external": {"url": pop_image_url}
        },
    },
    # ... Add similar blocks for other images ...
])
