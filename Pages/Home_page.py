from Pages.Base_page import BasePage
from playwright.sync_api import expect
from dotenv import load_dotenv
import os

class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        load_dotenv()
        self.head_title_Products = self.page.locator('//span[text() = "Products"]')
        self.sort_drop_down= self.page.locator('//select[@class="product_sort_container"]')
        self.products = self.page.locator('//div[@class="inventory_item"]')
        self.log_out_button = self.page.locator('//a[@id="logout_sidebar_link"]')
        self.sort_option_a_to_z = "Name (A to Z)"
        self.sort_option_z_to_a = "Name (Z to A)"
        self.sort_option_low_to_high = "Price (low to high)"
        self.sort_option_high_to_low = "Price (high to low)"
        self.active_option = self.page.locator('//span[@class="active_option"]')
        self.product_names = self.page.locator('//div[@class="inventory_item_name "]')
        self.product_descriptions = self.page.locator('//div[@class="inventory_item_desc"]')
        self.product_prices = self.page.locator('//div[@class="inventory_item_price"]')
        self.add_to_cart_buttons = self.page.locator('//button[text()="Add to cart"]')
        self.back_button_in_detail = self.page.locator('//button[@id="back-to-products"]')
        self.product_name_in_detail = self.page.locator('//div[@data-test="inventory-item-name"]')
        self.product_desc_in_detail = self.page.locator('//div[@data-test="inventory-item-desc"]')
        self.product_price_in_detail = self.page.locator('//div[@class="inventory_details_price"]')
        self.add_to_cart_button_in_detail = self.page.locator('//button[@id="add-to-cart"]')
        self.remove_button_in_detail = self.page.locator('//button[@id="remove"]')
        self.remove_buttons_in_the_list = self.page.locator('//button[text()="Remove"]')

    def verify_home_page_opened_correctly(self):
        expect(self.burger_menu).to_be_visible()
        expect(self.logo).to_be_visible()
        expect(self.cart_icon).to_be_visible()
        expect(self.head_title_Products).to_be_visible()
        expect(self.sort_drop_down).to_be_visible()

        for i in range(self.products.count()):
            self.products.nth(i).scroll_into_view_if_needed()
            expect(self.products.nth(i)).to_be_visible()
            expect(self.product_names.nth(i)).to_be_visible()
            expect(self.product_descriptions.nth(i)).to_be_visible()
            expect(self.product_prices.nth(i)).to_be_visible()
            expect(self.add_to_cart_buttons.nth(i)).to_be_visible()
            print(f"\n<<{i+1} - product is visisble>>")

        print("\n<<home page opened correctly>>")

    def open_home_page(self):
        self.open_url(os.getenv("HOME_PAGE_URL"))
        self.verify_home_page_opened_correctly()
        print("\n<<home page opened correctly>>")

    def log_out(self):
        self.burger_menu.click()
        self.log_out_button.click()

    def sort_product_list_low_to_high(self):
        self.sort_drop_down.click()
        self.sort_drop_down.select_option(self.sort_option_low_to_high)
        expect(self.active_option).to_have_text(self.sort_option_low_to_high)
        print(f"\n<<{self.sort_option_low_to_high} tanlandi va active holatda>>")

    def sort_product_list_high_to_low(self):
        self.sort_drop_down.click()
        self.sort_drop_down.select_option(self.sort_option_high_to_low)
        expect(self.active_option).to_have_text(self.sort_option_high_to_low)
        print(f"\n<<{self.sort_option_high_to_low} tanlandi va active holatda>>")

    def verify_product_list_price_sorted(self, low_to_high_or_high_to_low):
        product_prices_list = []
        for i in range(self.product_prices.count()):
            price_text = self.product_prices.nth(i).text_content()
            clean_price = float(price_text.replace("$", ""))
            product_prices_list.append(clean_price)

        if low_to_high_or_high_to_low == "low_to_high":
            expected_list = sorted(product_prices_list)
            assert product_prices_list == expected_list
            print(f"\nexpected product list: {expected_list}")
            print(f"\nactual product list: {product_prices_list}")

        elif low_to_high_or_high_to_low == "high_to_low":
            expected_list = sorted(product_prices_list, reverse=True)
            assert product_prices_list == expected_list
            print(f"\nexpected product list: {expected_list}")
            print(f"\nactual product list: {product_prices_list}")

    def sort_product_list_a_to_z(self):
        if self.active_option.text_content() == self.sort_option_a_to_z:
            print("\n<<a to z bo'yicha sort qilish tanlangan>>")
        else:
            self.sort_drop_down.click()
            self.sort_drop_down.select_option(self.sort_option_a_to_z)
            print("\n<<a to z bo'yicha sort qilish tanlandi>>")

        expect(self.active_option).to_have_text(self.sort_option_a_to_z)

    def sort_product_list_z_to_a(self):
        self.sort_drop_down.click()
        self.sort_drop_down.select_option(self.sort_option_z_to_a)
        expect(self.active_option).to_have_text(self.sort_option_z_to_a)
        print("\n<<z_to_a sort option selected and actual>>")

    def verify_product_list_sorted(self, a_to_z_or_z_to_a):
        product_name_list = []
        for i in range(self.product_names.count()):
            product_name_list.append(self.product_names.nth(i).text_content())

        if a_to_z_or_z_to_a == "a_to_z":
            expected_sorted_list = sorted(product_name_list)
            assert product_name_list == expected_sorted_list
            print(f"\nactual: {product_name_list}")
            print(f"\nexpected: {expected_sorted_list}")

        elif a_to_z_or_z_to_a == "z_to_a":
            expected_sorted_list = sorted(product_name_list, reverse=True)
            assert product_name_list == expected_sorted_list
            print(f"\nactual: {product_name_list}")
            print(f"\nexpected: {expected_sorted_list}")

    def matching_data_list_and_detail(self):
        for i in range(self.products.count()):
            name = self.product_names.nth(i).text_content()
            desc = self.product_descriptions.nth(i).text_content()
            price = self.product_prices.nth(i).text_content()
            self.product_names.nth(i).click()
            expect(self.product_name_in_detail).to_have_text(name)
            expect(self.product_desc_in_detail).to_have_text(desc)
            expect(self.product_price_in_detail).to_have_text(price)
            print(f"\n<<{i+1} - maxsulot ma'lumotlari list va detailda bir xil>>")
            self.back_button_in_detail.click()

    def add_product_to_the_cart_in_the_list(self, product_count):
        for i in range(product_count):
            self.add_to_cart_buttons.nth(i).click()

        expect(self.cart_badge).to_have_text(f"{product_count}")
        print(f"\n<<cart badge have text: {self.cart_badge.text_content()}>>")

        for i in range(self.remove_buttons_in_the_list.count()):
            expect(self.remove_buttons_in_the_list.nth(i)).to_be_visible()

        print("\n<<Remove buttons are visible>>")

    def add_product_to_the_cart(self, product_count):
        product_names = []
        product_prices = []
        descriptions = []
        for i in range(product_count):
            self.product_names.nth(i).click()
            self.add_to_cart_button_in_detail.click()
            expect(self.remove_button_in_detail).to_be_visible()
            product_names.append(self.product_name_in_detail.text_content())
            descriptions.append(self.product_desc_in_detail.text_content())
            price = self.product_price_in_detail.text_content()
            clean_price = float(price.replace("$", ""))
            product_prices.append(clean_price)
            self.back_button_in_detail.click()

        expect(self.cart_badge).to_have_text(f"{product_count}")
        return product_names, descriptions, product_prices

    def open_cart_page(self):
        self.cart_icon.click()