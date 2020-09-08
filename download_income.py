# Download links are not exposed so must use selenium
# actually not mb
# deprecated

from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.options import Options
import os
import pandas as pd

FIREFOX_LOC = 'C:\\Program Files\\Mozilla Firefox\\firefox.exe'
# binary = FirefoxBinary('C:\\Users\\sushe\\Tech\\Development\\libs\\geckodriver.exe')


# Setup headless firefox
options = Options()
options.headless = True
profile = webdriver.FirefoxProfile()
profile.set_preference('browser.download.folderList', 2)
profile.set_preference('browser.download.manager.showWhenStarting', False)
profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'text/csv')
binary = FirefoxBinary(FIREFOX_LOC)

# Read state codes
df = pd.read_csv('raw_data\state_codes.csv')
print(df.head())
print(df.columns)
codes = df['code']

profile.set_preference('browser.download.dir', os.getcwd() + '\\raw_data\\personal_income')
browser = webdriver.Firefox(profile, firefox_binary=binary, options=options)

for x in (codes):
    print(x)
    browser.get("https://fred.stlouisfed.org/series/" + x + "PCPI")
    browser.find_element_by_id('download-button').click()
    browser.find_element_by_id('download-data-csv').click()
    browser.quit()
    