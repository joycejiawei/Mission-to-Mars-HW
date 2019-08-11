from bs4 import BeautifulSoup 
from splinter import Browser
import pandas as pd 
import requests 
import time


def init_browser():
    executable_path = {"executable_path": "chromedriver.exe"}
    return Browser("chrome", **executable_path, headless=False)


# Mars News
def scrape_mars_news():
        browser = init_browser()

        url = 'https://mars.nasa.gov/news/'
        browser.visit(url)
        time.sleep(2)

        html = browser.html
        soup = BeautifulSoup(html, 'html.parser')

        news_title = soup.find('div', class_='content_title').find('a').text
        news_p = soup.find('div', class_='article_teaser_body').text

        mars_info = {
            "news_title": news_title,
            "news_p": news_p
        }

        browser.quit()

        return mars_info



# Mars Image
def scrape_mars_image():
        browser = init_browser()

        image_url_featured = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
        browser.visit(image_url_featured)
        time.sleep(1)

        html_image = browser.html
        soup = BeautifulSoup(html_image, 'html.parser')

        featured_image_url  = soup.find('article')['style'].replace('background-image: url(','').replace(');', '')[1:-1]
        main_url = 'https://www.jpl.nasa.gov'
        featured_image_url = main_url + featured_image_url 
        
        mars_info = {
            "featured_image_url": featured_image_url
        }

        browser.quit()

        return mars_info



        
# Mars Weather
def scrape_mars_weather():
        browser = init_browser()

        weather_url = 'https://twitter.com/marswxreport?lang=en'
        browser.visit(weather_url)
        time.sleep(1)

        html_weather = browser.html
        soup = BeautifulSoup(html_weather, 'html.parser')

        latest_tweets = soup.find_all('div', class_='js-tweet-text-container')
 
        for tweet in latest_tweets: 
            weather_tweet = tweet.find('p').text
            if 'Sol' and 'pressure' in weather_tweet:
                print(weather_tweet)
                break
            else: 
                pass

        mars_info = {
            "weather_tweet": weather_tweet
        }

        browser.quit()

        return mars_info
  




# Mars Facts
def scrape_mars_facts():
    facts_url = 'http://space-facts.com/mars/'
    mars_facts = pd.read_html(facts_url)
    mars_df = mars_facts[0]
    mars_df.columns = ['Description','Value','Vaule2']
    mars_df.set_index('Description', inplace=True)
    data = mars_df.to_html()
    mars_info ={
        "mars_facts": mars_facts
    }
    return mars_info


# Mars Hemisphere 
def scrape_mars_hemispheres():
        browser = init_browser()

        hemispheres_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
        browser.visit(hemispheres_url)
        time.sleep(1)

        html_hemispheres = browser.html
        soup = BeautifulSoup(html_hemispheres, 'html.parser')

        items = soup.find_all('div', class_='item')
        hiu = []
        hemispheres_main_url = 'https://astrogeology.usgs.gov' 

        for i in items: 
            title = i.find('h3').text
            partial_img_url = i.find('a', class_='itemLink product-item')['href']            
            browser.visit(hemispheres_main_url + partial_img_url)           
            partial_img_html = browser.html           
            soup = BeautifulSoup( partial_img_html, 'html.parser')            
            img_url = hemispheres_main_url + soup.find('img', class_='wide-image')['src']            
            hiu.append({"title" : title, "img_url" : img_url})

        mars_info = {
            "hiu": hiu
        }
        
        browser.quit()
        
        return mars_info


