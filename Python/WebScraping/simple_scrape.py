import requests, json
from bs4 import BeautifulSoup

def scrape_website():
    url = "https://www.scrapethissite.com/pages/simple/"
    
    response = requests.get(url)
    
    if response.status_code != 200:
        print(f"Error. Response code is {response.status_code}")
        return
    
    page = BeautifulSoup(response.text, 'html.parser')
    
    country_divs = page.find_all(class_="col-md-4 country")
    
    data = []
    for country_div in country_divs:
        country_name = country_div.find("h3").get_text().strip()
        capital = country_div.find(class_="country-capital").get_text()
        population = country_div.find(class_="country-population").get_text()
        area = country_div.find(class_="country-area").get_text()
        
        data.append(
            {
                "country_name": country_name,
                "capital": capital,
                "population": population,
                "area": area
            }
        )
        
    with open("countries.json", "w") as file:
        json.dump(data, file, indent=4)
    
if __name__ == "__main__":
    scrape_website()