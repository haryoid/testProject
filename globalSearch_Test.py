from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time

url = "https://staging-web.spacestock.com/"

def setup():
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)

def switchBeli():
    print("====Test button Beli====")
    btn_beli = driver.find_element_by_xpath("//*[@id='root']/div/div/div[3]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div[2]/label/span[3]")
    print("button beli is displayed: ", btn_beli.is_displayed())
    if btn_beli.is_enabled():
        pass
    else:
        btn_beli.click()
    print("button beli is enable: ", btn_beli.is_enabled())
    btn_aktif = driver.find_element(By.XPATH, "//*[@id='root']/div/div/div[3]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div[2]/label/span[2]").text
    print("button atif = beli", btn_aktif == "Beli")

def switchSewa():
    print("====Test button sewa====")
    btn_sewa = driver.find_element_by_xpath("//*[@id='root']/div/div/div[3]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div[2]/label/span[1]")
    print("button sewa is displayed :",btn_sewa.is_displayed())
    btn_sewa.click()
    print("button sewa is enable :", btn_sewa.is_enabled())
    btn_aktif = driver.find_element(By.XPATH, "//*[@id='root']/div/div/div[3]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div[2]/label/span[2]").text
    print("button atif = sewa", btn_aktif == "Sewa")

def aptSelect():                #dropdown building type >> pilih apartemen
    tipeBangunan = driver.find_element(By.XPATH, "//*[@id='root']/div/div/div[3]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div/select")
    pilihApartemen = Select(tipeBangunan)
    pilihApartemen.select_by_value("apartment")
    plh = driver.find_element(By.CSS_SELECTOR, "option[value=apartment]")
    print("pilih Apartemen: ", plh.is_selected())

def houseSelect():              # dropdown building type >> pilih house
    tipeBangunan = driver.find_element(By.XPATH, "//*[@id='root']/div/div/div[3]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div/select")
    pilihRumah = Select(tipeBangunan)
    pilihRumah.select_by_value("house")
    plh = driver.find_element(By.CSS_SELECTOR, "option[value=house]")
    print("pilih Rumah: ", plh.is_selected())

def officeSelect():             # dropdown building type >> pilih house
    tipeBangunan = driver.find_element(By.XPATH, "//*[@id='root']/div/div/div[3]/div[1]/div[2]/div[2]/div/div[2]/div[1]/div[1]/div[2]/div/select")
    pilihKantor = Select(tipeBangunan)
    pilihKantor.select_by_value("office")
    plh = driver.find_element(By.CSS_SELECTOR, "option[value=office]")
    print("pilih Kantor: ", plh.is_selected())


if __name__ == '__main__':
    setup()
    switchBeli()
    switchSewa()
    officeSelect(), houseSelect(), aptSelect()
    driver.close()

