from Pages.Base_page import BasePage
from playwright.sync_api import expect

class CheckoutPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.head_1 = self.page.locator('//span[text() = "Checkout: Your Information"]')
        self.head_2 = self.page.locator('//span[text() = "Checkout: Overview"]')
        self.head_3 = self.page.locator('//span[text() = "Checkout: Complete!"]')
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
        self.back_home_button = self.page.locator('//button[text()="Back Home"]')
        self.success_text = self.page.locator('//h2[text() = "Thank you for your order!"]')
        self.success_description = self.page.locator('//div[text()="Your order has been dispatched, and will arrive just as fast as the pony can get there!"]')
        self.success_image = self.page.locator('//img[@alt="Pony Express"]')


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
        expect(self.item_total).to_be_visible()
        expect(self.tax).to_be_visible()
        expect(self.total_price).to_be_visible()
        expect(self.cancel_button).to_be_visible()
        expect(self.finish_button).to_be_visible()

        for i in range(self.items.count()):
            expect(self.items.nth(i)).to_be_visible()
            expect(self.product_names.nth(i)).to_be_visible()
            expect(self.product_descriptions.nth(i)).to_be_visible()
            expect(self.product_prices.nth(i)).to_be_visible()
        print("\n<<checkout page opened correctly>>")

    def verify_product_count_in_checkout_should_equal(self, count):
        assert self.items.count() == count

    def verify_prices_is_right_in_checkout(self, total_product_prices_actual):
        total_product_price_checkout = 0
        prices = []

        total_price = self.total_price.text_content()
        total_price_clean = float(total_price.replace("Total: $",""))

        tax_price = self.tax.text_content()
        tax_price_clean = float(tax_price.replace("Tax: $",""))

        item_total_price = self.item_total.text_content()
        item_total_price_clean = float(item_total_price.replace("Item total: $",""))

        for i in range(self.items.count()):
            price = self.product_prices.nth(i).text_content()
            clean_price = float(price.replace("$", ""))
            prices.append(clean_price)

        total_product_price_checkout = sum(prices)

        assert total_price_clean == (total_product_price_checkout + tax_price_clean)
        assert total_price_clean == (total_product_prices_actual + tax_price_clean)
        assert total_product_prices_actual == item_total_price_clean
        assert total_product_prices_actual == total_product_price_checkout

        print("\n<<All prices are right in checkout page>>")

    def verify_names_and_descriptions_in_checkout(self, actual_names, actual_descriptions):
        names = []
        descriptions = []
        for i in range(self.items.count()):
            name = self.product_names.nth(i).text_content()
            description = self.product_descriptions.nth(i).text_content()
            names.append(name)
            descriptions.append(description)

        assert actual_names == names
        assert actual_descriptions == descriptions

    def click_on_finsh_button(self):
        self.finish_button.click()

    def verify_success_page_opened_correctly(self):
        expect(self.head_3).to_be_visible()
        expect(self.success_image).to_be_visible()
        expect(self.success_text).to_be_visible()
        expect(self.success_description).to_be_visible()
        expect(self.back_home_button).to_be_visible()

    def back_to_home_page(self):
        self.back_home_button.click()