from Pages.Base_page import BasePage
from playwright.sync_api import expect

class CheckoutPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.head_1 = self.page.locator('//span[text() = "Checkout: Your Information"]')
        self.head_2 = self.page.locator('//span[text() = "Checkout: Overview"]')
        self.first_name_input = self.page.locator('//input[@id="first-name"]')
        self.last_name_input = self.page.locator('//input[@id="last-name"]')
        self.postal_code_input = self.page.locator('//input[@id="postal-code"]')
        self.cancel_button = self.page.locator('//button[@id="cancel"]')
        self.continue_button = self.page.locator('//input[@id="continue"]')
        self.finish_button = self.page.locator('//button[@id="finish"]')
        self.qty_label = self.page.locator('//div[text() = "QTY"]')
        self.description_label = self.page.locator('//div[text() = "Description"]')
        self.items = self.page.locator('//div[@class="cart_item"]')
        self.product_names = self.page.locator('//div[@class="inventory_item_name"]')
        self.product_descriptions = self.page.locator('//div[@class="inventory_item_desc"]')
        self.product_prices = self.page.locator('//div[@class="inventory_item_price"]')
        self.item_total = self.page.locator('//div[@class="summary_subtotal_label"]')
        self.tax = self.page.locator('//div[@class="summary_tax_label"]')
        self.total_price = self.page.locator('//div[@class="summary_total_label"]')
        clean_item_total = 0


    def verify_pre_checkout_page_opened_correctly(self):
        expect(self.head_1).to_be_visible()
        expect(self.first_name_input).to_be_visible()
        expect(self.last_name_input).to_be_visible()
        expect(self.postal_code_input).to_be_visible()
        expect(self.cancel_button).to_be_visible()
        expect(self.continue_button).to_be_visible()
        print("\n<<pre checkout page opened correctly>>")

    def fill_inputs(self, first_name, last_name, postal_code):
        self.first_name_input.click()
        self.first_name_input.fill(first_name)
        self.last_name_input.click()
        self.last_name_input.fill(last_name)
        self.postal_code_input.click()
        self.postal_code_input.fill(postal_code)

    def open_checkout_page(self):
        self.continue_button.click()

    def verify_checkout_page_opened_correctly(self):
        expect(self.head_2).to_be_visible()
        expect(self.qty_label).to_be_visible()
        expect(self.description_label).to_be_visible()
        expect(self.cancel_button).to_be_visible()
        expect(self.finish_button).to_be_visible()

        for i in range(self.items.count()):
            expect(self.items.nth(i)).to_be_visible()
            expect(self.product_names.nth(i)).to_be_visible()
            expect(self.product_descriptions.nth(i)).to_be_visible()
            expect(self.product_prices.nth(i)).to_be_visible()

        print("\n<<checkout page opened correctly>>")

    def verify_total_product_price(self, total_product_prices_actual ):
        prices_in_checkout = []
        for i in range(self.items.count()):
            price = self.product_prices.nth(i).text_content()
            clean_price = float(price.replace("$", ""))
            prices_in_checkout.append(clean_price)

        item_total = self.item_total.text_content()
        clean_item_total = float(item_total.replace("Item total: $", ""))
        print(f"actual total product price: {total_product_prices_actual}")
        print(f"total product price in checkout: {sum(prices_in_checkout)}")
        print(f"item total: {clean_item_total}")
        assert sum(prices_in_checkout) == clean_item_total
        assert sum (prices_in_checkout) == total_product_prices_actual

    #def verify_total_price(self):




