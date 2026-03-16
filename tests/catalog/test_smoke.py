import pytest
from pages.catalog_page import CatalogPage


@pytest.mark.smoke
def test_catalog_page_load(browser, base_url):

    catalog = CatalogPage(browser)

    # 1️⃣ Открываем страницу
    catalog.open(base_url)

    # 2️⃣ Ждём, пока каталог загрузится
    catalog.wait_page_loaded()

    # 3️⃣ Получаем список товаров
    products = catalog.get_products()

    assert len(products) > 0, "Товары в каталоге не отображаются"
