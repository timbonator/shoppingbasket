from shoppingbasket.product_db import ProductDB


class TestProductDB:
    def test_from_yaml(self):
        db_path = 'shoppingbasket/tests/data/products.yaml'
        product_db = ProductDB.from_yaml(db_path)
        expected_products = {
            1: {'barcode': 1, 'name': 'Beans', 'unit_price': 0.50},
            2: {'barcode': 2, 'name': 'Onions', 'unit_price': 0.29, 'units': 'kg'},
        }
        assert product_db._products[1] == expected_products[1]
        assert product_db._products[2] == expected_products[2]
