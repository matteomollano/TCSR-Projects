import requests
from bs4 import BeautifulSoup

def scrape_website():
    # url to scrape
    url = "https://www.footyheadlines.com"

    # send a GET request to the URL
    response = requests.get(url)

    # unsuccessful request
    if response.status_code != 200:
        print(f"Failed to fetch {url}. Status code: {response.status_code}")
        return
    
    # successful request (proceed with beautiful soup code here ...)
    
    # parse the HTML content
    page = BeautifulSoup(response.text, 'html.parser')
    
    # find all elements with the class "post-feed__item" (div class for latest articles)
    latest_article_divs = page.find_all(class_="post-feed__item")

    for article_div in latest_article_divs:
        # print(article_div)
        # print("\n\n")
        
        article_link = "footyheadlines.com" + article_div.find("a").get("href")
        image_url = article_div.find("img").get("data-src")
        article_title = article_div.find("h2").get_text()
        
if __name__ == "__main__":
    scrape_website()