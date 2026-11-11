from product import Product
from inventory import Inventory
import pytest
import json

product = Product("Laptop", 50000, 2)

def test_product_name():
    assert product.name == "Laptop"
def test_product_price():
    assert product.price == 50000
def test_product_quantity():
    assert product.quantity == 2

def test_invalid_product_price():
    with pytest.raises(ValueError):
        Product("Laptop", -500, 2)



def test_stock():
    product = Product("Mouse", 800, 4)
    assert product.calculate_stock_value() == 3200


def test_add_product():
    inventory = Inventory()
    product = Product("Laptop", 50000, 2)
    inventory.add_product(product)
    assert len(inventory.products)==1
    assert inventory.products == [product]


def test_search_product():
    inventory = Inventory()
    product = Product("Laptop", 50000, 2)
    inventory.add_product(product)
    result = inventory.search_product("laptop")
    assert result is not None
    assert result.name == "Laptop"


def test_update_quantity():
    inventory = Inventory()
    product = Product("Laptop", 50000, 2)
    inventory.add_product(product)
    result =inventory.update_quantity("Laptop",10)
    assert result is True
    assert inventory.products[0].quantity == 10


def test_invalid_quantity_update():
    inventory = Inventory()
    product = Product("Laptop", 50000, 2)
    inventory.add_product(product)
    with pytest.raises(ValueError):
        inventory.update_quantity("Laptop",-5)
    assert product.quantity == 2


def test_delete_product():
    inventory = Inventory()
    product = Product("Laptop", 50000, 2)
    inventory.add_product(product)
    result = inventory.delete_product("Laptop")
    assert result is True
    assert len(inventory.products) == 0


def test_total_inventory_value():
    inventory = Inventory()
    product1 = Product("Laptop", 50000, 2)
    product2 = Product("Mouse", 800, 4)
    product3 = Product("Keyboard", 1500, 3)
    inventory.add_product(product1)
    inventory.add_product(product2)
    inventory.add_product(product3)
    assert inventory.calculate_total_inventory_value() == 107700
    


def test_empty_inventory_value():
    inventory = Inventory()
    assert inventory.calculate_total_inventory_value() == 0


def test_low_stock_products(capsys):
    inventory = Inventory()
    product1 = Product("Laptop", 50000, 2)
    product2 = Product("Mouse", 800, 5)
    product3 = Product("Keyboard", 1500, 1)
    inventory.add_product(product1)
    inventory.add_product(product2)
    inventory.add_product(product3)
    inventory.show_low_stock_products(3)
    captured = capsys.readouterr()
    assert "Laptop" in captured.out
    assert "Keyboard" in captured.out
    assert "Mouse" not in captured.out


def test_invalid_low_stock_threshold():
    inventory = Inventory()
    product1 = Product("Laptop",50000,2)
    product2 = Product("Mouse",500,3)
    inventory.add_product(product1)
    inventory.add_product(product2)
    with pytest.raises(ValueError):
        inventory.show_low_stock_products(-3)


def test_save_to_file(tmp_path):
    inventory = Inventory()
    inventory.add_product(Product("Laptop",50000,2))
    inventory.add_product(Product("Mouse",800,4))
    file_path = tmp_path / "test_products.json"
    inventory.save_to_file(file_path)
    assert file_path.exists()
    with open(file_path, "r") as file:
        data = json.load(file)
        assert len(data) == 2
        assert data[0]["name"] == "Laptop"
        assert data[1]["price"] == 800
        assert data[0]["quantity"] == 2


def test_load_from_file(tmp_path):
    inventory = Inventory()
    file_path = tmp_path / "test_products.json"
    data = [
    {"name": "Laptop", "price": 50000, "quantity": 2},
    {"name": "Mouse", "price": 800, "quantity": 4}
]
    with open(file_path, "w") as file:
        json.dump(data,file,indent=4)

    inventory.load_from_file(file_path)
    assert len(inventory.products) == 2
    assert inventory.products[0].name == "Laptop"
    assert inventory.products[1].quantity == 4
    assert isinstance(inventory.products[0],Product)


def test_repeated_loading(tmp_path):
    inventory = Inventory()
    file_path = tmp_path / "test_products.json"
    data = [
    {"name": "Laptop", "price": 50000, "quantity": 2},
    {"name": "Mouse", "price": 800, "quantity": 4}
]
    with open(file_path, "w") as file:
        json.dump(data,file,indent=4)
    
    inventory.load_from_file(file_path)
    inventory.load_from_file(file_path)
    assert len(inventory.products) == 2