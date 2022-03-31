import pytest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture()
def setup():
    global Movie, Year, Director, Distributor, Producer, driver
    Movie = input("Enter Name :")
    Year = input("Enter Name :")
    Director = input("Enter Name :")
    Distributor = input("Enter Name :")
    Producer = input("Enter Name :")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    print("Test case started")
    driver.maximize_window()
    yield
    time.sleep(5)
    driver.close()

def test_form(setup):
    driver.get("https://iprimedtraining.herokuapp.com/movie.php")
    time.sleep(1)
    driver.find_element_by_name("mname").send_keys(Movie)
    time.sleep(1)
    driver.find_element_by_name("myear").send_keys(Year)
    time.sleep(1)
    driver.find_element_by_name("mdirector").send_keys(Director)
    time.sleep(1)
    driver.find_element_by_name("mdist").send_keys(Distributor)
    time.sleep(1)
    driver.find_element_by_name("mproducer").send_keys(Producer)
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/div/div[2]/form/table/tbody/tr[6]/td[2]/select/option[3]").click()
    driver.find_element_by_name("subbtn").submit()
    time.sleep(10)