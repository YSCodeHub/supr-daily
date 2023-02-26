import uuid

from flask import Flask, request

from src.controllers.category_controller import CategoryController
from src.controllers.order_controller import OrderController
from src.controllers.warehouse_controller import WareHouseController
from src.services.category_service import CategoryService
from src.services.order_service import OrderService
from src.services.user_service import UserService
from src.controllers.user_controller import UserController
from src.services.ware_house_service import WareHouseService
from src.utils import load_data, check_order_possibility

app = Flask(__name__)


@app.route("/order/check", methods=["POST"])
def check_order():
    load_data()
    json_data = request.get_json(silent=True)
    date = json_data["delivery_date"]
    warehouse_id = json_data["warehouse_id"]
    items = json_data["items"]

    if type(check_order_possibility(items, warehouse_id, date)) is tuple:
        return {
            "can_fulfil": True
        }
    else:
        return {
            "can_fulfil": False
        }


@app.route("/order/reserve", methods=["POST"])
def reserve_order():
    load_data()
    json_data = request.get_json(silent=True)
    user = json_data["customer_id"]
    date = json_data["delivery_date"]
    warehouse_id = json_data["warehouse_id"]
    items = json_data["items"]
    order_id = uuid.uuid4()

    availability = check_order_possibility(items, warehouse_id, date)
    if type(availability) is None:
        return {
            "code": "Failure",
            "data": {
                "reserved": False,
                "message": "Insufficient quantities!"
            }
        }

    _, item_quantity, category_quantity = availability

    for key in item_quantity:
        WareHouseController(WareHouseService).update_warehouse_item_balance(warehouse_id, key, item_quantity[key])
        OrderController(OrderService).add_order(order_id, user, [key], [item_quantity[key]])

    for key in category_quantity:
        CategoryController(CategoryService).update_category_balance_per_date(key, date, category_quantity[key])

    UserController(UserService).add_order(user, order_id)

    return {
        "code": "Success",
        "data": {
            "reserved": True,
            "message": "Success"
        }
    }
