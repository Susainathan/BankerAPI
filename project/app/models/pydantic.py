from pydantic import BaseModel
from pydantic import EmailStr
from typing import Optional
from datetime import date



class AddBank(BaseModel):
    Bank_Name: str
    Bank_Masked_Name: str
    Toggle_Display: bool = True


class UpdateBank(AddBank):
    Bank_Name: str
    Bank_Masked_Name: str
    Toggle_Display: bool = True


class AddSegment(BaseModel):
    Segment_Name: str
    Toggle_Segment: bool =True
    owner_id: int

class UpdateSegment(AddSegment):
    pass


class Segmentshow(BaseModel):
    Toggle_Segment: bool


class AddBanker(BaseModel):
    Bank: str
    Market_Segment: str
    Banker_Name: str
    Banker_Contact_No: int
    Banker_Email_Address: EmailStr
    Remarks: str
    Banker_Start_Date: Optional[date]
    Banker_status: str = "Active"

class AddBankerOut(BaseModel):
    Bank: str
    Market_Segment: str
    Banker_Name: str
    Banker_Contact_No: int
    Banker_Email_Address: EmailStr
    Remarks: str
    Banker_Start_Date: Optional[date]
    Banker_status: str


class UpdateBanker(AddBanker):
    Banker_End_Date: Optional[date]
class BankerToggle(BaseModel):
    Banker_status: str