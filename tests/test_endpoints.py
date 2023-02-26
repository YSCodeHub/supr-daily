from pathlib import Path
import json

ORDER_CHECK_PATH = Path(__file__).parent.parent.joinpath("test_data", "order_check.json")
ORDER_RESERVE_PATH = Path(__file__).parent.parent.joinpath("test_data", "order_reserve.json")


def test_order_check(client):
    response = client.post('/order/check', json=json.load(open(ORDER_CHECK_PATH, "r"))).json
    assert response == {
        "can_fulfil": True
    }


def test_order_reserve(client):
    response = client.post('/order/reserve', json=json.load(open(ORDER_RESERVE_PATH, "r"))).json
    assert response["code"] == "Success"
