import  allure, pytest

@allure.title("opening cart page")
def test_opening_cart_page(logged_in_home_page, cart_page):
    logged_in_home_page.open_home_page()
    logged_in_home_page.open_cart_page()
    cart_page.verify_cart_page_opened_correctly()

@allure.title("product added to the cart successfully")
def test_product_added_to_the_cart_successfully(logged_in_home_page, cart_page):
    logged_in_home_page.open_home_page()
    names, descriptions, prices = logged_in_home_page.add_product_to_the_cart(4)
    logged_in_home_page.open_cart_page()
    cart_page.verify_cart_page_opened_correctly()
    cart_page.verify_products_added_correctly(names, descriptions, prices)

