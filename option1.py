import time
from selenium.webdriver.common.by import By

def likePeople(driver, profile):
  driver.find_element(By.CSS_SELECTOR, '[placeholder="Pesquisar"]').send_keys(profile)
  time.sleep(2)
  driver.find_elements(By.CLASS_NAME, '-qQT3')[0].click()
  time.sleep(5)
  publications = driver.find_elements(By.CLASS_NAME, '_aanf')
  for public in publications:
    public.click()
    time.sleep(4)
    driver.find_element(By.CLASS_NAME, '_aamw').click()
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, '[aria-label="Fechar"]').click()