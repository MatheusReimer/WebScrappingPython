from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

path = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(path)
def	main():

        
	def login(tupleUser):


	driver.get("https://www.amazon.com.br/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com.br%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=brflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&")
	linkLogin = driver.find_element_by_name("email")
	linkLogin.send_keys(tupleUser[0])
	linkLogin.send_keys(Keys.RETURN)
	password  = driver.find_element_by_name("password")
	password.send_keys(tupleUser[1])
	password.send_keys(Keys.RETURN)

login(tupleUser)
