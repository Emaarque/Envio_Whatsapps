import sys
#sys.path.append(<webdriver_manager path>)
from selenium import webdriver
#from webdriver_manager.chrome import ChromeDriverManager
#from webdriver_manager.firefox import firefox
#driver = webdriver.Chrome(ChromeDriverManager().install()) 

driver=webdriver.Chrome(executable_path="chromedriver.exe")
driver.maximize_window()