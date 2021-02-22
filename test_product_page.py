import pytest

from pages.product_page import ProductPage


@pytest.mark.parametrize('link', ["?promo=offer0",
                                  "?promo=offer1",
                                  "?promo=offer2",
                                  "?promo=offer3",
                                  "?promo=offer4",
                                  "?promo=offer5",
                                  "?promo=offer6",
                                  pytest.param("?promo=offer7", marks=pytest.mark.xfail),
                                  "?promo=offer8",
                                  "?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    original_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{0}".format(link)
    page = ProductPage(browser, original_link)
    page.open()
    book_name, price = page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.check_book_name(book_name)
    page.check_price(price)

