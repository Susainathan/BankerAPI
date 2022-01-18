from fastapi import APIRouter, Depends, status, HTTPException
from tortoise import router
from app.models.pydantic import AddBank, UpdateBank
from . import crud


router = APIRouter(tags=["Adding Bank"])


@router.post('/bank', status_code=status.HTTP_201_CREATED)
async def add_bank(bank:AddBank):
    await crud.addbank(bank)

    responses = {
        "Bank_Name": bank.Bank_Name,
        "Bank_Masked_Name": bank.Bank_Masked_Name,
        "Toggle_Display": bank.Toggle_Display
    }
    return responses


@router.get("/bank/{Bank_Name}")
async def get_bank(Bank_Name: str):
    bank = await crud.get_bank(Bank_Name)
    print(bank)
    if not bank:
        raise HTTPException(status_code=404, detail=f"Bank {Bank_Name} not found")

    return bank


@router.get("/bank")
async def get_all():
    return await crud.get_all()

@router.put("/bank/{id}/")
async def update_bank(id: int, payload: UpdateBank):
    Banks = await crud.update_bank(id, payload)
    if not Banks:
        raise HTTPException(status_code=404, detail="Not found")

    return Banks


@router.delete("/bank/{Bank_Name}/")
async def delete_bank(Bank_Name: str):
    Bankss = await crud.delete_bank(Bank_Name)
    if not Bankss:
        raise HTTPException(status_code=404, detail="Bank details not found")

    await crud.delete_bank(Bank_Name)

    if Bankss:
        return {"Deleted"}