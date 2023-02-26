from pathlib import Path
import json

from src.controllers.category_controller import CategoryController
from src.controllers.item_controller import ItemController
from src.controllers.user_controller import UserController
from src.controllers.warehouse_controller import WareHouseController
from src.services.category_service import CategoryService
from src.services.user_service import UserService
from src.services.item_service import ItemService
from src.services.ware_house_service import WareHouseService

FIXTURES_PATH = Path(__file__).parent.parent.joinpath("fixtures")


def load_data():
    categories_path = FIXTURES_PATH.joinpath("categories.json")
    items_path = FIXTURES_PATH.joinpath("items.json")
    users_path = FIXTURES_PATH.joinpath("users.json")
    warehouses_path = FIXTURES_PATH.joinpath("warehouses.json")

    categories = json.load(open(categories_path, "r"))
    items = json.load(open(items_path, "r"))
    users = json.load(open(users_path, "r"))
    warehouses = json.load(open(warehouses_path, "r"))

    for category in categories:
        CategoryController(CategoryService).add_category(category["id"], category["name"], category["details"])

    for item in items:
        ItemController(ItemService).add_item(item["id"], item["name"], item["category"])

    for user in users:
        UserController(UserService).add_user(user["id"], user["name"], user["orders"])

    for warehouse in warehouses:
        WareHouseController(WareHouseService).add_warehouse(warehouse["id"], warehouse["item_details"])


def check_order_possibility(items, warehouse_id, date):
    item_quantity, category_quantity = {}, {}
    for item in items:
        if item["item_id"] in item_quantity:
            item_quantity[item["item_id"]] += item["quantity"]
        else:
            item_quantity[item["item_id"]] = item["quantity"]
        if item["category"] in category_quantity:
            category_quantity[item["category"]] += item["quantity"]
        else:
            category_quantity[item["category"]] = item["quantity"]

    for key in item_quantity:
        warehouse_quantity = WareHouseController(WareHouseService).get_warehouse_item_balance(warehouse_id, key)
        if not warehouse_quantity or warehouse_quantity < item_quantity[key]:
            return False

    for key in category_quantity:
        category_quantity_new = CategoryController(CategoryService).category_balance_per_date(key, date)
        if not category_quantity_new or category_quantity_new < category_quantity[key]:
            return False

    return True, item_quantity, category_quantity
