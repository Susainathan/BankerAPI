from pydantic import EmailStr
from fastapi import APIRouter, Depends, status, HTTPException
from typing import List
from app.models.pydantic import AddBanker, UpdateBanker, BankerToggle

from . import crud


router = APIRouter(tags=["Banker API"])


@router.post("/Banker", status_code=status.HTTP_201_CREATED)
async def create_bankers(payload: AddBanker):
    await crud.create_banker(payload)
    banker_response = {
        "Bank": payload.Bank,
        "Market_Segment": payload.Market_Segment,
        "Banker_Name": payload.Banker_Name,
        "Banker_Contact_No": payload.Banker_Contact_No,
        "Banker_Email_Address": payload.Banker_Email_Address,
        "Remarks": payload.Remarks,
        "Banker_Start_Date": payload.Banker_Start_Date,
        "Banker_status": payload.Banker_status
    }
    return banker_response


@router.put("/Banker/{id}/")
async def update_bank(id: int, payload: UpdateBanker):
    Bankers = await crud.update_banker(id, payload)
    if not Bankers:
        raise HTTPException(status_code=404, detail="Bank not found")

    return Bankers



@router.get("/Banker")
async def get_all_bankers():
    return await crud.get_all_bankers()


@router.get("/Banker/{id}", response_model=BankerToggle)
async def get_toggle_status(id: int)-> BankerToggle:
    banker = await crud.Toggle_Banker_status(id)
    if not banker:
        raise HTTPException(status_code=404, detail="Banker not found")
    return banker


@router.delete("/Banker/{id}/")
async def delete_banker(id: int):
    segment = await crud.delete_banker(id)
    if not segment:
        raise HTTPException(status_code=404, detail="Banker not found")

    await crud.delete_banker(id)

    if segment:
        return {"Message":"Deleted"}


@router.get("/Banker/{Banker_Contact_Number}")
async def get_banker(Banker_Contact_Number: int):
    banker = await crud.search_banker_by_contact_no(Banker_Contact_Number)
    return banker