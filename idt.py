import time
import pandas as pd
#from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def inputSekaligus():
    startdate = input("Tanggal Awal (TTTT-BB-HH): ")
    enddate = input("Tanggal Akhir (TTTT-BB-HH): ")
    listdate = pd.date_range(startdate, enddate, freq='B').strftime("%Y-%m-%d").tolist()
    length = len(listdate)
    i = 0

    driver = webdriver.Firefox()
    driver.get("https://internship.ddstelkom.id/login")
    driver.find_element_by_id("email-field").send_keys("#email#")
    driver.find_element_by_id("password-field").send_keys("#password#")
    driver.find_element_by_class_name("button-tosca-login").click()

    while i < length:

        driver.get("https://internship.ddstelkom.id/internship/detail/2129")
        driver.find_element_by_class_name("button-tosca-tambahaktifitas").click()

        driver.find_element_by_xpath("//input[@id='date']").send_keys(listdate[i])
        WebDriverWait(driver, 10000).until(EC.element_to_be_clickable((By.XPATH,'//select[@name="hadir"]//option[text()="Hadir"]'))).click()
        driver.find_element_by_id("masuk").send_keys("08:00")
        driver.find_element_by_id("keluar").send_keys("17:00")
        driver.execute_script("arguments[0].value = arguments[1]", driver.find_element_by_css_selector("textarea.form-control"), aktifitas)
        driver.find_element_by_class_name("button-kirim").click()
        driver.get("https://internship.ddstelkom.id/internship/detail/2129")
        i += 1

def inputSekaligusCustom():
    startdate = input("Tanggal Awal (TTTT-BB-HH): ")
    enddate = input("Tanggal Akhir (TTTT-BB-HH): ")
    listdate = pd.date_range(startdate, enddate, freq='B').strftime("%Y-%m-%d").tolist()
    length = len(listdate)
    i = 0

    driver = webdriver.Firefox()
    driver.get("https://internship.ddstelkom.id/login")
    driver.find_element_by_id("email-field").send_keys("#email#")
    driver.find_element_by_id("password-field").send_keys("#password#")
    driver.find_element_by_class_name("button-tosca-login").click()

    while i < length:
        driver.get("https://internship.ddstelkom.id/internship/detail/2129")
        driver.find_element_by_class_name("button-tosca-tambahaktifitas").click()
        driver.find_element_by_xpath("//input[@id='date']").send_keys(listdate[i])
        WebDriverWait(driver, 10000).until(EC.element_to_be_clickable((By.XPATH,'//select[@name="hadir"]//option[text()="Hadir"]'))).click()
        driver.find_element_by_id("masuk").send_keys("08:00")
        driver.find_element_by_id("keluar").send_keys("17:00")
        tgl = listdate[i]
        print("aktifitas tanggal "+tgl)
        aktifitasC = input("Masukkan Aktifitas: ")
        driver.execute_script("arguments[0].value = arguments[1]", driver.find_element_by_css_selector("textarea.form-control"), aktifitasC)
        driver.find_element_by_class_name("button-kirim").click()
        driver.get("https://internship.ddstelkom.id/internship/detail/2129")
        i += 1

def eidtremove():
    driver = webdriver.Firefox()
    driver.get("https://internship.ddstelkom.id/login")
    driver.find_element_by_id("email-field").send_keys("#email#")
    driver.find_element_by_id("password-field").send_keys("#password#")
    driver.find_element_by_class_name("button-tosca-login").click()
    driver.get("https://internship.ddstelkom.id/internship/detail/2129")

def inputSpesifik():
    driver = webdriver.Firefox()
    driver.get("https://internship.ddstelkom.id/login")
    driver.find_element_by_id("email-field").send_keys("#email#")
    driver.find_element_by_id("password-field").send_keys("#password#")
    driver.find_element_by_class_name("button-tosca-login").click()

    driver.get("https://internship.ddstelkom.id/internship/detail/2129")
    driver.find_element_by_class_name("button-tosca-tambahaktifitas").click()
    driver.find_element_by_xpath("//input[@id='date']").send_keys("2019-"+tanggal)
    WebDriverWait(driver, 10000).until(EC.element_to_be_clickable((By.XPATH,'//select[@name="hadir"]//option[text()="Hadir"]'))).click()
    driver.find_element_by_id("masuk").send_keys("08:00")
    driver.find_element_by_id("keluar").send_keys("17:00")
    driver.execute_script("arguments[0].value = arguments[1]", driver.find_element_by_css_selector("textarea.form-control"), aktifitas)
    driver.find_element_by_class_name("button-kirim").click()
    driver.get("https://internship.ddstelkom.id/internship/detail/2129")
    time.sleep(5)
    driver.close()

def inputDaily():
    driver = webdriver.Firefox()
    driver.get("https://internship.ddstelkom.id/login")
    driver.find_element_by_id("email-field").send_keys("#email#")
    driver.find_element_by_id("password-field").send_keys("#password#")
    driver.find_element_by_class_name("button-tosca-login").click()

    driver.get("https://internship.ddstelkom.id/internship/detail/2129")
    driver.find_element_by_class_name("button-tosca-tambahaktifitas").click()
    #WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='date']"))).click()
    WebDriverWait(driver, 10000).until(EC.element_to_be_clickable((By.XPATH,'//select[@name="hadir"]//option[text()="Hadir"]'))).click()
    driver.find_element_by_id("masuk").send_keys("08:00")
    driver.find_element_by_id("keluar").send_keys("17:00")
    driver.execute_script("arguments[0].value = arguments[1]", driver.find_element_by_css_selector("textarea.form-control"), aktifitas)
    driver.find_element_by_class_name("button-kirim").click()
    driver.get("https://internship.ddstelkom.id/internship/detail/2129")
    time.sleep(5)
    driver.close()

def kirimSemua():
    ack = input("apakah kamu yakin? (y/t)")
    if (ack == "y"):
        ack2 = input("konfirmasi sekali lagi: ")
        if (ack2 == "y"):
            driver = webdriver.Firefox()
            driver.get("https://internship.ddstelkom.id/login")
            driver.find_element_by_id("email-field").send_keys("#email#")
            driver.find_element_by_id("password-field").send_keys("#password#")
            driver.find_element_by_class_name("button-tosca-login").click()
            driver.get("https://internship.ddstelkom.id/daily/707/approve")
            driver.get("https://internship.ddstelkom.id/internship/detail/2129")
            time.sleep(5)
            driver.close()
        else:
            print("Kirim gagal")
    else:
        print("Dibatalkan")


if __name__ == '__main__':
    print("Choose: ")
    print("====================")
    print("1. Input IDT Hari ini")
    print("2. Input IDT Tanggal Tertentu")
    print("3. Input Sekaligus / Aktifitas sama semua")
    print("4. Input Sekaligus / Aktifitas beda per hari")
    print("5. Edit or Remove Page")
    print("6. Kirim semua IDT")
    pilih = input(": ")
    #print(str(y), str(m))
    if (pilih == "1"):
        aktifitas = input("Masukkan Aktifitas Hari Ini: ")
        inputDaily()
    elif (pilih == "2"):
        tanggal = input("Masukkan Tanggal (BB-HH): ")
        aktifitas = input("Masukkan Aktifitas : ")
        inputSpesifik()
    elif (pilih == "3"):
        aktifitas = input("Masukkan Aktifitas untuk semua: ")
        inputSekaligus()
    elif (pilih == "4"):
        inputSekaligusCustom()
    elif (pilih == "5"):
        eidtremove()
    elif (pilih == "6"):
        kirimSemua()
    else:
        print("Unknown input")
#
# if __name__ == '__main__':
#