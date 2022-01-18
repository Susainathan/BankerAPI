import json
from urllib import response


def test_add_segment(test_app):
    response = test_app.post("/segment", 
    json = {"Segment_Name": "string","Toggle_Segment": "true", "owner_id": 1})
    print(response.json())
    assert response.status_code == 201
    assert response.json()['Segment_Name'] == "string"
    assert response.json()['Toggle_Segment'] == True
    assert response.json()['owner_id'] == 1



def test_add_segment_invalid_json(test_app):
    response = test_app.post("/segment", 
    data=json.dumps({"Bank_Name": "IOB", "Toggle_Segment":"True"}))
    print(response.json())
    assert response.status_code == 422


def test_get_segment(test_app):
    response = test_app.get("/segment/1")
    print(response.json())
    assert response.status_code == 200


def test_get_segment_incorrect_id(test_app):
    response = test_app.get("/segment/123")
    print(response.json())
    assert response.status_code == 404


def test_update_segment(test_app):
    test_update_data = {
        "Segment_Name": "string",
        "Toggle_Segment": False,
        "owner_id": 1
        }
    response = test_app.put("/segment/1/", data=json.dumps(test_update_data))
    print(response.json())
    assert response.status_code == 200

def test_update_segment_incorrect_id(test_app):
    test_update_data = {
        "Segment_Name": "string",
        "Toggle_Segment": False,
        "owner_id": 1
        }
    response = test_app.put("/segment/13456/", data=json.dumps(test_update_data))
    print(response.json())
    assert response.status_code == 404


def test_update_segment_invalid_json(test_app):
    response = test_app.post("/segment/1/")
    update_seg = response.json()

    response = test_app.put(
        f"/bank/{update_seg}/",
        data=json.dumps({})
    )
    assert response.status_code == 422


def test_delete_segment(test_app):
    response = test_app.post("/segment/1")
    print(response.json())

    response = test_app.delete("/segment/1/")
    assert response.status_code == 200


def test_delete_segment_invalid_id(test_app):
    response = test_app.post("/segment/123")
    print(response.json())

    response = test_app.delete("/segment/123/")
    assert response.status_code == 404
