import allure, pytest

@allure.title("checkout page, prices, total prices")
def test_checkout_page(logged_in_home_page, cart_page, checkout_page):
    logged_in_home_page.open_home_page()
    names, descriptions, prices = logged_in_home_page.add_product_to_the_cart(3)
    logged_in_home_page.open_cart_page()
    cart_page.open_checkout_page()
    checkout_page.verify_pre_checkout_page_opened_correctly()
    checkout_page.fill_inputs("Muzaffarjon", "Mirzayev", "778899")
    checkout_page.open_checkout_page()
    checkout_page.verify_checkout_page_opened_correctly()
    checkout_page.verify_total_product_price(sum(prices))