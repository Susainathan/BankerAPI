from typing import Union
from pydantic import EmailStr
from fastapi import HTTPException
from starlette import status
from app.models.pydantic import AddBank, UpdateBank, AddSegment, UpdateSegment, AddBanker, UpdateBanker
from app.models.tortoise import Bank
from app.models.tortoise import Segment, Banker



async def addbank(payload: AddBank):
    banks= Bank(
        Bank_Name=payload.Bank_Name,
        Bank_Masked_Name=payload.Bank_Masked_Name,
        Toggle_Display=payload.Toggle_Display
    )

    await banks.save()


async def update_bank(id: int, payload: UpdateBank) -> Union[dict, None]:
    summary = await Bank.filter(id=id).update(
        Bank_Name=payload.Bank_Name, Bank_Masked_Name=payload.Bank_Masked_Name, Toggle_Display=payload.Toggle_Display
    )
    if summary:
        updated_summary = await Bank.filter(id=id).first().values()
        return updated_summary
    return None


async def get_bank(Bank_Name: str):
    bank = await Bank.filter(Bank_Name=Bank_Name).first().values()
    if bank:
        return bank
    return bank


async def get_all():
    summaries = await Bank.all().values()
    return summaries


async def delete_bank(Bank_Name: str):
    del_bank = await Bank.filter(Bank_Name=Bank_Name).first().delete()
    return del_bank

# Segments

async def addsegment(payload: AddSegment):
    segment = Segment(
        Segment_Name=payload.Segment_Name,
        Toggle_Segment=payload.Toggle_Segment,
        owner_id=payload.owner_id
    )
    await segment.save()


async def update_seg(id: int, payload: UpdateSegment) -> Union[dict, None]:
    summary = await Segment.filter(id=id).update(
        Segment_Name=payload.Segment_Name, Toggle_Segment=payload.Toggle_Segment, owner_id=payload.owner_id
    )
    if summary:
        updated_summary = await Segment.filter(id=id).first().values()
        return updated_summary
    return None


async def toggle_banker_segment(id: int):
    segment = await Segment.filter(id=id).first().values()
    if segment:
        return segment
    return segment



async def delete_segment(id: int):
    del_segment = await Segment.filter(id=id).first().delete()
    return del_segment




# Banker
async def create_banker(payload: AddBanker):
    add_bankers = Banker(
        Bank=payload.Bank,
        Market_Segment=payload.Market_Segment,
        Banker_Name=payload.Banker_Name,
        Banker_Contact_No=payload.Banker_Contact_No,
        Banker_Email_Address=payload.Banker_Email_Address,
        Remarks=payload.Remarks,
        Banker_Start_Date=payload.Banker_Start_Date,
        Banker_status=payload.Banker_status
    )
    await add_bankers.save()

async def update_banker(id: int, payload: UpdateBanker) -> Union[dict, None]:
    segment = await Banker.filter(id=id).update(
        Bank=payload.Bank,
        Market_Segment=payload.Market_Segment,
        Banker_Name=payload.Banker_Name,
        Banker_Contact_No=payload.Banker_Contact_No,
        Banker_Email_Address=payload.Banker_Email_Address,
        Remarks=payload.Remarks,
        Banker_Start_Date=payload.Banker_Start_Date,
        Banker_status=payload.Banker_status
    )
    if segment:
        updated_segment = await Banker.filter(id=id).first().values()
        return updated_segment
    return None



async def get_all_bankers():
    bankers = await Banker.all().values()
    return bankers


async def Toggle_Banker_status(id: int):
    banker = await Banker.filter(id=id).first().values()
    if banker:
        return banker
    return banker


async def delete_banker(id: int):
    del_banker = await Banker.filter(id=id).first().delete()
    return del_banker



async def search_banker_by_contact_no(Banker_Contact_Number: int):
    banker = await Banker.filter(Banker_Contact_Number=Banker_Contact_Number).first().values()
    if not banker:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="not found")
    return banker

