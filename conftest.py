import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function", autouse=True) # autouse=True - будет использоваться автоматически для каждого теста
def driver(request):                            # scope="function" создания экземпляра драйвера для каждого теста отдельно
    options = Options()
    # options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage") #
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    print(type(request))
    request.cls.driver = driver # создает драйвер внутри тестовых классов (внутри наших тестов)
    yield driver
    driver.quit()


