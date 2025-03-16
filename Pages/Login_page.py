from Pages.Base_page import BasePage, expect
import os
from dotenv import load_dotenv

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        load_dotenv()
        self.logo_in_login_page = self.page.locator('//div[@class="login_logo" and text() = "Swag Labs"]')
        self.username_input = self.page.locator('//input[@id="user-name" and @placeholder="Username"]')
        self.password_input = self.page.locator('//input[@id="password" and @placeholder="Password"]')
        self.login_submit_button = self.page.locator('//input[@name="login-button"]')
        self.login_usernames_list = self.page.locator('//div[@id="login_credentials"]')
        self.login_passwords_list = self.page.locator('//div[@class="login_password"]')
        self.filed_login_error_text = self.page.locator('//h3[@data-test="error" ]')
        self.x_icon_to_close_error_text = self.page.locator('//button[@class="error-button"]')

    def verify_login_page_opened_correctly(self):
        expect(self.logo_in_login_page).to_be_visible()
        expect(self.username_input).to_be_visible()
        expect(self.password_input).to_be_visible()
        expect(self.login_submit_button).to_be_visible()
        expect(self.login_usernames_list).to_be_visible()
        expect(self.login_passwords_list).to_be_visible()
        print("\nLogin page opened correctly")

    def login_with(self, username, password):
        self.username_input.click()
        self.username_input.fill(username)
        self.password_input.click()
        self.password_input.fill(password)
        self.login_submit_button.click()
        print("\nFilled username, password and clicked submit button")

    def verify_login_filed(self):
        expect(self.filed_login_error_text).to_be_visible()
        expect(self.x_icon_to_close_error_text).to_be_visible()
        print("\nLogin failed")

    def open_login_page(self):
        self.open_url(os.getenv("BASEURL"))
        self.verify_login_page_opened_correctly()
        print("\n<<login page opened correctly>>")