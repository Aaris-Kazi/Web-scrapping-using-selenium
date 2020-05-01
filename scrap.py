from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PATH = r'C:\Users\aaris\OneDrive\Desktop\Python\chromedriver.exe'

driver = webdriver.Chrome(PATH)
driver.get('https://www.python.org/')
dev = driver.title
print(dev)

search = driver.find_element_by_id('id-search-field')
search.send_keys('lambda')
search.send_keys(Keys.RETURN)

try:
    article = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "list-recent-events"))
    )
    print(article.text)

    high = driver.find_elements_by_tag_name('p')
    for highlighted in high:
        print(highlighted.text)
except:
    driver.quit()

driver.close