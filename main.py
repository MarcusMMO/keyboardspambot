from selenium import webdriver
import time
from sys import platform

if platform == "darwin":
    PATH = './chromedriver'
elif platform == "win32":
    PATH = './chromedriver.exe'
else:
    print('This Python Script is not compatible with your operating system...')
    exit()


browser = webdriver.Chrome(PATH)

browser.get('https://www.typingtest.com/')

time.sleep(2)

agreeButton = browser.find_element_by_class_name('sc-bwzfXH')
agreeButton.click()

startButton = browser.find_element_by_class_name('start-btn')
startButton.click()

time.sleep(3)

clickArea = browser.find_element_by_class_name('test-notification')
clickArea.click()

editArea = browser.find_element_by_class_name('test-edit-area')

timer = browser.find_element_by_class_name('test-timer')

while True:

    textArea = browser.find_element_by_class_name('test-text-area')
    text = textArea.text

    for letters in text:
        editArea.send_keys(letters)

