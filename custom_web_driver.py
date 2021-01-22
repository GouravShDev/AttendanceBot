from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import constants

class CustomWebdriver:
    def __init__(self, driverPath=constants.driverPath, profilePath = constants.profilePath, link = ''):
        super().__init__()
        self._driverPath = driverPath
        self._profilePath = profilePath
        self._link = link
        options = Options()
        options.add_argument(r"--user-data-dir=" + self._profilePath)
        options.add_experimental_option("detach", True)
        self._driver = webdriver.Chrome(executable_path=self._driverPath, options=options)



    def getDriverPath(self):
        return self._driverPath
    
    def getProfilePath(self):
        return self._profilePath
    

    def launch(self):
        self._driver.get(self._link)
        self._driver.find_element_by_xpath(constants.micXss).click()
        self._driver.find_element_by_xpath(constants.cameraXss).click()
        sleep(4)
        self._driver.find_element_by_xpath(constants.joinButtonXss).click()
