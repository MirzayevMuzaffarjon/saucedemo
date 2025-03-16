import os
from dotenv import load_dotenv
load_dotenv()

def test_sort_product_list_by_price_low_to_high(logged_in_home_page):
    logged_in_home_page.open_home_page()
    logged_in_home_page.sort_product_list_low_to_high()
    logged_in_home_page.verify_product_list_price_sorted("low_to_high")

def test_sort_product_list_by_price_high_to_low(logged_in_home_page):
    logged_in_home_page.open_home_page()
    logged_in_home_page.sort_product_list_high_to_low()
    logged_in_home_page.verify_product_list_price_sorted("high_to_low")

def test_sort_product_list_a_to_z(logged_in_home_page):
    logged_in_home_page.open_home_page()
    logged_in_home_page.sort_product_list_a_to_z()
    logged_in_home_page.verify_product_list_sorted("a_to_z")

def test_sort_product_list_z_to_a(logged_in_home_page):
    logged_in_home_page.open_home_page()
    logged_in_home_page.sort_product_list_z_to_a()
    logged_in_home_page.verify_product_list_sorted("z_to_a")

