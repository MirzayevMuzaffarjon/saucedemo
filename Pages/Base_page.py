from playwright.sync_api import Page

class BasePage:
    def __init__(self, page:Page):
        self.page = page
        self.burger_menu = self.page.locator('//button[@id="react-burger-menu-btn"]')
        self.logo = self.page.locator('//div[@class="app_logo" and text() = "Swag Labs"]')
        self.cart_icon = self.page.locator('//div[@id="shopping_cart_container"]')
        self.cart_badge = self.page.locator('//span[@class="shopping_cart_badge"]')

    def open_url(self, url):
        self.page.goto(url, wait_until="networkidle")

    def wait(self, time: int):
        self.page.wait_for_timeout(time*1000)