#import required ?
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

#lists of urls, logins, password, etc.
#can these all go together in a def or master dict?
pwd = 'Password1'
carriers = ['scis', 'drisi', 'ihs', 'inova']
urls = {
  'scis': 'https://stage-myaccount.hubsmartcoverage.ca/',
  'drisi': 'https://stage-directaccess.directrate.ca/',
  'ihs': 'https://stage-myaccount.hubinsurancehunter.ca/',
  'inova': 'https://stage-myinova.inovainc.ca/'
}
users = {
    'scis': 'csgwebapps.qa+5@gmail.com',
    'drisi': 'csgwebapps.qa+216@gmail.com',
    'ihs': 'csgwebapps.qa+ihs-econ-1@gmail.com',
    'inova': 'csgwebapps.qa+inova-doc-3a@gmail.com'
}
titles = {
    'scis': 'QuickServe - Home',
    'drisi': 'Direct Access - Home',
    'ihs': 'IHConnect - Home',
    'inova': 'myInova - Home'
}


# login
    # navigate to the appropriate site
    # assert title
    # enter user email
    # enter password
    # click login
def page(site):
    print("Opening Chrome and navigating to ", (titles[site]))
    driver.maximize_window()
    driver.get(urls[site])
    driver.find_element_by_name('email').send_keys(users[site])
    driver.find_element_by_name('password').send_keys(pwd)
    driver.find_element_by_css_selector('button.Btn.Sm').click()
    print('clickity clickity')

def login(site):
    while driver.current_url != (urls[site] + "account"):
        print('sending creds')
        time.sleep(1)
    if driver.current_url == (urls[site] + "account"):
        print('we are in')


#account:
    #wait for shimmer/scrapping
    #check for auto/property policy
    #check for appropriate quote link

def scrapping(site):
    time.sleep(2)
    try:
        print("here we go a scrapping!")
        elshim = driver.find_element_by_class_name('LoadingPlaceholder')
        WebDriverWait(driver, 60).until(EC.presence_of_element_located(elshim))
        print("still shimmering")
    except NoSuchElementException:
        print("scrapping complete? - cool cool cool")
        #driver.get(urls[site] + "account/billing")
    finally:
        print("and we are done!")

# def policy_check(slug):
#     while driver.current_url == (urls[slug]):
#         print("checking billing...")
#     while driver.current_url == (urls[slug] + "account"):
#         quote_box = 0


        # try:
        #     shimmer = webdriver.is_element_present(By.CLASS_NAME, 'LoadingPlaceholder')
        # except NoSuchElementException:
        #     return False

def details(site):
#    time.sleep(5)
    while driver.current_url != (urls[site] + "account"):
        time.sleep(2)
    while driver.current_url == (urls[site] + "account"):
        driver.find_element_by_xpath("//a[contains(text(),'More Details')]").click()
        print('here is the billing details page')
        continue

    #driver.find_element_by_xpath("//")
    #assert /account
    #click 'more details'
    #pass billing details/message
    #return to /account

#def billing(site):
    #assert /account
    #click 'billing request'
    #submit 1 of 4 random request?
    #next
    #submit
    #return to /account

def logout(site):
    driver.find_element_by_css_selector('button.Btn.AccountBtn').click()
    driver.find_element_by_xpath("//a[contains(text(),'Log Out')]").click()
    print('and now we are out')
    driver.quit()
    #assert /account
    #click logout
    #click logout
    #assert /logout

#def add_driver(site):

# Finding Element by Name
# Finding Element by ID
# Finding Element by Link Text
# Finding Element by Partial Link Text
# Finding Element by Xpath
# Finding Element by CSS Selector
# Finding Element by Tagname
# Finding Element by Classname

def getlist():
    #elements = driver.find_elements_by_css("//*[not(*)]")
    elements = driver.find_elements_by_name("*")
    for i in elements:
        print(i)
        #print(chr(i))


driver = webdriver.Chrome()

site = 'drisi'
page(site)
login(site)
#details(site)
#policy_check(site)
scrapping(site)
#getlist()
logout(site)

#driver.quit()
