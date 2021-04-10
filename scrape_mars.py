from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import time
from webdriver_manager.chrome import ChromeDriverManager

def scrape():
    #setup splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    #set base urls for scraping
    news_url='https://redplanetscience.com/'
    img_url='https://spaceimages-mars.com/'
    facts_url='https://galaxyfacts-mars.com/'
    hemisphere_url='https://marshemispheres.com/'

    #NASA Mars News
    browser.visit(news_url)
    time.sleep(1)
    html = browser.html
    soup = bs(html, "html.parser")

    #Obtaining latest news and paragraph
    news=soup.find('div', id = 'news')
    latest_news_title=news.find('div', class_='content_title').text
    latest_news_par=news.find('div', class_='article_teaser_body').text

    # JPL Mars Space Images - Featured Image
    browser.visit(img_url)
    time.sleep(1)
    html = browser.html
    soup = bs(html, "html.parser")

    browser.links.find_by_partial_text('FULL IMAGE').click()
    #obtaining the url
    images=soup.find_all('img')
    mars_image=images[1]['src']
    featured_image_url=img_url+mars_image
    
    #scrape tables from mars facts url
    tables = pd.read_html(facts_url)
    facts=tables[1]
    
    #converting table to html
    facts_html=facts.to_html(header=False, index=False)
    fact_table=facts_html.replace('\n', '')

    # Mars hemisphere images
    # Gathering the titles and links for each high resolution image
    browser.visit(hemisphere_url)
    time.sleep(1)
    html = browser.html
    soup = bs(html, "html.parser")

    # Getting the soup object that contains each title and link
    # to the page that holds the img url. Creating a list of urls for 
    # the img
    items=soup.find_all('div', class_='item')
    link=[]
    for item in items:
        l=item.find('div', class_='description')
        li=hemisphere_url+l.a['href']
        link.append(li)

    #creating a list to hold the titles an url's for each img
    hemisphere_images=[]
   
    #generating the titles and url's and adding them to the list
    for idx, item in enumerate(items):
        title=item.find('h3').text
        browser.visit(link[idx])
        result= browser.find_by_tag('a')
        img_url= result[3]['href']
        hemisphere_images.append({'title': title, 'img_url': img_url})

   

    scraped_data={
        'latest_news_title' : latest_news_title,
        'latest_news_par' : latest_news_par,
        'featured_image_url' : featured_image_url,
        'fact_table' : fact_table,
        'hemisphere_images' : hemisphere_images
     }

    # Quit the browser after scraping
    browser.quit()

    # Return results
    return scraped_data