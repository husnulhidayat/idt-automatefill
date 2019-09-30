import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

def inputSekaligus():
    driver = webdriver.Firefox()
    driver.get("https://internship.ddstelkom.id/login")
    driver.find_element_by_id("email-field").send_keys("husnul_hidayat@outlook.com")
    driver.find_element_by_id("password-field").send_keys("c0d31997")
    driver.find_element_by_class_name("button-tosca-login").click()

    year = "2019"
    month = "09"
    day = "07"

    start date =
    end date =

    driver.get("https://internship.ddstelkom.id/internship/detail/2129")
    driver.find_element_by_class_name("button-tosca-tambahaktifitas").click()
    driver.find_element_by_xpath("//input[@id='date']").send_keys(year+"-"+month+"-"+day)
    WebDriverWait(driver, 10000).until(EC.element_to_be_clickable((By.XPATH,'//select[@name="hadir"]//option[text()="Hadir"]'))).click()
    driver.find_element_by_id("masuk").send_keys("08:00")
    driver.find_element_by_id("keluar").send_keys("17:00")
    driver.execute_script("arguments[0].value = arguments[1]", driver.find_element_by_css_selector("textarea.form-control"), "s")
    driver.find_element_by_class_name("button-kirim").click()

def inputDaily():
    driver = webdriver.Firefox()
    driver.get("https://internship.ddstelkom.id/login")
    driver.find_element_by_id("email-field").send_keys("husnul_hidayat@outlook.com")
    driver.find_element_by_id("password-field").send_keys("c0d31997")
    driver.find_element_by_class_name("button-tosca-login").click()

    driver.get("https://internship.ddstelkom.id/internship/detail/2129")
    driver.find_element_by_class_name("button-tosca-tambahaktifitas").click()
    #driver.find_element_by_xpath("//input[@id='date']").send_keys("2019-09-07")
    WebDriverWait(driver, 10000).until(EC.element_to_be_clickable((By.XPATH,'//select[@name="hadir"]//option[text()="Hadir"]'))).click()
    driver.find_element_by_id("masuk").send_keys("08:00")
    driver.find_element_by_id("keluar").send_keys("17:00")
    driver.execute_script("arguments[0].value = arguments[1]", driver.find_element_by_css_selector("textarea.form-control"), aktifitas)
    # driver.find_element_by_class_name("button-kirim").click()
    # driver.close()

def kirimSemua():
    ack = input("apakah kamu yakin? (y/t)")
    if (ack == "y"):
        ack2 = input("konfirmasi sekali lagi: ")
        if (ack2 == "y"):
            driver = webdriver.Firefox()
            driver.get("https://internship.ddstelkom.id/login")
            driver.find_element_by_id("email-field").send_keys("husnul_hidayat@outlook.com")
            driver.find_element_by_id("password-field").send_keys("c0d31997")
            driver.find_element_by_class_name("button-tosca-login").click()
            driver.get("https://internship.ddstelkom.id/daily/707/approve")
            driver.close()
        else:
            print("Kirim gagal")
    else:
        print("Dibatalkan")


if __name__ == '__main__':
    # print("Choose: ")
    # print("====================")
    # print("1. Input IDT")
    # print("2. Kirim semua IDT")
    # pilih = input(": ")
    # if (pilih == "1"):
    #     aktifitas = input("Masukkan Aktifitas Hari Ini: ")
    #     inputDaily()
    # elif (pilih == "2"):
    #     kirimSemua()
    # else:
    #     print("Unknown input")
    #inputDaily()
    inputSekaligus()
#
# if __name__ == '__main__':
#