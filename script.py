""" This is script is for vote"""

from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://158.69.76.135/level0.php')


def req_votes(num, identifier):
    """ This function is to vote in many times into a web page"""
    for i in range(num):
        browser.find_element(By.NAME, "id").send_keys(identifier)
        browser.find_element(By.NAME, "holdthedoor").click()
    return "DONE"
