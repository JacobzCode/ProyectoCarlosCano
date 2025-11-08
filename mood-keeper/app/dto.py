from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class AccountCreate(BaseModel):
    handle: str
    email: EmailStr
    secret: str

class SessionCreate(BaseModel):
    handle: str
    secret: str

class AccountOut(BaseModel):
    id: int
    handle: str
    email: str
    created: datetime

class EntryCreate(BaseModel):
    mood: int
    comment: Optional[str] = None

class EntryOut(BaseModel):
    id: int
    account_id: int
    handle: str
    mood: int
    comment: Optional[str]
    created: datetime
