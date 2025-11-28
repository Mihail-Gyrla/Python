import pytest
from selenium import webdriver
from lesson7.shop import ShopPage


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_shopping(driver):
    shop_page = ShopPage(driver)
    shop_page.open()
    shop_page.authorization(login="standard_user", password="secret_sauce")
    shop_page.add_to_cart()
    shop_page.cart()
    shop_page.checkout_cart()
    shop_page.checkout_page(first="Михаил",last="Гырла",code="620105")

    total = shop_page.get_total_price()
    assert total == 58.29