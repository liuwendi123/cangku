from time import sleep

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestBrowser():
	def setup(self):
		des_caps={
			'platformName': 'android',
			'platformVersion': '6.0',
			'browserName': 'Browser',
			'noReset':True,
			'deviceName': 'emulator-5554',
			'chromedriverExecutable': '/Users/liuwendi/Documents/chromedriver'
		}
		self.driver = webdriver.Remote("http://localhost:4723/wd/hub",des_caps)
		self.driver.implicitly_wait(5)

	def teardown(self):
		self.driver.quit()

	def test_browser(self):
		self.driver.get("http://m.baidu.com")
		self.driver.find_element_by_id("index-kw").click()
		self.driver.find_element_by_id("index-kw").send_keys("appium")
		search_locator = (By.ID,"index-bn")
		WebDriverWait(self.driver,10).until(expected_conditions.visibility_of_element_located(search_locator))
		self.driver.find_element_by_id(*search_locator).click()