from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import csv

url = "https://forlap.ristekdikti.go.id/perguruantinggi/search" # Scrape PT
driver = webdriver.Chrome()
driver.get(url)

cap_1 = driver.find_element_by_xpath("//*[@id='searchPtForm']/div[6]/div/input[2]")
cap_2 = driver.find_element_by_xpath("//*[@id='searchPtForm']/div[6]/div/input[3]")
kode_pengaman = int(cap_1.get_attribute("value")) + int(cap_2.get_attribute("value"))
#print(kode_pengaman)
kode_box = driver.find_element_by_xpath("//*[@id='kode_pengaman']").send_keys(kode_pengaman)
kode_btn = driver.find_element_by_xpath("//*[@id='searchPtForm']/div[7]/div/input").click()

driver.implicitly_wait(5)

page = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[1]/div/div/ul/li[3]/a").get_attribute("href")
page = page.split("/")
tot_row = int(page[-1])
rows = len(driver.find_elements_by_xpath("/html/body/div[2]/div[2]/div[2]/div[1]/div/table/tbody/tr"))
cols = len(driver.find_elements_by_xpath("/html/body/div[2]/div[2]/div[2]/div[1]/div/table/tbody/tr[3]/td"))
#print(rows,cols)

with open('perguruanTinggi.csv', 'w') as f:
    for tw in range(0,tot_row,20):
        driver.get(url+"/"+str(tw))
        driver.implicitly_wait(1)
        for r in range(3,rows+1):
            link = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[1]/div/table/tbody/tr[" + str(r) + "]/td[3]/a").get_attribute("href")
            link = link.split()
            values = ""
            for c in range(1,cols+1):
                value = driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[1]/div/table/tbody/tr["+str(r)+"]/td["+str(c)+"]").text
                values += value + ';'
                #print(value,end='     ')
            f.write(values + link[-1]+"\n")
            #print(link)
driver.close()