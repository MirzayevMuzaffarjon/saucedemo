import allure

@allure.title("Verify opening pre-checkout and checkout page")
def test_opening_checkout_page(logged_in_home_page, cart_page, checkout_page):
    logged_in_home_page.open_home_page()
    logged_in_home_page.add_product_to_the_cart(3)
    logged_in_home_page.verify_cart_badge_have_count("3")
    logged_in_home_page.open_cart_page()
    cart_page.open_pre_checkout_page()
    checkout_page.verify_pre_checkout_page_opened_correctly()
    checkout_page.fill_inputs("Muzaffarjon", "Mirzayev", "778899")
    checkout_page.open_checkout_page()
    checkout_page.verify_checkout_page_opened_correctly()
    checkout_page.verify_product_count_in_checkout_should_equal(3)

@allure.title("Verify prices in checkout page")
def test_prices_in_checkout_page(logged_in_home_page, cart_page, checkout_page):
    logged_in_home_page.open_home_page()
    names, descriptions, prices = logged_in_home_page.add_product_to_the_cart(3)
    logged_in_home_page.verify_cart_badge_have_count("3")
    logged_in_home_page.open_cart_page()
    cart_page.open_pre_checkout_page()
    checkout_page.fill_inputs("Muzaffarjon", "Mirzayev", "778899")
    checkout_page.open_checkout_page()
    checkout_page.verify_product_count_in_checkout_should_equal(3)
    checkout_page.verify_prices_is_right_in_checkout(sum(prices))

@allure.title("Verify names and descriptions in checkout page")
def test_names_and_descriptions_in_checkout(logged_in_home_page, cart_page, checkout_page):
    logged_in_home_page.open_home_page()
    names, descriptions, prices = logged_in_home_page.add_product_to_the_cart(3)
    logged_in_home_page.verify_cart_badge_have_count("3")
    logged_in_home_page.open_cart_page()
    cart_page.open_pre_checkout_page()
    checkout_page.fill_inputs("Muzaffarjon", "Mirzayev", "778899")
    checkout_page.open_checkout_page()
    checkout_page.verify_product_count_in_checkout_should_equal(3)
    checkout_page.verify_names_and_descriptions_in_checkout(names, descriptions)

@allure.title("Verify success page opening and back to home")
def test_success_page(logged_in_home_page, cart_page, checkout_page):
    logged_in_home_page.open_home_page()
    logged_in_home_page.add_product_to_the_cart(3)
    logged_in_home_page.verify_cart_badge_have_count("3")
    logged_in_home_page.open_cart_page()
    cart_page.open_pre_checkout_page()
    checkout_page.fill_inputs("name_test", "last_name_test", "778844")
    checkout_page.open_checkout_page()
    checkout_page.verify_product_count_in_checkout_should_equal(3)
    checkout_page.click_on_finsh_button()
    checkout_page.verify_success_page_opened_correctly()
    checkout_page.back_to_home_page()
    logged_in_home_page.verify_home_page_opened_correctly()

