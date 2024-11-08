import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import logging
from typing import Optional

# Configuração do logger
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

# Exceções customizadas
class ElementNotFoundException(Exception):
    pass

class WebDriverInitializationException(Exception):
    pass

# Singleton para o WebDriver
class ChromeDriverSingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ChromeDriverSingleton, cls).__new__(cls)
            cls._instance.driver = cls._initialize_driver()
        return cls._instance

    @staticmethod
    def _initialize_driver() -> webdriver.Chrome:
        try:
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--start-maximized")
            chrome_options.binary_location = r'C:\Program Files\Google\Chrome\Application\chrome.exe'

            service = Service(ChromeDriverManager().install())
            driver = webdriver.Chrome(service=service, options=chrome_options)
            logging.info("WebDriver inicializado com sucesso.")
            return driver
        except Exception as e:
            logging.error(f"Erro ao inicializar o WebDriver: {e}")
            raise WebDriverInitializationException("Falha ao inicializar o WebDriver.")

# Classe abstrata para busca de elementos
class ElementFinderStrategy:
    def find_element(self, identifier: str) -> Optional[str]:
        raise NotImplementedError("Este método deve ser implementado por subclasses.")

# Implementação de busca com Selenium
class SeleniumElementFinder(ElementFinderStrategy):
    def __init__(self):
        self.driver = ChromeDriverSingleton().driver

    def find_element(self, xpath: str) -> Optional[str]:
        try:
            self.driver.get('https://steamdb.info/sales/')
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))
            element = self.driver.find_element(By.XPATH, xpath)
            logging.info(f"Elemento encontrado com Selenium: {element.text}")
            return element.text
        except Exception as e:
            logging.warning(f"Erro ao buscar o elemento com Selenium: {e}")
            return None

# Implementação de busca com BeautifulSoup
class BeautifulSoupElementFinder(ElementFinderStrategy):
    def find_element(self, tag: str, text: str) -> Optional[str]:
        try:
            response = requests.get('https://steamdb.info/sales/')
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')
            element = soup.find(tag, string=text)
            if element:
                logging.info(f"Elemento encontrado com BeautifulSoup: {element.text}")
                return element.text
            return None
        except Exception as e:
            logging.warning(f"Erro ao buscar o elemento com BeautifulSoup: {e}")
            return None

# Classe principal para busca de elementos
class ElementSearcher:
    def __init__(self):
        self.selenium_finder = SeleniumElementFinder()
        self.bs_finder = BeautifulSoupElementFinder()

    def search(self, identifier: str, tag: str, text: str) -> str:
        result = self.selenium_finder.find_element(identifier)
        if result:
            return result

        logging.info("Tentando buscar o elemento com BeautifulSoup como fallback.")
        result = self.bs_finder.find_element(tag, text)
        if result:
            return result

        raise ElementNotFoundException("Elemento não encontrado em ambas as tentativas.")

# Classe para controle da aplicação
class ApplicationController:
    def __init__(self):
        self.searcher = ElementSearcher()

    def run(self):
        try:
            xpath = "//span[text()='Show only historical lows']"
            tag = 'span'
            text = 'Show only historical lows'
            result = self.searcher.search(xpath, tag, text)
            logging.info(f"Texto do elemento encontrado: {result}")
        except ElementNotFoundException as e:
            logging.error(e)
        except Exception as e:
            logging.critical(f"Erro inesperado: {e}")
        finally:
            driver_instance = ChromeDriverSingleton().driver
            driver_instance.quit()
            logging.info("WebDriver encerrado com sucesso.")

if __name__ == "__main__":
    app = ApplicationController()
    app.run()
