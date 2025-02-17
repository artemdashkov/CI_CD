import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService

@pytest.fixture(scope="function", autouse=True) # autouse=True - будет использоваться автоматически для каждого теста
def driver(request):                            # scope="function" создания экземпляра драйвера для каждого теста отдельно
    print(f"\n===>\tStart driver in conftest.py")
    options = Options()
    # options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage") #
    options.add_argument("--window-size=1920,1080")

    driver_path = ChromeDriverManager().install()


    driver = webdriver.Chrome(service=ChromeService(driver_path), options=options)
    print(f"\n===>\ttype(request): {type(request)}")
    request.cls.driver = driver # создает драйвер внутри тестовых классов (внутри наших тестов)
    yield driver
    print(f"\n===>\tEnd driver in conftest.py")
    driver.quit()
