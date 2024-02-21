import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# fixture that creates class instance for each test
@pytest.fixture(scope="function", autouse=True)
def driver(request):
    # Creating ChromeOptions object
    options = Options()

    # Add options to work with tests
    options.add_argument("--headless") # Headless mode to run tests in Docker or CI

    # options that permit to run tests without UI
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    # Initializing WebDriver with Chrome and options
    driver = webdriver.Chrome(options=options)

    # Providing the driver object to the test class
    request.cls.driver = driver

    # Yielding the driver object to the test
    yield driver

    # Exiting after execution of all tests
    driver.quit()

