from features.pages.login_page import LoginPage, LoginPageLocator
from features.pages.flight_finder_page import FlightFinderPage, FlightFinderPageLocator
from selenium import webdriver
import allure
from webdriver_manager.chrome import ChromeDriverManager

options = [
    '--headless',
    '--disable-gpu',
    '--window-size=1280x800',
    '--disable-dev-shm-usage',
    '--no-sandbox',
    '--acceptInsecureCerts',
    '--disable-infobars',
    '--ignore-certificate-errors',
    '--remote-debugging-port=9222',
    '--disable-blink-features=BlockCredentialedSubresources',
    '--disable-web-security',
    '--disable-browser-side-navigation'
]

def before_all(context):
    chromeOptions = webdriver.ChromeOptions()
    chromeOptions._arguments = options
    context.driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=chromeOptions)
    context.driver.get("http://newtours.demoaut.com/")
    context.driver.maximize_window()
    context.login_page = LoginPage()
    context.login_page_locators = LoginPageLocator()
    context.flight_finder_page = FlightFinderPage()
    context.flight_finder_page_locators = FlightFinderPageLocator()


def after_scenario(context, scenario):
    if scenario.status == "failed":
        allure.attach(context.driver.get_screenshot_as_png(),
                      name='screenshot',
                      attachment_type=allure.attachment_type.PNG)


def after_all(context):
    context.driver.close()