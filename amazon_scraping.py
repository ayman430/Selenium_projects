from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import pandas as pd
import time

mobile_name = []
m_img = []
url = []
m_price = []
details = []
mobile_num = 1
page_number = 1
web = webdriver.Chrome()
web.get("https://www.amazon.eg/s?i=electronics&rh=n%3A21832883031&fs=true&page=1")

web.find_element(By.ID, "icp-nav-flyout").click()
web.find_element(By.ID, "icp-language-translation-hint").click()
web.find_element(By.ID, "icp-save-button").click()
time.sleep(5)

names = web.find_elements(By.XPATH,
                          '//*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]/div/div/div/div/div/div/div/h2/a/span')
images = web.find_elements(By.CLASS_NAME, "s-image")
links = web.find_elements(By.XPATH, '//*[@id="search"]/div[1]/div[1]/div/span[3]/div[2]/div/div/div/div/div/div/span/a')

for i in range(len(names)):
    mobile_name.append(names[i].text)
    m_img.append(images[i].get_dom_attribute('src'))
    url.append("https://www.amazon.eg" + links[i].get_dom_attribute('href'))

for x in url:
    web.get(x)
    time.sleep(2)
    if len(web.find_elements(By.XPATH, '//p[@class="a-text-left a-size-base"]')) > 0:
        web.find_elements(By.XPATH, '//p[@class="a-text-left a-size-base"]')[1].click()
        time.sleep(2)
        price = web.find_element(By.XPATH, '//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span/span[2]/span[2]')
        m_price.append(price.text)

    else:
            try:
                price = web.find_element(By.XPATH, '//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span/span[2]/span[2]')
                m_price.append(price.text)

            except NoSuchElementException:
                m_price.append("no price exist you can check website")

    details.append(web.find_element(By.XPATH, '//table[@class="a-normal a-spacing-micro"]').text)
    print(f"{mobile_num} is done")
    mobile_num += 1
print(len(m_price))
df = pd.DataFrame({"Mobile image": m_img, "Mobile name": mobile_name, "Mobile price": m_price,"Details": details, "Mobile url": url})
df.to_csv("amazon.csv", index=False)
print("process is done")
web.close()
