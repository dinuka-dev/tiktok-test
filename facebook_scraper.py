import time, requests, json, csv, os
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""

def timeCheck(input_string):
    allowed_times = ['second', 'seconds', 'minute', 'minutes', 'hour', 'hours', 'day', 'days', 'week', 'weeks']
    
    input_string_lower = input_string.lower()

    return any(word.lower() in input_string_lower for word in allowed_times)

def getTitleAndPrice(soup):
    title_el = soup.find('h1')
    title = title_el.text
    print(f"Title: {title}")
    
    title_parent = title_el.parent.parent
    price_el = title_parent.find(name='div', class_='x1xmf6yo')
    price = price_el.text
    print(f"Price: {price}")
    return {'title': title, 'price': price}
    
def getIconicData(soup):
    miles_raw_text = ""
    css_icons = soup.find_all('i', {'data-visualcompletion': 'css-img'})
    for icon in css_icons:
        icon_styles = icon['style']
        if ('background-position:0 -63px' in icon_styles):
            # print("Found The Icon")
            milage_icon_parent = icon.parent
            milage_icon_sec_parent = milage_icon_parent.parent
            
            miles_el = milage_icon_sec_parent.find('span')
            miles_raw_text = miles_el.text
            return miles_raw_text
        
    return miles_raw_text

def getSellerDetails(soup):
    seller_elements = soup.select('a[href*=profile]')
    seller = {'name': '', 'contact': ''}
    for el in seller_elements:
        el_text = el.text
        if ('Seller details' not in el_text):
            seller_name = el_text
            seller_profile_link = el['href']
            seller_id = find_between(seller_profile_link, '/profile/', '/')
            contact_link = f'https://www.facebook.com/messages/t/{seller_id}'
            seller['name'] = seller_name
            seller['contact'] = contact_link
    
    print(f"Seller: {seller_name}")
    print(f"Contact: {contact_link}")
    return seller
    
def initBrowser():  
    browser_dir = os.getcwd() + '\\session'
    options = Options()
    options.add_argument(f"--user-data-dir={browser_dir}")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.set_window_size(1600, 900)
    driver.get('https://www.facebook.com/marketplace/category/vehicles?maxMileage=1000000&maxYear=2023&minMileage=1&minYear=2017&sortBy=creation_time_descend&exact=false')
    wait = WebDriverWait(driver, 60)
    return driver

def scrapeSearchResult(driver):
    main_tab = driver.window_handles[0]
    driver.execute_script("window.open('about:blank', 'tab2');")
    sec_tab = driver.window_handles[1]

    driver.switch_to.window(main_tab)

    time.sleep(5)

    for _ in range(1, 20):
        element = driver.find_element(By.CSS_SELECTOR, 'div.x1xfsgkm.xqmdsaz.x1cnzs8.x1mtsufr.x1w9j1nh')
        element_html = element.get_attribute('innerHTML')
        soup = BeautifulSoup(element_html, 'html.parser')
        all_links = soup.find_all('a')
        
        links = []
        for link in all_links:
            the_link = link['href']
            listing_id = find_between(the_link, 'item/', '/')
            clean_link = f"https://www.facebook.com/marketplace/item/{listing_id}"
            links.append(clean_link)
            
        print(f"Listing Count: {len(all_links)}")
        
        last_link = links[-1]
        
        driver.switch_to.window(sec_tab)
        driver.get(last_link)
        
        time_element = driver.find_element(By.CSS_SELECTOR, 'span.x193iq5w.xeuugli.x13faqbe.x1vvkbs.x1xmvt09.x1lliihq.x1s928wv.xhkezso.x1gmr53x.x1cpjm7i.x1fgarty.x1943h6x.x4zkp8e.x676frb.x1nxh6w3.x1sibtaa.xo1l8bm.xi81zsa')
        time_raw_text = time_element.get_attribute('innerText')
        
        print(time_raw_text)
        isItGood = timeCheck(time_raw_text)
        
        if (isItGood == False):
            return links
        
        time.sleep(2)
        driver.switch_to.window(main_tab)
        
        html = driver.find_element(By.TAG_NAME, 'html')
        html.send_keys(Keys.END)
        time.sleep(5)


def getListingDetails(driver, link):
    driver.get(link)
    wait = WebDriverWait(driver, 30)
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'span.x193iq5w.xeuugli.x13faqbe.x1vvkbs.x1xmvt09.x1lliihq.x1s928wv.xhkezso.x1gmr53x.x1cpjm7i.x1fgarty.x1943h6x.x4zkp8e.x676frb.x1nxh6w3.x1sibtaa.xo1l8bm.xi81zsa')))
    
    time_element = driver.find_element(By.CSS_SELECTOR, 'span.x193iq5w.xeuugli.x13faqbe.x1vvkbs.x1xmvt09.x1lliihq.x1s928wv.xhkezso.x1gmr53x.x1cpjm7i.x1fgarty.x1943h6x.x4zkp8e.x676frb.x1nxh6w3.x1sibtaa.xo1l8bm.xi81zsa')
    time_raw_text = time_element.get_attribute('innerText')
    print(time_raw_text)
    isItGood = timeCheck(time_raw_text)
    if (isItGood == False):
        return None
    
    sidebar_parent = driver.find_element(By.CSS_SELECTOR, 'div.xckqwgs.x26u7qi.x2j4hbs.x78zum5.xnp8db0.x5yr21d.x1n2onr6.xh8yej3.xzepove.x1stjdt1')
    element_html = sidebar_parent.get_attribute('innerHTML')
    soup = BeautifulSoup(element_html, 'html.parser')
    titleAndPrice = getTitleAndPrice(soup)
    sellerDetails = getSellerDetails(soup)
    millage = getIconicData(soup)
    
    try:
        description_parent = sidebar_parent.find_element(By.CSS_SELECTOR, 'div.xz9dl7a.x4uap5.xsag5q8.xkhd6sd.x126k92a')
        description_el = description_parent.find_element(By.CSS_SELECTOR, 'span.x193iq5w.xeuugli.x13faqbe')
        try:
            see_more = description_el.find_element(By.CSS_SELECTOR, 'span.x193iq5w.xeuugli.x13faqbe')
            see_more.click()
            time.sleep(1)
        except:
            # print("No See More Button!")
            pass
        
        description_raw_text = description_el.get_attribute('innerText')
        description = description_raw_text.replace('See less', '')
        description = description.strip()
        
    except:
        description = ""
        
    print(description)
    
    image_elements = driver.find_elements(By.CSS_SELECTOR, 'img.x5yr21d.xl1xv1r.xh8yej3')
    images = [elem.get_attribute('src') for elem in image_elements]
    # print(images)



driver.quit()
