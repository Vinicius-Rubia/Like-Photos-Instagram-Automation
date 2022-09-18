from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import option1

def verifyOption(result):
  if result == '1':
    print('\nPor favor preencha o seu login para continuar\n')
    credentials_email = input('Email: ')
    credentials_password = input('Senha: ')
    print('\nDigite o nome do perfil da seguinte maneira: @nome_perfil\n')
    profile = input()
    openBrowser(credentials_email, credentials_password, profile)
  else:
    print('Escolha um opção válida')
    chooseOption()

def chooseOption():
  print('\nO que deseja fazer?\n')

  print('1 - Curtir todas as fotos de um perfil')
  result = input()
  verifyOption(result)

def openBrowser(email, senha, profile):
  options = webdriver.ChromeOptions()
  options.add_experimental_option('excludeSwitches', ['enable-logging'])
  driver = webdriver.Chrome(options=options)
  driver.maximize_window()

  driver.get('https://www.instagram.com/')
  time.sleep(3)
  loginInstagram(driver, email, senha, profile)


def loginInstagram(driver, email, senha, profile):
  driver.find_element(By.NAME, 'username').send_keys(email)
  driver.find_element(By.NAME, 'password').send_keys(senha)
  driver.find_element(By.CSS_SELECTOR, '[type="submit"]').click()
  time.sleep(10)
  option1.likePeople(driver, profile)