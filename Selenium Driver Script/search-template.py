from typing import List

from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement

search_term="Cyber Security News"
driver = webdriver.Firefox()
driver.get("https://www.google.com/search?q="+search_term)
i=0

f= open("result.txt","w+")

falsedeger = "www.google.com/"

def list(i):

    gelen= driver.find_elements_by_css_selector('div.g')
    links = gelen[i].find_element_by_tag_name("a")
    href = links.get_attribute("href")
    deneme = driver.find_elements_by_id('center_col')

    if ((href.find(falsedeger))== -1):
        print("Adres : "+href)
        f.write(href+"\n")
        print((href.find(falsedeger)))
        if(i==9):
            next = driver.find_elements_by_link_text("Sonraki")[0].click()
            print("-------------------------------------------------------")
            i=0
            return list(i)
        return list(i+1)


    elif ((href.find(falsedeger))== 8):
        print((href.find(falsedeger)))
        next = driver.find_elements_by_link_text("Sonraki")[0].click()
        i=0
        return list(i)

    else:
        print((href.find(falsedeger)))
        print("hataaaa")
        pass

list(i)

f.close()
