from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
BASE_URL = "https://demowebshop.tricentis.com/"
BROWSER = "chrome"
#BROWSER = "firefox"

class ComputersPage:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def get_subgroup_names(self):
        # find the sub-group elements
        subgroups = self.driver.find_elements(By.CSS_SELECTOR, 'ul.sublist.firstLevel li a')
        # get the names of the sub-groups
        names = [subgroup.text.strip() for subgroup in subgroups if subgroup.text.strip() != '']
        return names
    
class TestComputersPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()  # or webdriver.Firefox() if you're using Firefox
        self.computers_page = ComputersPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_subgroup_names(self):
        self.computers_page.open_url(f"{BASE_URL}/computers")
        expected_names = ['Desktops', 'Notebooks', 'Accessories']
        self.assertEqual(self.computers_page.get_subgroup_names(), expected_names)


class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def register_user(self, first_name, last_name, email, password):
        # find the form elements and fill them out
        self.driver.find_element(By.ID, 'FirstName').send_keys(first_name)
        self.driver.find_element(By.ID, 'LastName').send_keys(last_name)
        self.driver.find_element(By.ID, 'Email').send_keys(email)
        self.driver.find_element(By.ID, 'Password').send_keys(password)
        self.driver.find_element(By.ID, 'ConfirmPassword').send_keys(password)
        # submit the form
        self.driver.find_element(By.XPATH, '//*[@id="register-button"]').click()

class TestRegistrationPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()  # or webdriver.Firefox() if you're using Firefox
        self.registration_page = RegistrationPage(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_user_registration(self):
        self.registration_page.open_url(f"{BASE_URL}/register")
        self.registration_page.register_user('John', 'Doe', 'test@example.com', 'password')
        # verify that the user is registered
        self.assertTrue(self.driver.find_element(By.CSS_SELECTOR, 'div.result').text == 'Your registration completed')

class BooksPageSorting:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def get_sort_options(self):
        # find the sorting dropdown
        sort_dropdown = self.driver.find_element(By.ID, 'products-orderby')
        # get the options in the dropdown
        options = [option.get_attribute('innerText') for option in sort_dropdown.find_elements(By.TAG_NAME, 'option')]
        return options

class TestBooksPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()  # or webdriver.Firefox() if you're using Firefox
        self.books_page = BooksPageSorting(self.driver)

    def tearDown(self):
        self.driver.quit()

    def test_sort_options(self):
        self.books_page.open_url(f"{BASE_URL}//books") 
        expected_options = ['Position', 'Name: A to Z', 'Name: Z to A', 'Price: Low to High', 'Price: High to Low', 'Created on']
        self.assertEqual(self.books_page.get_sort_options(), expected_options)

if __name__ == "__main__":
    unittest.main()