from fastapi import APIRouter, Depends, status, HTTPException
from app.models.pydantic import AddSegment, UpdateSegment, Segmentshow
from app.models.tortoise import Segment
from . import crud


router = APIRouter(tags=["Segments"])


@router.post('/segment', status_code=status.HTTP_201_CREATED)
async def add_segment(Seg: AddSegment):
    await crud.addsegment(Seg)

    responses = {
        "Segment_Name": Seg.Segment_Name,
        "Toggle_Segment":Seg.Toggle_Segment,
        "owner_id":Seg.owner_id
    }   
    return responses


@router.put("/segment/{id}/")
async def update_bank(id: int, payload: UpdateSegment):
    Bankers = await crud.update_seg(id, payload)
    if not Bankers:
        raise HTTPException(status_code=404, detail="Segment not found")

    return Bankers


@router.get('/segment/{id}', response_model=Segmentshow)
async def get_segment_status(id: int)->Segmentshow:
    segment = await crud.toggle_banker_segment(id)
    if not segment:
        raise HTTPException(status_code=404, detail="Segment not found")
    return segment
    
@router.delete("/segment/{id}/")
async def delete_segment(id: int):
    segment = await crud.delete_segment(id)
    if not segment:
        raise HTTPException(status_code=404, detail="segment not found")

    await crud.delete_bank(id)

    if segment:
        return {"Message":"Deleted"}
