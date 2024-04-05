import requests
from bs4 import BeautifulSoup
import time
import pandas as pd



DWARF_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

browser = webdriver.Chorome("D:/Setup/chromedriver_win32/chromedriver.exe")
browser.get(DWARF_URL)

time.sleep(10)

new_planets_data =[]

def scrape_more_data(hyperlink):
    print(hyperlink)

    try:
        page = requests.get(hyperlink)

        soup = BeautifulSoup(page.content,"html,parser")

        temp_list= []

        for tr_tag in soup.find_all("tr",attrs={"class": "fact_row"}):
            td_tag - tr_tag.find_all("td")

            for td_tag in td_tag:
                try: 
                    temp_list.append(td_tag.find_all)
                    
                    new_planets_data.append(temp_list)
         
    except: 
        temp_list.append("")

    new_planets_data.append(temp_list)

    except:
    time.sleep(1)
    scrape_more_data(hyperlink)

planet_df_1 = pd.read_csv("updated_scraped_data.csv")

or index, row in planet_df_1.iterrows():

     ## ADD CODE HERE ##
     print(row['hyperlink'])
     scrape_more_data(row["hyperlink"])
     # Call scrape_more_data(<hyperlink>)

     print(f"Data Scraping at hyperlink {index+1} completed")

print(new_planets_data)

# Remove '\n' character from the scraped data
scraped_data = []

for row in new_planets_data:
    replaced = []
    ## ADD CODE HERE ##
    
    for row  in new_planets_data:
        replaced =[]
        for el in row:
            el = el.replace("\n","")
            replaced.append(el)
        scraped_data.append(replaced)  

    
    scraped_data.append(replaced)

print(scraped_data)

headers = ["planet_type","discovery_date", "mass", "planet_radius", "orbital_radius", "orbital_period", "eccentricity", "detection_method"]

new_planet_df_1 = pd.DataFrame(scrapped_data,columns = headers)

# Convert to CSV

new_planet_df_1.to_csv('new_scraped_data.csv', index=True, index_label="id")
