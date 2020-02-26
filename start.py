from selenium import webdriver
import requests

url = "https://spacestock.com/cari-apartemen?listingType=buy&buildingType=apartment"

driver = webdriver.Chrome()
driver.get(url) # Akses Site

switch_buy = driver.find_element_by_xpath("//*[@id='root']/div/div/div[3]/div[1]/div/div/div[2]/div/div[3]/label/span[2]")
print(driver.current_url)
print("SRP sw Buy displayed: ", switch_buy.is_displayed())
print("SRP sw Buy enabled: ", switch_buy.is_enabled())

switch_rent = driver.find_element_by_xpath("//*[@id='root']/div/div/div[3]/div[1]/div/div/div[2]/div/div[3]/label/span[1]")
print("SRP sw Rent displayed: ", switch_rent.is_displayed())
switch_rent.click()
print("SRP sw Buy enabled: ", switch_rent.is_enabled())
driver.implicitly_wait(5) # beri waktu untuk loading
print(driver.current_url)

driver.close()


#API Test

def cekStatus(url):
    
    if req.status_code == 200:
        print(req.headers)
        print("Status code :", req.status_code)
    else:
        print(req.raise_for_status())

#cekStatus(url)

try:
    req = requests.get(url)
    print("Status Code: ",req.status_code)
    req.raise_for_status()
except requests.exceptions.HTTPError as e:  # This is the correct syntax
    print(e)
