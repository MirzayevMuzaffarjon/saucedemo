import pytest, os
from playwright.sync_api import sync_playwright, Page, expect
from Pages.Login_page import LoginPage
from Pages.Home_page import HomePage
from Pages.Cart_page import CartPage
from Pages.Checkout_page import CheckoutPage
from dotenv import load_dotenv
load_dotenv()

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=100)
        print("\n<<Browser launched>>")
        yield browser
        browser.close()
        print("\n<<Browser closed>>")

@pytest.fixture(scope="function")
def context(browser):
    context = browser.new_context()
    print("\n<<Context opened>>")
    yield context
    context.close()
    print("\n<<Context closed>>")

@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()
    print("\n<<Page opened>>")
    yield page
    page.close()
    print("\n<<Page closed>>")

#-----------------------------------------------------------------------------

@pytest.fixture(scope="session")
def login_and_save_state():  # context fixture'ini ishlatamiz
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, slow_mo=100)
        context = browser.new_context()
        page = context.new_page()
        login_page = LoginPage(page)
        home_page = HomePage(page)

        login_page.open_url(os.getenv("BASEURL"))
        login_page.verify_login_page_opened_correctly()
        login_page.login_with(os.getenv("STANDARD_USERNAME"), os.getenv("PASSWORD"))
        home_page.verify_home_page_opened_correctly()

        context.storage_state(path="state.json")
        print("\n<<state saqlandi>>")
        page.close()
        context.close()
        browser.close()

@pytest.fixture(scope="function")
def logged_in_context(login_and_save_state, browser):
    context = browser.new_context(storage_state="state.json")
    print("\n<<logged_in_context opened>>")
    yield context
    context.close()
    print("\n<<logged_in_context closed>>")

@pytest.fixture(scope="function")
def logged_in_page(logged_in_context):
    logged_in_page = logged_in_context.new_page()
    print("\n<<logged in page opened>>")
    yield logged_in_page
    logged_in_page.close()
    print("\n<<logged in page closed>>")

#----------------------------------------------------------------------------------------

@pytest.fixture()
def login_page(page):
    return LoginPage(page)

@pytest.fixture()
def home_page(page):
    return HomePage(page)

@pytest.fixture()
def logged_in_home_page(logged_in_page):
    return HomePage(logged_in_page)

@pytest.fixture()
def cart_page(logged_in_page):
    return CartPage(logged_in_page)

@pytest.fixture()
def checkout_page(logged_in_page):
    return CheckoutPage(logged_in_page)