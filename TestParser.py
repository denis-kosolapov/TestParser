# olx.pl test selenium

from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By

options = Options()
options.set_preference('javascript.enabled', False)

options.add_argument("--headless")
service = FirefoxService(executable_path=GeckoDriverManager().install(), log_output=True)
driver = webdriver.Firefox(service=service, options=options)

driver.get("https://www.olx.pl")
# button = driver.find_element(By.XPATH, '/html/body/div/section[1]/div[2]/div/div[1]/div[6]/div/a').click()
button = driver.find_element(By.LINK_TEXT, "Moda").click()
content = driver.find_element(By.XPATH, "//div[@data-testid='listing-grid']")
get_child_elements = content.find_elements(By.TAG_NAME, 'h6')

products = []

for child in get_child_elements:
    products.append(child.text)

pagination_list = driver.find_element(By.CLASS_NAME, "pagination-list")
pagination_list_li = pagination_list.find_elements(By.TAG_NAME, "li")
count_pages = int(pagination_list_li[len(pagination_list_li) - 1].text)

for page_number in range(count_pages):
    if len(products) < 150:
        driver.get(driver.current_url + f"/?page={page_number}")
        content = driver.find_element(By.XPATH, "//div[@data-testid='listing-grid']")
        get_child_elements = content.find_elements(By.TAG_NAME, 'h6')
        for child in get_child_elements:
            if len(products) == 150:
                break
            products.append(child.text)

print(f"\n Список заголовков товаров, всего наименований {len(products)} \n")
for prod in products:
    print(prod)
