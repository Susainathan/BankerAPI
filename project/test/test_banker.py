import json

def test_create_banker(test_app):
    response = test_app.post("/Banker", 
    json={"Bank": "string",
  "Market_Segment": "string",
  "Banker_Name": "string",
  "Banker_Contact_No": 0,
  "Banker_Email_Address": "user@example.com",
  "Remarks": "string",
  "Banker_Start_Date": "2022-01-07",
  "Banker_status": "Active"})

    print(response.json())
    assert response.status_code == 201
    assert response.json()['Bank'] == "string"
    assert response.json()['Market_Segment'] == "string"
    assert response.json()['Banker_Name'] == "string"
    assert response.json()['Banker_Contact_No'] == 0
    assert response.json()['Banker_Email_Address'] == "user@example.com"
    assert response.json()['Remarks'] == "string"
    assert response.json()['Banker_Start_Date'] == "2022-01-07"
    assert response.json()['Banker_status'] == "Active"


def test_create_banker_invalid_json(test_app):
    response = test_app.post("/Banker", 
    json={"Bank": "string",
  "Market_Segment": "string",
  "Banker_Name": "string",
  "Banker_Contact_No": 0,
  "Remarks": "string",
  "Banker_Start_Date": "2022-01-07",
  "Banker_status": "Active"})

    print(response.json())
    assert response.status_code == 422


def test_update_banker(test_app):
    test_update_data = {
        "Bank": "string",
        "Market_Segment": "string",
        "Banker_Name": "string",
        "Banker_Contact_No": 0,
        "Banker_Email_Address": "user@example.com",
        "Remarks": "string",
        "Banker_Start_Date": "2022-01-07",
        "Banker_status": "Active"}
    response = test_app.put("/Banker/1/", data=json.dumps(test_update_data))
    print(response.json())
    assert response.status_code == 200


def test_update_banker_incorrect_id(test_app):
    response = test_app.put(
        "/Banker/9909/",
        json={"Bank": "string1",
  "Market_Segment": "string1",
  "Banker_Name": "string",
  "Banker_Contact_No": 0,
  "Banker_Email_Address": "user@example.com",
  "Remarks": "string",
  "Banker_Start_Date": "2022-01-07",
  "Banker_status": "Active",
  "Banker_End_Date": "2021-01-07"})
    assert response.status_code == 404
    assert response.json()["detail"] == 'Bank not found'


def test_update_banker_invalid_json(test_app):
    response = test_app.post("/Banker/5/")
    update_bank = response.json()

    response = test_app.put(
        f"/bank/{update_bank}/",
        data=json.dumps({})
    )
    assert response.status_code == 422


def test_get_all_bankers(test_app):
    response = test_app.get("/Banker", json={})
    print(response.json())
    assert response.status_code == 200


def test_get_banker(test_app):
    response = test_app.get("/Banker/1")
    print(response.json())
    assert response.status_code == 200



def test_get_invaid_banker(test_app):
    responses = test_app.get("/Banker/9999")
    assert responses.status_code == 404


# def test_delete_banker(test_app):
#     response = test_app.post("/Banker/1")
#     print(response.json())

#     response = test_app.delete("/Banker/1/")
#     assert response.status_code == 200


def test_delete_banker_incorrect_id(test_app):
    response = test_app.post("/Banker/123")
    print(response.json())

    response = test_app.delete("/Banker/123/")
    assert response.status_code == 404


def test_get_banker(test_app):
    response = test_app.get("/Banker/", json={"Banker_Contact_Number":0})
    print(response.json())
    assert response.status_code == 200

def test_get_bank_incorrect_contact_number(test_app):
    response = test_app.get("/Banker/123")
    print(response.json())
    assert response.status_code == 404
    assert response.json()['detail'] == "Banker not found"