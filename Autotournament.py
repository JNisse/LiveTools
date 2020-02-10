from selenium import webdriver
from selenium.webdriver.support.ui import Select

import secrets
""" Behöver geckodriver(för att köras i Firefox), samt seleniumpaketet
"""
class Auto_tournament:

    
    """Loggar in i medlemssystemet och går till turneringsfliken
    """
    def __init__(self):
        self.driver =webdriver.Firefox()
        self.driver.set_page_load_timeout(30)
        self.driver.get('https://member.schack.se/ViewFederationServlet')
        self.driver.find_element_by_xpath('//*[@id="username"]').send_keys(secrets.user())
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(secrets.password())
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        self.driver.get('https://member.schack.se/ViewTournamentsServlet')
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr/td[4]/table[1]/tbody/tr[1]/td[1]/button').click()
    def new_tournament(self):
        self.driver.find_element_by_xpath('/html/body/table/tbody/tr/td[4]/table[2]/tbody/tr/td/button').click()
        self.driver.find_element_by_xpath('//*[@id="name"]').send_keys("Turneringsnamn")
        self.driver.find_element_by_xpath('//*[@id="nrofrounds"]').clear()
        self.driver.find_element_by_xpath('//*[@id="nrofrounds"]').send_keys("5")
        Select(self.driver.find_element_by_xpath('//*[@id="pairingsystem"]')).select_by_index(3)
    
    
# New tournament button
#/html/body/table/tbody/tr/td[4]/table[2]/tbody/tr/td/button

g=Auto_tournament()
g.new_tournament()
