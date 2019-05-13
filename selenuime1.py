from selenium import webdriver as wb 
import json


driver = wb.Chrome('/Users/benmoussaothmane/Downloads/chromedriver')

driver.get('https://www.amazon.fr/s?k=imac&__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ref=nb_sb_noss_2')

source = driver.page_source
# div = driver.find_elements_by_xpath("""//*[@class="a-section"]""").click()


p = driver.find_elements_by_class_name('a-price-whole')
t = driver.find_elements_by_class_name('a-color-price')

num_page = len(p)
num_page = len(t)
d = {}
ll = []

for i in p:
    d["price"] = i.text
    ll.append(i.text)

    with open("selenuime.json" , "w") as f:
        f.write(json.dumps(ll , indent = 3 , sort_keys = True))

for j in t:
    d["text"] = j.text
    ll.append(j.text)

    with open("selenuime.json" , "w") as f:
        f.write(json.dumps(ll , indent  =3 , sort_keys = True))


print(ll)
# driver.close()