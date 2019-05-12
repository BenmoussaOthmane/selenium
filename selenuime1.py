from selenium import webdriver as wb 



driver = wb.Chrome('/Users/benmoussaothmane/Downloads/chromedriver')

driver.get('https://www.amazon.fr/s?k=imac&__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss_2')

source = driver.page_source

div  = driver.find_element_by_class_name('s-include-content-margin')
print(len(div))