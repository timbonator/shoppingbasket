import pytest

from product_db import ProductDB


@pytest.fixture(scope='session')
def products() -> ProductDB:
    db_path = 'tests/db/full_product_db.yaml'
    return ProductDB.from_yaml(db_path)