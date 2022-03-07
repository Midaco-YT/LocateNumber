import phonenumbers
import pyautogui
from phonenumbers import geocoder
from os import system, name
import pyfiglet, os, threading
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode
import folium
from selenium import webdriver
from time import sleep
import pyperclip

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

clear()
system('title FindNumber V1 / Made By MidacoYT')
print(pyfiglet.figlet_format("FindNumber V1"))

number = input("Number with country code: ")
key = "f2698d2dc8e342cfb20bf2b5eb61a8e7"

phonenumber = phonenumbers.parse(number)
location = geocoder.description_for_number(phonenumber,'fr')
print(location)

service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, 'fr'))

geocoder = OpenCageGeocode("f2698d2dc8e342cfb20bf2b5eb61a8e7")

query = str(location)

results = geocoder.geocode(query)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat, lng)

myMap = folium.Map(location=[lat, lng], zoom_start=9)

folium.Marker([lat, lng], popup=location).add_to((myMap))

myMap.save('Location.html')

answer = input("More information: ")
if answer == "yes":

    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    driver = webdriver.Chrome(executable_path='chromedriver.exe')

    driver.get("https://opencagedata.com/demo")
    sleep(3)
    driver.find_element_by_xpath("/html[1]/body[1]/main[1]/div[1]/div[2]/div[1]/form[1]/div[3]/div[2]/div[1]/input[1]").click();
    sleep(1)
    pyautogui.hotkey("ctrl", "a")
    sleep(2)
    pyautogui.press("delete")
    sleep(2)
    pyautogui.write(f"{lat, lng}")
    sleep(1)
    driver.find_element_by_xpath("/html[1]/body[1]/main[1]/div[1]/div[2]/div[1]/form[1]/div[4]/div[2]/input[1]").click();
    sleep(1)
    pyautogui.hotkey("ctrl", "a")
    pyautogui.press("delete")
    pyautogui.write(f"{key}")
    sleep(1)
    driver.find_element_by_xpath("/html[1]/body[1]/main[1]/div[1]/div[2]/div[1]/form[1]/div[5]/div[2]/button[1]").click();
    sleep(5)
    driver.find_element_by_xpath("/html[1]/body[1]/main[1]/div[1]/div[2]/div[2]/div[1]/nav[1]/div[1]/a[3]").click();
    sleep(1)
    driver.find_element_by_xpath("/html[1]/body[1]/main[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[3]/div[1]/a[1]").click();
elif answer == "no":
    os.system(quit())
else:
    print("Please enter yes or no.")

