import os, allure
from dotenv import load_dotenv
load_dotenv()

@allure.title("login as standard user")
def test_login_as_standard_user(login_page, home_page):
    login_page.open_login_page()
    login_page.login_with(os.getenv("STANDARD_USERNAME"), os.getenv("PASSWORD"))
    home_page.verify_home_page_opened_correctly()


@allure.title("login with incorrect password")
def test_login_with_incorrect_password(login_page):
    login_page.open_login_page()
    login_page.login_with(os.getenv("STANDARD_USERNAME"), os.getenv("INCORRECT_PASSWORD"))
    login_page.verify_login_filed()

@allure.title("login as locked user")
def test_login_with_locked_user(login_page):
    login_page.open_login_page()
    login_page.login_with(os.getenv("LOCKED_USERNAME"), os.getenv("PASSWORD"))
    login_page.verify_login_filed()

@allure.title("login and logout")
def test_log_out(login_page, home_page):
    test_login_as_standard_user(login_page, home_page)
    home_page.log_out()
    login_page.verify_login_page_opened_correctly()

