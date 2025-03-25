from playwright.sync_api import expect
from Pages.Base_page import BasePage

added_names = []
added_descriptions = []
added_prices = []

class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.head_of_cart_page = self.page.locator('//span[text() = "Your Cart"]')
        self.checkout_button = self.page.locator('//button[@id="checkout"]')
        self.continue_shopping_button = self.page.locator('//button[@id="continue-shopping"]')
        self.qty_label = self.page.locator('//div[@class="cart_quantity_label"]')
        self.descriptions_label = self.page.locator('//div[@class="cart_desc_label"]')
        self.product_names_in_cart = self.page.locator('//div[@class="inventory_item_name"]')
        self.product_descriptions_in_cart = self.page.locator('//div[@class="inventory_item_desc"]')
        self.product_prices_in_cart = self.page.locator('//div[@class="inventory_item_price"]')
        self.remove_buttons_in_cart = self.page.locator('//button[text() = "Remove"]')
        self.items_in_cart = self.page.locator('//div[@class="cart_item"]')

    def verify_cart_page_opened_correctly(self):
        expect(self.burger_menu).to_be_visible()
        expect(self.logo).to_be_visible()
        expect(self.cart_icon).to_be_visible()
        expect(self.head_of_cart_page).to_be_visible()
        expect(self.continue_shopping_button).to_be_visible()
        expect(self.checkout_button).to_be_visible()
        expect(self.qty_label).to_be_visible()
        expect(self.descriptions_label).to_be_visible()
        print("\n<<cart page opened correctly>>")

    def verify_products_added_correctly(self, names, descs, prices):
        for i in range(self.items_in_cart.count()):
            added_names.append(self.product_names_in_cart.nth(i).text_content())
            added_descriptions.append(self.product_descriptions_in_cart.nth(i).text_content())
            product_price = self.product_prices_in_cart.nth(i).text_content()
            clean_price = float(product_price.replace("$", ""))
            added_prices.append(clean_price)

        print(f"actual names: {names} \nnames_in_cart: {added_names} \n \n")
        print(f"actual descs: {descs} \ndescs_in_cart: {added_descriptions} \n \n")
        print(f"actual prices: {prices} \nprices_in_cart: {added_prices} \n \n")

        assert added_names == names
        assert added_descriptions == descs
        assert added_prices == prices

    def open_checkout_page(self):
        self.checkout_button.click()