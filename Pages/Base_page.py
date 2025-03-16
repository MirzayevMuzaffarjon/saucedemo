from playwright.sync_api import Page, expect

class BasePage:
    def __init__(self, page:Page):
        self.page = page

    def open_url(self, url):
        self.page.goto(url, wait_until="networkidle")

    def wait(self, time: int):
        self.page.wait_for_timeout(time*1000)