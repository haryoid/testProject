#script test UI spacestock 
from selenium import webdriver

url = "https://spacestock.com/cari-apartemen?listingType=buy&buildingType=apartment"

def setup():
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url) # Akses Site

def srpSwitch_buy():
    switch_buy = driver.find_element_by_xpath("//*[@id='root']/div/div/div[3]/div[1]/div/div/div[2]/div/div[3]/label/span[2]")
    print(driver.current_url)
    print("SRP sw Buy displayed: ", switch_buy.is_displayed())
    print("SRP sw Buy enabled: ", switch_buy.is_enabled())

def srpSwitch_rent():
    switch_rent = driver.find_element_by_xpath("//*[@id='root']/div/div/div[3]/div[1]/div/div/div[2]/div/div[3]/label/span[1]")
    print("SRP sw Rent displayed: ", switch_rent.is_displayed())
    switch_rent.click()
    print("SRP sw Buy enabled: ", switch_rent.is_enabled())
    driver.implicitly_wait(5) # beri waktu untuk loading
    print(driver.current_url)


def exitTest():
    driver.close()


if __name__ == '__main__':
    setup()
    srpSwitch_buy()
    srpSwitch_rent()
    exitTest()
