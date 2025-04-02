import allure

@allure.title("sort product list low to high by price")
def test_sort_product_list_by_price_low_to_high(logged_in_home_page):
    logged_in_home_page.open_home_page()
    logged_in_home_page.sort_product_list_low_to_high()
    logged_in_home_page.verify_product_list_sorted_by_price("low_to_high")

@allure.title("sort product list high to low by price")
def test_sort_product_list_by_price_high_to_low(logged_in_home_page):
    logged_in_home_page.open_home_page()
    logged_in_home_page.sort_product_list_high_to_low()
    logged_in_home_page.verify_product_list_sorted_by_price("high_to_low")

@allure.title("sort product list a to z by name")
def test_sort_product_list_a_to_z(logged_in_home_page):
    logged_in_home_page.open_home_page()
    logged_in_home_page.sort_product_list_a_to_z()
    logged_in_home_page.verify_product_list_sorted("a_to_z")

@allure.title("sort product list z to a by name")
def test_sort_product_list_z_to_a(logged_in_home_page):
    logged_in_home_page.open_home_page()
    logged_in_home_page.sort_product_list_z_to_a()
    logged_in_home_page.verify_product_list_sorted("z_to_a")

@allure.title("product data match with product  detail data")
def test_list_data_match_with_detail_data(logged_in_home_page):
    logged_in_home_page.open_home_page()
    logged_in_home_page.verify_matching_data_list_and_detail()

@allure.title("adding product to the cart from product list")
def test_add_product_to_the_cart_in_the_list(logged_in_home_page):
    logged_in_home_page.open_home_page()
    logged_in_home_page.add_product_to_the_cart_in_the_list(3)
    logged_in_home_page.verify_cart_badge_have_count("3")
    logged_in_home_page.verify_remove_buttons_in_the_list(3)

@allure.title("adding product to the cart from product detail")
def test_adding_product_to_the_cart(logged_in_home_page):
    logged_in_home_page.open_home_page()
    logged_in_home_page.add_product_to_the_cart(4)
    logged_in_home_page.verify_cart_badge_have_count("4")






