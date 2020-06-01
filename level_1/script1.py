from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://158.69.76.135/level1.php')



def votes_levl(num, identi):
    for _ in range(num):
        browser.find_element_by_name("id").send_keys(id)
        browser.find_element_by_name("holdthedoor").click()

ide = "1565"
votes_levl(4048, ide)
