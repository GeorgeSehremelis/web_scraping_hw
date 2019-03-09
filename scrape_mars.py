from bs4 import BeautifulSoup
import requests
import pandas as pd


def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": ""}
    return Browser("chrome", **executable_path, headless=False)



def mars_scraper: 

    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    results = soup.find_all('div', class_="slide")
    #print(results)

    for result in results:
    # Error handling
    try:
        
        title = result.find_all('img', class_="img-lazy")
        
      
        paragraph = result.find_all('div', class_="rollover_description_inner")
        

        # Print results only if title, price, and link are available
        if (title and paragraph):
            
            print(title)
            print(paragraph)
           
    except AttributeError as e:
        print(e)


def image_scraper: 
    featured_image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    response2 = requests.get(featured_image_url)

    soup2 = BeautifulSoup(response2.text, 'lxml')
    #print(soup2.prettify())
    results2 = soup2.find_all('div', class_="img")
    #print(results2)
def weather_scraper: 
    mars_weather_url = "https://twitter.com/marswxreport?lang=en"
    tables = pd.read_html(mars_weather_url)
    tables
    #not 100%% sure what to do here, not sure if this is right or not

def mars_hemisphere_scraper:
    mars_hemispheres = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    response3 = requests.get(mars_hemispheres)

    soup3 = BeautifulSoup(response3.text, 'lxml')
    #print(soup3.prettify())

    #image scraper
    results3 = soup3.find_all('img', class_="thumb")
    #print(results2)

    #title scraper
    results4 = soup3.find_all('div', class_ = "description").find_all('h3')
    #print(results4)

#getting an error