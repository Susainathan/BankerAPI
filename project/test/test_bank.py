from app.api import bank
import json


def test_add_bank(test_app):
    response = test_app.post("/bank", 
    json = {"Bank_Name":"Indian Bank", "Bank_Masked_Name":"IB", "Toggle_Display":"True"})
    print(response.json())
    assert response.status_code == 201
    assert response.json()['Bank_Name'] == "Indian Bank"
    assert response.json()['Bank_Masked_Name'] == "IB"
    assert response.json()['Toggle_Display'] == True



def test_add_bank_invalid_json(test_app):
    response = test_app.post("/bank", 
    data=json.dumps({"Bank_Masked_Name":"IB", "Toggle_Display":"True"}))
    print(response.json())
    assert response.status_code == 422



def test_get_bank(test_app):
    response = test_app.get("/bank/", json={"Bank_Name":"Indian Bank"})
    print(response.json())
    assert response.status_code == 200


def test_get_bank_incorrect_name(test_app):
    response = test_app.get("/bank/", json={"Bank_Name":"Bank"})
    print(response.json())
    assert response.status_code == 200



def test_delete_bank(test_app):
    response = test_app.post("/bank", json={"Bank_Name":"Indian Bank"})
    print(response.json())

    response = test_app.delete(f"/bank/Indian Bank/")
    assert response.status_code == 200



# def test_update_bank(test_app):
#     responses = test_app.put("/bank", 
#             json = {"Bank_Name":"Indian Bank", "Bank_Masked_Name":"IBI", "Toggle_Display":"True"})
#     print(responses.json())

#     response = test_app.put("/bank/1/", data=json.dumps(responses))
#     assert response.status_code == 200


def test_delete_bank_incorrect_id(test_app):
    response = test_app.delete("/bank/India Bank/")
    assert response.status_code == 404
    assert response.json()["detail"] == "Bank details not found"


def test_update_bank_incorrect_id(test_app):
    response = test_app.put(
        "/banka/Indian Bank/",
        json = {"Bank_Name":"Indian Bank", "Bank_Masked_Name":"IBI", "Toggle_Display":"True"})
    assert response.status_code == 404
    assert response.json()["detail"] == 'Not Found'


def test_update_bank_invalid_json(test_app):
    response = test_app.delete("/bank/Indian Bank/")
    update_bank = response.json()

    response = test_app.put(
        f"/bank/{update_bank}/",
        data=json.dumps({})
    )
    assert response.status_code == 422
