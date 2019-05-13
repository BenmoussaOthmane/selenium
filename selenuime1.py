from selenium import webdriver as wb 



driver = wb.Chrome('/Users/benmoussaothmane/Downloads/chromedriver')

driver.get('https://www.amazon.fr/s?k=imac&__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss_2')

source = driver.page_source
# div = driver.find_elements_by_xpath("""//*[@class="a-section"]""").click()


p = driver.find_elements_by_class_name('a-price-whole')
t = driver.find_elements_by_class_name('a-color-price')
num_page = len(p)



for i in range(num_page):
    print(p[i].text + "      " + t[i].text)


driver.close()