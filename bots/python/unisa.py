'''Python to to autofill UNISA online application.
Disclaimer: Make sure you know what you are doing before using it
'''


from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
#Check correct driver here: https://pypi.org/project/webdriver-manager/
from webdriver_manager.firefox import GeckoDriverManager


browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
#Open unisa online application portal:Caution: Elements change often
browser.get(
    'https://www.unisa.ac.za/sites/corporate/default/Apply-for-admission/Apply-for-admission-to-study:-application-tool'
    )

#Wait till  elements show up

wait = WebDriverWait(browser, 60)
#Click on undergrad
wait.until(EC.element_to_be_clickable((By.ID, 'UD'))).click()
