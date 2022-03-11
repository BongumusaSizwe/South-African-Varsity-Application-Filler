'''Python to to autofill UNISA online application.
Disclaimer: Make sure you know what you are doing before using it
'''


from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
#Check correct driver here: https://pypi.org/project/webdriver-manager/
from webdriver_manager.firefox import GeckoDriverManager



details = {
    'name': 'Tholwana',
    'surname': 'Maloma',
    'cell':'+27617095670',
    'id':'0403110957076',
    'addr':'13719 Kuthangi Street, Palmrideg Ext 8, 1458',
    'parent_name': 'Nomsa Gladys Maloma',
    'parent_cell': '+27849470796',
    'year': '04',
    'month': '03',
    'day':'11',
}

browser = webdriver.Firefox(executable_path=GeckoDriverManager().install())
# browser = webdriver.Firefox()
#Open unisa online application portal:Caution: Elements change often
browser.get(
    'https://www.unisa.ac.za/sites/corporate/default/Apply-for-admission/Apply-for-admission-to-study:-application-tool'
    )

# Wait till  elements show up

wait = WebDriverWait(browser,45)
delay = 40
try:
    ud = WebDriverWait(browser, delay),until(EC.presence_of_elements_located((By.ID, 'UD')))
    print('Page is readt')
    browser.find_element_by_id('UD').click()
except:
    print("Page took too long to load")

WebDriverWait(browser, delay).until(EC.presence_of_elements_located((By.ID, 'showNO')))
browser.find_element_by_id('showNO').click()


WebDriverWait(browser, delay).until(EC.presence_of_elements_located((By.NAME, 'student.surname')))
browser.find_element_by_name('student.surname').send_keys(details['surname'])
browser.find_element_by_name('student.firstnames').send_keys(details['name'])

browser.find_element_by_name('student.birthYear').select_by_value(details['year'])
browser.find_element_by_name('student.birthMonth').select_by_value(details['month'])
browser.find_element_by_name('student.birthMonth').select_by_value(details['month'])
browser.find_element_by_name('student.birthDay').select_by_value(details['day'])

browser.implicitly_wait(10)

browser.execute_script('validate()')